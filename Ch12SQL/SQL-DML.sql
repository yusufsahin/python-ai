Select * From Products;

INSERT INTO Products (ProductName,SupplierID,CategoryID,QuantityPerUnit,UnitPrice,UnitsInStock,UnitsOnOrder,ReorderLevel,Discontinued)
VALUES('Organic Jasmin Tea',1,2,'20 bags',12.50,75,20,10,0);

INSERT INTO Products (ProductName,SupplierID,CategoryID,QuantityPerUnit,UnitPrice,UnitsInStock,UnitsOnOrder,ReorderLevel,Discontinued)
VALUES('Organic Jasmin Tea',3000,3500,'20 bags',12.50,75,20,10,0); --Çalışmaz Foreign Key Böyle bir değeri yok 3000 ve 35000
 
SELECT * FROM Categories;
SELECT * FROM Suppliers;

INSERT INTO Products (ProductID,SupplierID,CategoryID,QuantityPerUnit,UnitPrice,UnitsInStock,UnitsOnOrder,ReorderLevel,Discontinued)
VALUES(90,'Organic Jasmin Tea',3000,3500,'20 bags',12.50,75,20,10,0); --Çalışmaz Primary Key Bu örneke Identity 1 den başlayıp 1 er 1 er artıyor Primary ancak ms server tarafında atanır 



INSERT INTO Customers (CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode, Country, Phone)
VALUES ( 'Organic Textures Ltd.', 'Elena Marquez', 'Purchasing Manager', '5 Greenway Blvd', 'Barcelona', NULL, '08001', 'Spain', '+34-93-5551234'); ---Bu kod çalışmaz Primary Key in CLient/istemci tarafında  verilmesini istiyor

INSERT INTO Customers (CustomerID, CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode, Country, Phone)
VALUES ('ORGTX', 'Organic Textures Ltd.', 'Elena Marquez', 'Purchasing Manager', '5 Greenway Blvd', 'Barcelona', NULL, '08001', 'Spain', '+34-93-5551234');

SELECT * FROM Customers WHERE CustomerID='ORGTX'

INSERT INTO Suppliers (CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode, Country, Phone)
VALUES ('Nordic Harvest Co.', 'Anders Bjorn', 'Logistics Coordinator', '78 Fjord Lane', 'Oslo', NULL, '0150', 'Norway', '+47-22-445566'); --Yine Identity identity olduğu için primary key ms server tarafından atanır


Select * From Suppliers;

--Multi Row Insert

INSERT INTO Suppliers (
    CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode, Country, Phone
)
VALUES 
('Alpine Naturals', 'Greta Meier', 'Purchasing Agent', '45 Summit Street', 'Zurich', NULL, '8001', 'Switzerland', '+41-44-1234567'),
('Baltic Produce Ltd.', 'Kaisa Lehto', 'Procurement Lead', '9 Seaside Road', 'Helsinki', NULL, '00100', 'Finland', '+358-9-5554443'),
('Danube Agro Foods', 'István Nagy', 'Sourcing Manager', '12 Riverbank Ave', 'Budapest', NULL, '1051', 'Hungary', '+36-1-2345678'),
('Mediterranean Essentials', 'Sophia Costa', 'Head of Logistics', '88 Olive Way', 'Athens', NULL, '10558', 'Greece', '+30-21-9988776');

Select * From Suppliers;


---Bir başka tablodan yeni bir tablo oluşturarak insert yapma

--Örneğin USA deki müştelerimi başka bi bir tabloya yazmak istiyorum 


SELECT * INTO USA_Customers FROM Customers WHERE Country ='USA'

SELECT * FROM USA_Customers;

SELECT * INTO Supplier1_Products FROM Products Where SupplierID=1

Select * FROM Supplier1_Products


---Tablo daha önceden oluştulmuş olmalı
INSERT INTO USA_Customers (
    CustomerID, CompanyName, ContactName, ContactTitle, Address,
    City, Region, PostalCode, Country, Phone, Fax
)
SELECT 
    CustomerID, CompanyName, ContactName, ContactTitle, Address,
    City, Region, PostalCode, Country, Phone, Fax
FROM Customers
WHERE Country = 'USA';

