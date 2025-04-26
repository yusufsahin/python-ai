CREATE TABLE ProductLogs (
    LogID INT IDENTITY(1,1) PRIMARY KEY,  -- Otomatik artan ID
    ProductID INT NOT NULL,
    LogDate DATETIME NOT NULL
);


CREATE TRIGGER Loglama
ON Products
AFTER UPDATE
AS
BEGIN
    SET NOCOUNT ON;

    INSERT INTO ProductLogs (ProductID, LogDate)
    SELECT d.ProductID, GETDATE()
    FROM DELETED d;
END;

UPDATE [dbo].[Products]
   SET [UnitPrice] = 17     
WHERE ProductID=5

SELECT * FROM Products WHERE ProductID=5;

SELECT * FROM ProductLogs;

CREATE TRIGGER tgr_AfterInsertProducts ON Products
AFTER INSERT
AS
BEGIN
	SET NOCOUNT ON;
	INSERT INTO ProductLogs (ProductID,LogDate)
	SELECT ProductID,GETDATE()
	FROM INSERTED;
END;

INSERT INTO [dbo].[Products]
           ([ProductName],[SupplierID],[CategoryID],[QuantityPerUnit],[UnitPrice],[UnitsInStock],[UnitsOnOrder],[ReorderLevel],[Discontinued])
     VALUES
           ('New Product',2,2,'10 in a Box',17,75,10,15,0)

SELECT * FROM Products 

SELECT * FROM ProductLogs

CREATE TRIGGER trg_AfterDelete_Products
ON Products
AFTER DELETE
AS
BEGIN
	SET NOCOUNT ON;
	INSERT INTO ProductLogs(ProductID,LogDate)
	SELECT ProductID,GETDATE()
	FROM DELETED;
END;

DELETE FROM Products WHERE ProductID=82;
SELECT * FROM ProductLogs;

CREATE TABLE CategoryLogs (
    LogID INT IDENTITY(1,1) PRIMARY KEY,
    CategoryID INT NOT NULL,
    ActionType NVARCHAR(10) NOT NULL,  -- 'INSERT', 'UPDATE', 'DELETE'
    LogDate DATETIME NOT NULL
);

CREATE TRIGGER trg_Categories_LogAllActions
ON Categories
AFTER INSERT, UPDATE, DELETE
AS
BEGIN
    SET NOCOUNT ON;

    -- INSERT için: INSERTED tablosunda kayıt var, DELETED yok
    INSERT INTO CategoryLogs (CategoryID, ActionType, LogDate)
    SELECT CategoryID, 'INSERT', GETDATE()
    FROM INSERTED
    WHERE NOT EXISTS (
        SELECT 1 FROM DELETED d WHERE d.CategoryID = INSERTED.CategoryID
    );

    -- DELETE için: DELETED tablosunda kayıt var, INSERTED yok
    INSERT INTO CategoryLogs (CategoryID, ActionType, LogDate)
    SELECT CategoryID, 'DELETE', GETDATE()
    FROM DELETED
    WHERE NOT EXISTS (
        SELECT 1 FROM INSERTED i WHERE i.CategoryID = DELETED.CategoryID
    );

    -- UPDATE için: Hem INSERTED hem DELETED tablosunda aynı CategoryID var
    INSERT INTO CategoryLogs (CategoryID, ActionType, LogDate)
    SELECT i.CategoryID, 'UPDATE', GETDATE()
    FROM INSERTED i
    JOIN DELETED d ON i.CategoryID = d.CategoryID;
END;

INSERT INTO Categories (CategoryName)
VALUES ('New Category');

SELECT * FROM Categories;
SELECT * FROM CategoryLogs;

UPDATE Categories SET CategoryName='U Category' WHERE CategoryID =9;
SELECT * FROM Categories;
SELECT * FROM CategoryLogs;

DELETE FROM Categories WHERE CategoryID =9;

SELECT * FROM Categories;
SELECT * FROM CategoryLogs;

CREATE TRIGGER trg_PreventProductDelete
ON Products
INSTEAD OF DELETE --BEFORE DELETE
AS
BEGIN
    RAISERROR ('Ürün silinemez! Silme işlemi engellendi.', 16, 1);
    ROLLBACK TRANSACTION;
END;

SELECT * FROM Products;

