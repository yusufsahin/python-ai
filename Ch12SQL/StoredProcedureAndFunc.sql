USE [northwind]
GO
CREATE VIEW EndOfLifeProducts AS
SELECT * FROM Products Where Discontinued=1;

INSERT INTO [dbo].[EndOfLifeProducts]
           ([ProductName]
           ,[SupplierID]
           ,[CategoryID]
           ,[QuantityPerUnit]
           ,[UnitPrice]
           ,[UnitsInStock]
           ,[UnitsOnOrder]
           ,[ReorderLevel]
           ,[Discontinued])
     VALUES
           ('Apple Juice'
           ,1
           ,2
           ,'40 per Box'
           ,7.5
           ,50
           ,10
           ,25
           ,0);

UPDATE [dbo].[EndOfLifeProducts]
   SET [UnitsInStock] = 60
 WHERE ProductID=53;

SELECT * FROM [dbo].[EndOfLifeProducts];

SELECT * FROM Products;


DELETE FROM [EndOfLifeProducts] WHERE ProductID=80

CREATE VIEW View_Country_Revenue AS
SELECT
    c.Country,
    SUM(od.UnitPrice * od.Quantity) AS TotalRevenue
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
JOIN [Order Details] od ON o.OrderID = od.OrderID
GROUP BY c.Country;

SELECT * FROM View_Country_Revenue


CREATE PROCEDURE GetProductsByCategory
	@CategoryID INT=NULL
AS 
BEGIN
SELECT ProductID,ProductName,CategoryID,UnitPrice,UnitsInStock FROM Products
	WHERE (@CategoryID IS NULL OR CategoryID=@CategoryID)
	ORDER BY ProductName
END;

EXEC GetProductsByCategory;

EXEC GetProductsByCategory @CategoryID=1
EXEC GetProductsByCategory @CategoryID=2
CREATE PROCEDURE GetProductsByCategoryName
	@CategoryName NVARCHAR(15)=NULL --Opsiyonel  Parametre
AS 
BEGIN
	SET NOCOUNT ON;
	SELECT 
		p.ProductID,
		p.ProductName,
		c.CategoryName,
		p.UnitPrice,
		p.UnitsInStock 
	FROM Products p 
	INNER JOIN Categories c on p.CategoryID=c.CategoryID
	WHERE (@CategoryName IS NULL OR c.CategoryName=@CategoryName)
	ORDER BY p.ProductName;
END;

EXEC GetProductsByCategoryName;

EXEC GetProductsByCategoryName @CategoryName='Beverages';
EXEC GetProductsByCategoryName @CategoryName='Produce';

ALTER PROCEDURE GetProductsByCategoryName
	@CategoryName NVARCHAR(15)=NULL --Opsiyonel  Parametre
AS 
BEGIN
	SET NOCOUNT ON;
	SELECT 
		p.ProductID,
		p.ProductName,
		c.CategoryName,
		p.UnitPrice,
		p.UnitsInStock 
	FROM Products p 
	INNER JOIN Categories c on p.CategoryID=c.CategoryID
	WHERE (@CategoryName IS NULL OR c.CategoryName LIKE '%'+@CategoryName+'%')
	ORDER BY p.ProductName;
END;

EXEC GetProductsByCategoryName;

EXEC GetProductsByCategoryName @CategoryName='Con';
EXEC GetProductsByCategoryName @CategoryName='Produce';
EXEC GetProductsByCategoryName @CategoryName='Grains';
SELECT * FROM Categories

CREATE PROCEDURE GetProductsByCategoryName2
	@CategoryName NVARCHAR(15)=NULL --Opsiyonel  Parametre
AS 
BEGIN
	SET NOCOUNT ON;
	SELECT 
		p.ProductID,
		p.ProductName,
		c.CategoryName,
		p.UnitPrice,
		p.UnitsInStock 
	FROM Products p 
	INNER JOIN Categories c on p.CategoryID=c.CategoryID
	WHERE (@CategoryName IS NULL OR c.CategoryName=@CategoryName)
	ORDER BY p.ProductName;
END;

EXEC GetProductsByCategoryName2 @CategoryName='Grains';
EXEC GetProductsByCategoryName2 @CategoryName='Grains/Cereals';

--CustomerOrderCount Müşterinin toplam sipariş sayısı

CREATE PROCEDURE GetCustomerOrderCount
	@CustomerID NCHAR(5)
AS 
BEGIN
	SELECT
		c.CustomerID,
		c.CompanyName,
		COUNT(o.OrderID) AS OrderCount
	FROM Customers c
	LEFT JOIN Orders o ON c.CustomerID=o.CustomerID
	WHERE c.CustomerID=@CustomerID
	GROUP BY c.CustomerID,c.CompanyName
END;

EXEC GetCustomerOrderCount @CustomerID='ALFKI'

---Ürün ekleme / INSERT