-- OUTPUT ile yeni eklenen kayıtları göster
INSERT INTO Suppliers (
    CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode, Country, Phone
)
OUTPUT inserted.SupplierID, inserted.CompanyName
VALUES 
('Green Valley Ltd.', 'Thomas Eriksen', 'Warehouse Lead', '23 Greenhill Blvd', 'Copenhagen', NULL, '2100', 'Denmark', '+45-32-123456');



--Id yi görmek isterseniz 
DECLARE @NewID INT;

INSERT INTO Suppliers (
    CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode, Country, Phone
)
VALUES (
    'Arctic Foods Ltd.', 'Helena Nord', 'Procurement Lead',
    '12 Icefield Rd', 'Reykjavik', NULL, '101', 'Iceland', '+354-555-1234'
);

SET @NewID = SCOPE_IDENTITY();

SELECT @NewID AS InsertedSupplierID;

SELECT * FROM Products

--Id 1 Chai nin fiyatı artık 20 olsun /yani güncelleecek

UPDATE Products SET UnitPrice=20.05 WHERE ProductID=1;

SELECT * FROM Products WHERE ProductID=1;


SELECT * FROM Products WHERE ProductID=2;

UPDATE Products SET UnitsInStock=20.05 WHERE ProductID=2;  --20 olarak aldı ,data type /column önemli

SELECT * FROM Products WHERE CategoryID=3

--Category 3 deki ürünlerimin fiyatını 3 dolar artırmak istiyorum

UPDATE Products SET UnitPrice=UnitPrice+3 WHERE CategoryID=3;

--Category 4 deki ürünlerime %25 zam yapmak istiyorum

SELECT * FROM Products WHERE CategoryID=4

--100 %25 lira zam yaptığımda 125 lira oran 1.25

UPDATE Products SET UnitPrice=UnitPrice* 1.25 WHERE CategoryID=4;


SELECT * FROM Products WHERE CategoryID=4


---Soru ABD den gelen ürünlere %75 zam yapmak


SELECT p.ProductID,p.ProductName,p.UnitPrice,s.Country FROM Products p JOIN Suppliers s ON p.SupplierID=s.SupplierID WHERE s.Country='USA'

UPDATE p SET p.UnitPrice=p.UnitPrice *1.75 FROM Products p JOIN Suppliers s ON p.SupplierID=s.SupplierID WHERE s.Country='USA'

---Soru ABD den gelen ürünlere %85 indirim yapmak

---100 %85 ->15->0.15

UPDATE p SET p.UnitPrice=p.UnitPrice *0.15 FROM Products p JOIN Suppliers s ON p.SupplierID=s.SupplierID WHERE s.Country='USA'


SELECT p.ProductID,p.ProductName,p.UnitPrice,s.Country FROM Products p JOIN Suppliers s ON p.SupplierID=s.SupplierID WHERE s.Country='USA'

SELECT * FROM USA_Customers


DELETE FROM USA_Customers WHERE CustomerID ='WHITC' --Siler 

SELECT * FROM USA_Customers WHERE CustomerID ='WHITC' -- Boş döner

DELETE FROM Products; -- Silemedi Bir tabloda Foreing Key 'i varsa MS SQL veri tutarlılığı açısından sildirmez Order Details ta foreing key

---DELETE Output kullanmak ,silenenleri gösterir

DELETE FROM USA_Customers OUTPUT DELETED.CustomerID,DELETED.CompanyName WHERE CustomerID IN ('WHITC','THECR','SPLIR') 


---UPSERT / Bir kayıt varsa güncellesin  yoksa eklesin

MERGE INTO Customers AS Target
USING (VALUES
    ('CSTM1', 'New Horizons Ltd.', 'Selina Brand', 'Sales Manager', 'Bonn', 'Germany', '+49-30-555233'),
    ('CSTM2', 'Harvest Foods', 'Daniel Frei', 'Director', 'Zurich', 'Switzerland', '+41-44-732921'),
	('CSTM3', 'Harman Ltd.Sti.', 'Ahmet Yilmaz', 'Director', 'Istanbul', 'Turkiye', '+90-212-3476524')
) AS Source (CustomerID, CompanyName, ContactName, ContactTitle, City, Country, Phone)
ON Target.CustomerID = Source.CustomerID