DELETE FROM Products WHERE ProductID=1;

CREATE TRIGGER trg_PreventNegativeStock_Products_Insert
ON Products
INSTEAD OF INSERT
AS
BEGIN
    SET NOCOUNT ON;

    IF EXISTS (
        SELECT 1 FROM INSERTED WHERE UnitsInStock < 0
    )
    BEGIN
        RAISERROR('Ürün eklenemez: Stok miktarı negatif olamaz!', 16, 1);
        ROLLBACK TRANSACTION;
        RETURN;
    END;

    INSERT INTO Products (ProductName, SupplierID, CategoryID, QuantityPerUnit, UnitPrice, UnitsInStock)
    SELECT ProductName, SupplierID, CategoryID, QuantityPerUnit, UnitPrice, UnitsInStock
    FROM INSERTED;
END;

CREATE TRIGGER trg_PreventNegativeStock_Products_Update
ON Products
INSTEAD OF UPDATE
AS
BEGIN
    SET NOCOUNT ON;

    IF EXISTS (
        SELECT 1 FROM INSERTED WHERE UnitsInStock < 0
    )
    BEGIN
        RAISERROR('Ürün güncellenemez: Stok miktarı negatif olamaz!', 16, 1);
        ROLLBACK TRANSACTION;
        RETURN;
    END;

    UPDATE p
    SET 
        p.ProductName = i.ProductName,
        p.SupplierID = i.SupplierID,
        p.CategoryID = i.CategoryID,
        p.QuantityPerUnit = i.QuantityPerUnit,
        p.UnitPrice = i.UnitPrice,
        p.UnitsInStock = i.UnitsInStock
    FROM Products p
    JOIN INSERTED i ON p.ProductID = i.ProductID;
END;


CREATE TRIGGER trg_PreventNegativeStock_OrderDetails_Insert
ON [Order Details]
AFTER INSERT
AS
BEGIN
    SET NOCOUNT ON;

    -- UnitsInStock kontrolü (stok yetersizse iptal)
    IF EXISTS (
        SELECT 1
        FROM INSERTED i
        JOIN Products p ON i.ProductID = p.ProductID
        WHERE p.UnitsInStock - i.Quantity < 0
    )
    BEGIN
        RAISERROR('Yetersiz stok! Sipariş oluşturulamaz.', 16, 1);
        ROLLBACK TRANSACTION;
        RETURN;
    END;

    -- Stokları güncelle (sipariş miktarı kadar düşür)
    UPDATE p
    SET p.UnitsInStock = p.UnitsInStock - i.Quantity
    FROM Products p
    JOIN INSERTED i ON p.ProductID = i.ProductID;
END;

CREATE TRIGGER trg_UpdateStock_OrderDetails_Delete
ON [Order Details]
AFTER DELETE
AS
BEGIN
    SET NOCOUNT ON;

    -- Silinen siparişin miktarını stoka geri ekle
    UPDATE p
    SET p.UnitsInStock = p.UnitsInStock + d.Quantity
    FROM Products p
    JOIN DELETED d ON p.ProductID = d.ProductID;
END;

CREATE TRIGGER trg_PreventNegativeStock_OrderDetails_Update
ON [Order Details]
AFTER UPDATE
AS
BEGIN
    SET NOCOUNT ON;

    -- Önce stok yetecek mi kontrol et
    IF EXISTS (
        SELECT 1
        FROM INSERTED i
        JOIN DELETED d ON i.OrderID = d.OrderID AND i.ProductID = d.ProductID
        JOIN Products p ON i.ProductID = p.ProductID
        WHERE p.UnitsInStock + d.Quantity - i.Quantity < 0
    )
    BEGIN
        RAISERROR('Yetersiz stok! Sipariş miktarı güncellenemez.', 16, 1);
        ROLLBACK TRANSACTION;
        RETURN;
    END;

    -- Stok farkını uygula (eski miktarı geri ekle, yenisini çıkar)
    UPDATE p
    SET p.UnitsInStock = p.UnitsInStock + d.Quantity - i.Quantity
    FROM Products p
    JOIN INSERTED i ON p.ProductID = i.ProductID
    JOIN DELETED d ON i.ProductID = d.ProductID;
END;