CREATE PROCEDURE InsertNewProduct
@ProductName NVARCHAR(40),
@CategoryID INT,
@UnitPrice MONEY,
@UnitsInStock SMALLINT
AS 
BEGIN
	SET NOCOUNT ON;
	INSERT INTO Products(ProductName,CategoryID,UnitPrice,UnitsInStock)
	VALUES (@ProductName,@CategoryID,@UnitPrice,@UnitsInStock);
	SELECT SCOPE_IDENTITY() as NewProductID;
END;

EXEC InsertNewProduct
	@ProductName='New Sample Product',
	@CategoryID=1,
	@UnitPrice=19.99,
	@UnitsInStock=50;

	SELECT * FROM Products;

CREATE PROCEDURE UpdateProductStock
    @ProductID INT,
    @NewUnitsInStock SMALLINT
AS
BEGIN
    SET NOCOUNT ON;

    UPDATE Products
    SET UnitsInStock = @NewUnitsInStock
    WHERE ProductID = @ProductID;
END;

EXEC UpdateProductStock @ProductID = 5, @NewUnitsInStock = 100;

SELECT * FROM Products WHERE ProductID=5;


CREATE PROCEDURE DeleteProduct
    @ProductID INT
AS
BEGIN
    SET NOCOUNT ON;

    DELETE FROM Products
    WHERE ProductID = @ProductID;
END;

EXEC DeleteProduct @ProductID = 81;
SELECT * FROM Products WHERE ProductID=81;

-- Girilen Sipariş Numarasına göre Sipariş tutarını hesapla
--SCALAR FUNC. 
CREATE FUNCTION GetOrderTotal(@OrderID INT)
RETURNS MONEY 
AS
BEGIN
	DECLARE @Total MONEY;
	SELECT @Total=SUM(UnitPrice * Quantity * (1-Discount))
		FROM [Order Details]
		WHERE OrderID=@OrderID;
	RETURN @Total;
END;

SELECT dbo.GetOrderTotal(10248) as TotalAmount;

SELECT dbo.GetOrderTotal(10250) as TotalAmount;

--Table-Valued Func.

CREATE FUNCTION GetOrdersByCustomer(@CustomerID NCHAR(5))
RETURNS TABLE
AS 
RETURN(
SELECT
	o.OrderID,
	o.OrderDate,
	dbo.GetOrderTotal(o.OrderID) AS TotalAmount
FROM Orders o
WHERE o.CustomerID=@CustomerID
);

SELECT * FROM dbo.GetOrdersByCustomer('ALFKI');



SELECT OrderID,TotalAmount FROM dbo.GetOrdersByCustomer('ALFKI');

CREATE FUNCTION dbo.GetTotalSalesByCategoryAndDate
(
    @CategoryName NVARCHAR(15),
    @StartDate DATETIME,
    @EndDate DATETIME
)
RETURNS MONEY
AS
BEGIN
    DECLARE @TotalSales MONEY;

    SELECT @TotalSales = SUM(od.UnitPrice * od.Quantity * (1 - od.Discount))
    FROM Orders o
    INNER JOIN [Order Details] od ON o.OrderID = od.OrderID
    INNER JOIN Products p ON od.ProductID = p.ProductID
    INNER JOIN Categories c ON p.CategoryID = c.CategoryID
    WHERE 
        c.CategoryName = @CategoryName
        AND o.OrderDate BETWEEN @StartDate AND @EndDate;

    RETURN @TotalSales;
END;
SELECT dbo.GetTotalSalesByCategoryAndDate('Beverages', '1997-01-01', '1997-12-31') AS TotalSales;
SELECT dbo.GetTotalSalesByCategoryAndDate('Beverages', '2000-01-01', '2000-12-31') AS TotalSales;


ALTER FUNCTION dbo.GetTotalSalesByCategoryAndDate
(
    @CategoryName NVARCHAR(15),
    @StartDate DATETIME,
    @EndDate DATETIME
)
RETURNS MONEY
AS
BEGIN
    DECLARE @TotalSales MONEY;

    SELECT @TotalSales = SUM(od.UnitPrice * od.Quantity * (1 - od.Discount))
    FROM Orders o
    INNER JOIN [Order Details] od ON o.OrderID = od.OrderID
    INNER JOIN Products p ON od.ProductID = p.ProductID
    INNER JOIN Categories c ON p.CategoryID = c.CategoryID
    WHERE 
        c.CategoryName = @CategoryName
        AND o.OrderDate BETWEEN @StartDate AND @EndDate;

    RETURN ISNULL(@TotalSales,0);
END;

SELECT dbo.GetTotalSalesByCategoryAndDate('Beverages', '1997-01-01', '1997-12-31') AS TotalSales;
SELECT dbo.GetTotalSalesByCategoryAndDate('Beverages', '2000-01-01', '2000-12-31') AS TotalSales;