WHEN MATCHED THEN
    UPDATE SET 
        Target.CompanyName = Source.CompanyName,
        Target.ContactName = Source.ContactName,
        Target.ContactTitle = Source.ContactTitle,
        Target.City = Source.City,
        Target.Country = Source.Country,
        Target.Phone = Source.Phone

WHEN NOT MATCHED THEN
    INSERT (CustomerID, CompanyName, ContactName, ContactTitle, City, Country, Phone)
    VALUES (Source.CustomerID, Source.CompanyName, Source.ContactName, Source.ContactTitle, Source.City, Source.Country, Source.Phone);

SELECT * FROM Customers WHERE CustomerID IN ('CSTM1','CSTM2','CSTM3');


---VİEW Kendileri kendileri tablo değil ama tablo gibi davranır -Sanal Tablodur

CREATE VIEW View_Customers_USA AS
SELECT * FROM Customers WHERE Country='USA';


SELECT * FROM View_Customers_USA;



INSERT INTO View_Customers_USA (CustomerID, CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode, Country, Phone)
VALUES ('HELTY', 'Healty Foods Ltd.', 'John Doe', 'Sales Manager', 'Silicon Hill Blvd', 'Texas', NULL, '45001', 'USA', '+1-800-5951236');

SELECT * FROM Customers WHERE Country='USA';

UPDATE View_Customers_USA SET ContactName='Jane Doe' WHERE CustomerID='HELTY';

SELECT * FROM Customers WHERE CustomerID='HELTY'

---Tedarikçilerin ürün listesi

CREATE VIEW View_Supplier_Products AS
SELECT 
    s.CompanyName AS Supplier,
    p.ProductName,
    p.UnitPrice,
    p.UnitsInStock
FROM Suppliers s
JOIN Products p ON s.SupplierID = p.SupplierID;

SELECT * FROM View_Supplier_Products


CREATE VIEW View_Order_Summary AS
SELECT 
    o.OrderID,
    o.CustomerID,
    c.CompanyName AS CustomerName,
    o.OrderDate,
    SUM(od.UnitPrice * od.Quantity) AS TotalAmount
FROM Orders o
JOIN [Order Details] od ON o.OrderID = od.OrderID
JOIN Customers c ON o.CustomerID = c.CustomerID
GROUP BY o.OrderID, o.CustomerID, c.CompanyName, o.OrderDate;


SELECT * FROM View_Order_Summary

SELECT 
    c.CustomerID,
    c.CompanyName AS CustomerName,
    SUM(od.UnitPrice * od.Quantity) AS TotalRevenue
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
JOIN [Order Details] od ON o.OrderID = od.OrderID
GROUP BY c.CustomerID, c.CompanyName
ORDER BY TotalRevenue DESC;

CREATE VIEW View_Customer_Revenue AS
SELECT 
    c.CustomerID,
    c.CompanyName AS CustomerName,
    SUM(od.UnitPrice * od.Quantity) AS TotalRevenue
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
JOIN [Order Details] od ON o.OrderID = od.OrderID
GROUP BY c.CustomerID, c.CompanyName;

select * from View_Customer_Revenue

SELECT * FROM View_Customer_Revenue WHERE TotalRevenue > 10000;

CREATE VIEW View_Annual_Customer_Revenue AS
SELECT
    c.CustomerID,
    c.CompanyName AS CustomerName,
    YEAR(o.OrderDate) AS OrderYear,
    SUM(od.UnitPrice * od.Quantity) AS TotalRevenue
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
JOIN [Order Details] od ON o.OrderID = od.OrderID
GROUP BY c.CustomerID, c.CompanyName, YEAR(o.OrderDate);


select * from View_Annual_Customer_Revenue order by CustomerID,OrderYear

CREATE VIEW View_Country_Revenue AS
SELECT
    c.Country,
    SUM(od.UnitPrice * od.Quantity) AS TotalRevenue
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
JOIN [Order Details] od ON o.OrderID = od.OrderID
GROUP BY c.Country;

select * from View_Country_Revenue
--Aşağıdaki özellikleri taşıyan View 'lere insert update delete yapılabilir 
--GROUP BY, DISTINCT, UNION, JOIN, TOP	Olmamalı
--Sadece tek tabloya dayalı olmalı	Örneğin: SELECT * FROM Customers
--VIEW'deki tüm alanlar orijinal tablo ile doğrudan eşleşmeli	