INSERT INTO Products (ProductName, SupplierID, CategoryID, QuantityPerUnit, UnitPrice, UnitsInStock)
VALUES ('Tea', NULL, 1, '12 boxes', 12.00, -5);  -- HATA BEKLENİR


SELECT * FROM Products

INSERT INTO [Order Details] (OrderID, ProductID, UnitPrice, Quantity, Discount)
VALUES (11077, 1, 18.00, 10, 0);  -- Fazla sipariş, stok yetmez

SELECT * FROM Orders 

ALTER TABLE Orders
ADD OrderSum MONEY NULL;

SELECT * FROM Orders

CREATE TRIGGER trg_UpdateOrderSum
ON [Order Details]
AFTER INSERT, UPDATE, DELETE
AS
BEGIN
    SET NOCOUNT ON;

    -- Etkilenen OrderID'leri yakala (hem INSERTED hem DELETED)
    DECLARE @AffectedOrders TABLE (OrderID INT);

    INSERT INTO @AffectedOrders (OrderID)
    SELECT DISTINCT OrderID FROM INSERTED
    UNION
    SELECT DISTINCT OrderID FROM DELETED;

    -- Her etkilenen siparişin toplamını güncelle:
    UPDATE o
    SET o.OrderSum = (
        SELECT SUM(od.UnitPrice * od.Quantity * (1 - od.Discount))
        FROM [Order Details] od
        WHERE od.OrderID = o.OrderID
    )
    FROM Orders o
    JOIN @AffectedOrders ao ON o.OrderID = ao.OrderID;
END;


INSERT INTO Orders (CustomerID, EmployeeID, OrderDate, RequiredDate, ShippedDate, ShipVia, Freight)
VALUES ('ALFKI', 1, GETDATE(), GETDATE(), GETDATE(), 1, 10.0);

SELECT * FROM Orders WHERE CustomerID='ALFKI'
INSERT INTO [Order Details] (OrderID, ProductID, UnitPrice, Quantity, Discount)
VALUES 
(11078, 1, 18.00, 5, 0),    -- 5 * 18 = 90
(11078, 2, 25.00, 3, 0.1);  -- 3 * 25 * 0.9 = 67.5

SELECT * FROM Orders WHERE CustomerID='ALFKI'


DECLARE @ProductID int;
DECLARE product_cursor CURSOR FOR
SELECT ProductID FROM Products;

OPEN product_cursor;
FETCH NEXT FROM product_cursor INTO @ProductID;

WHILE @@FETCH_STATUS = 0
BEGIN
   PRINT @ProductID;
   FETCH NEXT FROM product_cursor INTO @ProductID;
END;

CLOSE product_cursor;
DEALLOCATE product_cursor;


-- Cursor tanımlanır
DECLARE ProductCursor CURSOR FOR
SELECT ProductName FROM Products;

-- Değişken tanımlanır
DECLARE @ProductName NVARCHAR(40);

-- Cursor açılır
OPEN ProductCursor;

-- İlk satır çekilir
FETCH NEXT FROM ProductCursor INTO @ProductName;

-- Satır satır gezilir
WHILE @@FETCH_STATUS = 0
BEGIN
    PRINT 'Product: ' + @ProductName;

    -- Sonraki satır
    FETCH NEXT FROM ProductCursor INTO @ProductName;
END

-- Cursor kapatılır ve silinir
CLOSE ProductCursor;
DEALLOCATE ProductCursor;


--Birden  fazla alan ve şartlı kullanım

DECLARE ProductCursor CURSOR FOR
SELECT ProductID, ProductName, UnitsInStock FROM Products;

DECLARE @ProductID INT, @ProductName NVARCHAR(40), @UnitsInStock SMALLINT;

OPEN ProductCursor;
FETCH NEXT FROM ProductCursor INTO @ProductID, @ProductName, @UnitsInStock;

WHILE @@FETCH_STATUS = 0
BEGIN
    IF @UnitsInStock < 10
    BEGIN
        PRINT 'Low stock: ' + @ProductName;
    END

    FETCH NEXT FROM ProductCursor INTO @ProductID, @ProductName, @UnitsInStock;
END

CLOSE ProductCursor;
DEALLOCATE ProductCursor;


--Cursor Tipleri
--Tip | Açıklama | Performans
--STATIC | Sonuçları temp tabloda tutar | Yavaş, değişiklikleri görmez
--DYNAMIC | Canlı değişiklikleri görür | Yavaş olabilir
--FAST_FORWARD | Sadece ileri gider, hızlı | Genelde önerilir
--KEYSET | Primary key’leri tutar | Orta hız

-- Değişkenler ve Cursor tanımlanır
DECLARE OrderCursor CURSOR FAST_FORWARD FOR
SELECT OrderID FROM Orders;

DECLARE @OrderID INT;
DECLARE @OrderSum MONEY;

-- Cursor açılır
OPEN OrderCursor;

-- İlk satır alınır
FETCH NEXT FROM OrderCursor INTO @OrderID;

-- Satır satır dolaşılır
WHILE @@FETCH_STATUS = 0
BEGIN
    -- Bu siparişin toplam tutarını hesapla (Discount dikkate al!)
    SELECT @OrderSum = ISNULL(SUM(od.UnitPrice * od.Quantity * (1 - od.Discount)), 0)
    FROM [Order Details] od
    WHERE od.OrderID = @OrderID;

    -- Orders tablosundaki OrderSum alanını güncelle
    UPDATE Orders
    SET OrderSum = @OrderSum
    WHERE OrderID = @OrderID;

    -- Sonraki siparişi getir
    FETCH NEXT FROM OrderCursor INTO @OrderID;
END

-- Cursor kapatılır ve temizlenir
CLOSE OrderCursor;
DEALLOCATE OrderCursor;


SELECT * FROM Orders
--

UPDATE Orders
SET OrderSum = NULL;
SELECT * FROM Orders;

--CURSOR YERINE 
UPDATE o
SET o.OrderSum = ISNULL(od.Total, 0)
FROM Orders o
OUTER APPLY (
    SELECT SUM(od.UnitPrice * od.Quantity * (1 - od.Discount)) AS Total
    FROM [Order Details] od
    WHERE od.OrderID = o.OrderID
) od;


SELECT * FROM Orders;
UPDATE Orders
SET OrderSum = NULL
WHERE YEAR(OrderDate) = 1996;


UPDATE Orders
SET OrderSum = NULL
WHERE YEAR(OrderDate) = 1997;

SELECT * FROM Orders;

DECLARE OrderCursor CURSOR FAST_FORWARD FOR
SELECT OrderID FROM Orders WHERE YEAR(OrderDate) = 1996;

DECLARE @OrderID INT;
DECLARE @OrderSum MONEY;

OPEN OrderCursor;
FETCH NEXT FROM OrderCursor INTO @OrderID;

WHILE @@FETCH_STATUS = 0
BEGIN
    -- OrderSum hesapla (Discount dahil!)
    SELECT @OrderSum = ISNULL(SUM(od.UnitPrice * od.Quantity * (1 - od.Discount)), 0)
    FROM [Order Details] od
    WHERE od.OrderID = @OrderID;

    -- Güncelle
    UPDATE Orders
    SET OrderSum = @OrderSum
    WHERE OrderID = @OrderID;

    -- Sonraki sipariş
    FETCH NEXT FROM OrderCursor INTO @OrderID;
END

CLOSE OrderCursor;
DEALLOCATE OrderCursor;


SELECT * FROM Orders


UPDATE o
SET o.OrderSum = ISNULL(od.Total, 0)
FROM Orders o
OUTER APPLY (
    SELECT SUM(od.UnitPrice * od.Quantity * (1 - od.Discount)) AS Total
    FROM [Order Details] od
    WHERE od.OrderID = o.OrderID
) od
WHERE YEAR(o.OrderDate) = 1997;


SELECT * FROM Orders Where OrderSum is null 


--SELF JOIN Çalışan ve Müdürleri
SELECT * FROM Employees;

SELECT 
    e1.EmployeeID AS EmployeeID,
    CONCAT(e1.FirstName, ' ', e1.LastName) AS EmployeeName,
    e2.EmployeeID AS ManagerID,
    CONCAT(e2.FirstName, ' ', e2.LastName) AS ManagerName
FROM 
    Employees e1
LEFT JOIN 
    Employees e2 ON e1.ReportsTo = e2.EmployeeID
ORDER BY 
    e1.EmployeeID;


--SADECE Müdür olanlar
SELECT 
    e1.EmployeeID AS EmployeeID,
    CONCAT(e1.FirstName, ' ', e1.LastName) AS EmployeeName,
    e2.EmployeeID AS ManagerID,
    CONCAT(e2.FirstName, ' ', e2.LastName) AS ManagerName
FROM 
    Employees e1
INNER JOIN 
    Employees e2 ON e1.ReportsTo = e2.EmployeeID
ORDER BY 
    e1.EmployeeID;

--Bir müdüre bağlı çalışanlar

SELECT 
    e2.EmployeeID AS ManagerID,
    CONCAT(e2.FirstName, ' ', e2.LastName) AS ManagerName,
    COUNT(e1.EmployeeID) AS SubordinateCount
FROM 
    Employees e1
INNER JOIN 
    Employees e2 ON e1.ReportsTo = e2.EmployeeID
GROUP BY 
    e2.EmployeeID, e2.FirstName, e2.LastName
ORDER BY 
    SubordinateCount DESC;


--	CEO ve altında çalışanı olmayanlar
-- Employees e1 (EmployeeID)  -- ReportsTo --> Employees e2 (EmployeeID)
SELECT 
    e1.EmployeeID,
    CONCAT(e1.FirstName, ' ', e1.LastName) AS EmployeeName,
    e1.ReportsTo
FROM 
    Employees e1
LEFT JOIN 
    Employees e2 ON e1.EmployeeID = e2.ReportsTo
WHERE 
    e2.EmployeeID IS NULL;

--INNER JOIN

--Müşteri ve Siparişleri (Kesişim)

SELECT 
	c.CustomerID,
	c.CompanyName as CustomerName 
FROM
	Customers c;

SELECT
	o.CustomerID,
	o.OrderID,
	o.OrderDate
FROM
	Orders o;


SELECT 
	c.CustomerID,
	c.CompanyName as CustomerName,
	o.OrderID,
	o.OrderDate,
	o.OrderSum
FROM
	Customers c
INNER JOIN Orders o ON c.CustomerID=o.CustomerID
ORDER BY c.CustomerID;


---LEFT JOIN / Tüm müşteriler  ve varsa Siparişleri

SELECT 
	c.CustomerID,
	c.CompanyName as CustomerName,
	o.OrderID,
	o.OrderDate,
	o.OrderSum
FROM
	Customers c
LEFT JOIN Orders o ON c.CustomerID=o.CustomerID
ORDER BY
	c.CustomerID

---LEFT JOIN / Tüm müşteriler olup hiç sipariş vermemiş
SELECT 
	c.CustomerID,
	c.CompanyName as CustomerName,
	o.OrderID,
	o.OrderDate,
	o.OrderSum
FROM
	Customers c
LEFT JOIN Orders o ON c.CustomerID=o.CustomerID
WHERE o.OrderID IS NULL
ORDER BY
	c.CustomerID

--RIGHT JOIN - Tüm Siparişler ve varsa Müşterileri
SELECT
	c.CustomerID,
    c.CompanyName AS CustomerName,
    o.OrderID,
    o.OrderDate,
    o.OrderSum
FROM 
    Orders o
RIGHT JOIN 
    Customers c ON o.CustomerID = c.CustomerID
ORDER BY 
    o.OrderID;

---FULL JOIN Örneği (Tüm Müşteriler ve Tüm Siparişler)

SELECT 
    c.CustomerID,
    c.CompanyName AS CustomerName,
    o.OrderID,
    o.OrderDate,
	o.OrderSum
FROM 
    Customers c
FULL OUTER JOIN 
    Orders o ON c.CustomerID = o.CustomerID
ORDER BY 
    CustomerName;

-- CROSS JOIN Kartezyen çarpım

SELECT 
	p.ProductName,
	c.CategoryName
FROM
	Products p
CROSS JOIN
	Categories c 


--JOIN Türü | Açıklama
--INNER JOIN | Her iki tabloda eşleşen kayıtları getirir
--LEFT (OUTER) JOIN | Sol tablodaki tüm kayıtları getirir, eşleşen sağ tablo verisi varsa ekler
--RIGHT (OUTER) JOIN | Sağ tablodaki tüm kayıtları getirir, eşleşen sol tablo verisi varsa ekler
--FULL (OUTER) JOIN | Her iki tablodaki tüm kayıtları getirir, eşleşmeyenlerde NULL gösterir
--CROSS JOIN | Kartezyen çarpım, her satırı diğer tablo ile çarpar
--SELF JOIN | Tabloyu kendiyle join eder

--Birden çok tablo Müşteri Sipariş ve Çalışan

SELECT 
    o.OrderID,
    o.OrderDate,
	o.OrderSum,
    c.CompanyName AS CustomerName,
    e.FirstName + ' ' + e.LastName AS EmployeeName
FROM 
    Orders o
INNER JOIN 
    Customers c ON o.CustomerID = c.CustomerID
INNER JOIN 
    Employees e ON o.EmployeeID = e.EmployeeID
ORDER BY 
    o.OrderID;

---Müşteri Çalışan Ürün arasındaki ilişiki

SELECT * FROM Customers;
SELECT * FROM Products;
SELECT * FROM Employees;

SELECT * FROM Orders; --Müşteri ve Çalışan burda ama ürün yok
SELECT * FROM [Order Details]; -- Product bilgisi burada 

SELECT 
    c.CustomerID,
    c.CompanyName AS CustomerName,
    CONCAT(e.FirstName, ' ', e.LastName) AS EmployeeName,
    o.OrderID,
    o.OrderDate,
    p.ProductName,
    od.Quantity,
    od.UnitPrice,
    (od.Quantity * od.UnitPrice) AS TotalPrice
FROM 
    Customers c
INNER JOIN 
    Orders o ON c.CustomerID = o.CustomerID
INNER JOIN 
    Employees e ON o.EmployeeID = e.EmployeeID
INNER JOIN 
    [Order Details] od ON o.OrderID = od.OrderID
INNER JOIN 
    Products p ON od.ProductID = p.ProductID
ORDER BY 
    o.OrderID;


--Her Müşteri, Her Ürün, Hangi Çalışan Satmış ve Toplam Satış Tutarı (GROUP BY + SUM):

SELECT 
    c.CustomerID,
    c.CompanyName AS CustomerName,
    CONCAT(e.FirstName, ' ', e.LastName) AS EmployeeName,
    p.ProductName,
    SUM(od.Quantity) AS TotalQuantitySold,
    SUM(od.Quantity * od.UnitPrice) AS TotalSales
FROM 
    Customers c
INNER JOIN 
    Orders o ON c.CustomerID = o.CustomerID
INNER JOIN 
    Employees e ON o.EmployeeID = e.EmployeeID
INNER JOIN 
    [Order Details] od ON o.OrderID = od.OrderID
INNER JOIN 
    Products p ON od.ProductID = p.ProductID
GROUP BY 
    c.CustomerID, c.CompanyName, e.EmployeeID, e.FirstName, e.LastName, p.ProductName
ORDER BY 
    TotalSales DESC;
--Sadece 1997 Yılındaki Satışlar İçin (WHERE ile Yıl Filtreleme)
SELECT 
    c.CustomerID,
    c.CompanyName AS CustomerName,
    CONCAT(e.FirstName, ' ', e.LastName) AS EmployeeName,
    p.ProductName,
    SUM(od.Quantity) AS TotalQuantitySold,
    SUM(od.Quantity * od.UnitPrice) AS TotalSales
FROM 
    Customers c
INNER JOIN 
    Orders o ON c.CustomerID = o.CustomerID
INNER JOIN 
    Employees e ON o.EmployeeID = e.EmployeeID
INNER JOIN 
    [Order Details] od ON o.OrderID = od.OrderID
INNER JOIN 
    Products p ON od.ProductID = p.ProductID
WHERE 
    YEAR(o.OrderDate) = 1997
GROUP BY 
    c.CustomerID, c.CompanyName, e.EmployeeID, e.FirstName, e.LastName, p.ProductName
ORDER BY 
    TotalSales DESC;

--- 1997 yılı için 100K üzerinde satış yapanlar

SELECT 
    c.CustomerID,
    c.CompanyName AS CustomerName,
    CONCAT(e.FirstName, ' ', e.LastName) AS EmployeeName,
    p.ProductName,
    SUM(od.Quantity) AS TotalQuantitySold,
    SUM(od.Quantity * od.UnitPrice) AS TotalSales
FROM 
    Customers c
INNER JOIN 
    Orders o ON c.CustomerID = o.CustomerID
INNER JOIN 
    Employees e ON o.EmployeeID = e.EmployeeID
INNER JOIN 
    [Order Details] od ON o.OrderID = od.OrderID
INNER JOIN 
    Products p ON od.ProductID = p.ProductID
WHERE 
    YEAR(o.OrderDate) = 1997
GROUP BY 
    c.CustomerID, c.CompanyName, e.EmployeeID, e.FirstName, e.LastName, p.ProductName
HAVING 
    SUM(od.Quantity * od.UnitPrice) > 7500  -- 7500 üstü olanları getirir
ORDER BY 
    TotalSales DESC;

-- Yıl seçilebilir olsun

DECLARE @SelectedYear INT = 1998;  -- MS SQL için

SELECT 
    c.CustomerID,
    c.CompanyName AS CustomerName,
    CONCAT(e.FirstName, ' ', e.LastName) AS EmployeeName,
    p.ProductName,
    SUM(od.Quantity) AS TotalQuantitySold,
    SUM(od.Quantity * od.UnitPrice) AS TotalSales
FROM 
    Customers c
INNER JOIN 
    Orders o ON c.CustomerID = o.CustomerID
INNER JOIN 
    Employees e ON o.EmployeeID = e.EmployeeID
INNER JOIN 
    [Order Details] od ON o.OrderID = od.OrderID
INNER JOIN 
    Products p ON od.ProductID = p.ProductID
WHERE 
    YEAR(o.OrderDate) = @SelectedYear
GROUP BY 
    c.CustomerID, c.CompanyName, e.EmployeeID, e.FirstName, e.LastName, p.ProductName
HAVING 
    SUM(od.Quantity * od.UnitPrice) > 7500
ORDER BY 
    TotalSales DESC;

---Aynı sorguda ilk 3
	
DECLARE @SelectedYear INT = 1998;  -- MS SQL için

SELECT TOP 3
    c.CustomerID,
    c.CompanyName AS CustomerName,
    CONCAT(e.FirstName, ' ', e.LastName) AS EmployeeName,
    p.ProductName,
    SUM(od.Quantity) AS TotalQuantitySold,
    SUM(od.Quantity * od.UnitPrice) AS TotalSales
FROM 
    Customers c
INNER JOIN 
    Orders o ON c.CustomerID = o.CustomerID
INNER JOIN 
    Employees e ON o.EmployeeID = e.EmployeeID
INNER JOIN 
    [Order Details] od ON o.OrderID = od.OrderID
INNER JOIN 
    Products p ON od.ProductID = p.ProductID
WHERE 
    YEAR(o.OrderDate) = @SelectedYear
GROUP BY 
    c.CustomerID, c.CompanyName, e.EmployeeID, e.FirstName, e.LastName, p.ProductName
HAVING 
    SUM(od.Quantity * od.UnitPrice) > 7500
ORDER BY 
    TotalSales DESC;

---QUERY DESIGNER
DECLARE @SelectedYear INT = 1998;  -- MS SQL için
SELECT c.CustomerID, c.CompanyName AS CustomerName,  CONCAT(e.FirstName, ' ', e.LastName) AS EmployeeName, p.ProductName, SUM(od.Quantity) AS TotalQuantitySold, SUM(od.Quantity * od.UnitPrice) AS TotalSales, p.SupplierID, 
                  Suppliers.CompanyName, Categories.CategoryID, Categories.CategoryName
FROM     Customers AS c INNER JOIN
                  Orders AS o ON c.CustomerID = o.CustomerID INNER JOIN
                  Employees AS e ON o.EmployeeID = e.EmployeeID INNER JOIN
                  [Order Details] AS od ON o.OrderID = od.OrderID INNER JOIN
                  Products AS p ON od.ProductID = p.ProductID INNER JOIN
                  Suppliers ON p.SupplierID = Suppliers.SupplierID INNER JOIN
                  Categories ON p.CategoryID = Categories.CategoryID
WHERE  (YEAR(o.OrderDate) = @SelectedYear)
GROUP BY c.CustomerID, c.CompanyName, e.EmployeeID, e.FirstName, e.LastName, p.ProductName, p.SupplierID, Suppliers.CompanyName, Categories.CategoryID, Categories.CategoryName
HAVING (SUM(od.Quantity * od.UnitPrice) > 7500)
ORDER BY TotalSales DESC

---SUB QUERY Bir sorgunun içinde başka bir sorgunun olması durumu
--SELECT, FROM, WHERE, HAVING gibi yerlerde kullanılabilir.
--Kullanım Yeri | Açıklama
--WHERE içinde | Koşul filtresi için
--FROM içinde | Derived Table (geçici tablo gibi)
--SELECT içinde | Tek değer döndüren alt sorgu
--EXISTS / IN / NOT IN | Liste kontrolü için

--EN ÇOK Sipariş veren müşteri
SELECT 
    CustomerID, 
    COUNT(OrderID) AS OrderCount
FROM 
    Orders
GROUP BY 
    CustomerID
HAVING 
    COUNT(OrderID) = (
        SELECT MAX(OrderCount)
        FROM (
            SELECT 
                CustomerID, 
                COUNT(OrderID) AS OrderCount
            FROM 
                Orders
            GROUP BY 
                CustomerID
        ) AS Subquery
    );

---WHERE
--En pahalı ürün sub-query 
SELECT 
    ProductID, 
    ProductName, 
    UnitPrice
FROM 
    Products
WHERE 
    UnitPrice = (
        SELECT MAX(UnitPrice) 
        FROM Products
    );


--Sipariş vermiş müşteriler

SELECT 
    CustomerID, 
    CompanyName
FROM 
    Customers
WHERE 
    CustomerID NOT IN (
        SELECT DISTINCT CustomerID 
        FROM Orders
    );

--Sipariş vermemiş müşteriler
SELECT 
    CustomerID, 
    CompanyName
FROM 
    Customers
WHERE 
    CustomerID NOT IN (
        SELECT DISTINCT CustomerID 
        FROM Orders
    );


--SUBQuery ile ortalama fiya 
SELECT 
    ProductID, 
    ProductName, 
    UnitPrice,
    (SELECT AVG(UnitPrice) FROM Products) AS AveragePrice
FROM 
    Products
WHERE 
    UnitPrice > (
        SELECT AVG(UnitPrice) 
        FROM Products
    );

--FROM İçinde SUBQUERY (Derived Table Kullanımı)

SELECT 
    CategoryName, 
    AveragePrice
FROM 
    (
        SELECT 
            c.CategoryName, 
            AVG(p.UnitPrice) AS AveragePrice
        FROM 
            Categories c
        INNER JOIN 
            Products p ON c.CategoryID = p.CategoryID
        GROUP BY 
            c.CategoryName
    ) AS CategoryAverages
ORDER BY 
    AveragePrice DESC;

---EXIST ile sipariş vermiş müşteri
SELECT 
    CustomerID, 
    CompanyName
FROM 
    Customers c
WHERE 
    EXISTS (
        SELECT 1 
        FROM Orders o 
        WHERE o.CustomerID = c.CustomerID
    );
---En fazla siprariş vermiş müşteri

SELECT 
    CustomerID, 
    COUNT(OrderID) AS OrderCount
FROM 
    Orders
GROUP BY 
    CustomerID
HAVING 
    COUNT(OrderID) = (
        SELECT MAX(OrderCount)
        FROM (
            SELECT 
                CustomerID, 
                COUNT(OrderID) AS OrderCount
            FROM 
                Orders
            GROUP BY 
                CustomerID
        ) AS Subquery
    );
--Bağımlı alt sorgu / Kendi kategorisindeki ortalama fiyatın üstündeki ürünleri getirir (kategori bazlı).

SELECT 
    p.ProductID, 
    p.ProductName, 
    p.UnitPrice
FROM 
    Products p
WHERE 
    p.UnitPrice > (
        SELECT 
            AVG(p2.UnitPrice) 
        FROM 
            Products p2 
        WHERE 
            p2.CategoryID = p.CategoryID
    );

--Subquery Tipi | Kullanıldığı Yer | Amaç
--Scalar Subquery | SELECT içinde | Tek değer döner
--Inline View | FROM içinde | Derived Table (geçici tablo)
--WHERE Subquery | WHERE, IN, NOT IN, EXISTS | Liste veya koşul kontrolü
--Correlated Subquery | Satır satır bağlı alt sorgu | Bağımlı alt sorgular