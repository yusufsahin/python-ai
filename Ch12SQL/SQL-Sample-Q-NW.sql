SELECT * FROM Customers;

SELECT DISTINCT(City) FROM Customers;

SELECT COUNT(*) FROM Customers;

SELECT COUNT(CustomerID) FROM Customers;

SELECT COUNT(DISTINCT(City)) FROM Customers;

SELECT CustomerID, CompanyName, ContactName, ContactTitle
FROM     Customers;

SELECT CategoryID AS ID, CategoryName as Name, Description
FROM     Categories;

SELECT DISTINCT(Country) FROM Customers;
SELECT COUNT(DISTINCT(Country)) FROM Customers;

SELECT * FROM Customers WHERE Country ='Argentina'

SELECT COUNT(*) FROM Customers WHERE Country ='Argentina'

SELECT * FROM Customers WHERE Country ='UK' AND City='Cowes'
SELECT * FROM Customers WHERE Country ='UK' AND City='London'

SELECT * FROM Customers WHERE Country ='UK' AND Country='Germany' --Kesişim olduğu için boş verir

SELECT * FROM Customers WHERE Country ='UK' OR Country='Germany' ORDER BY Country,City

SELECT * FROM Customers WHERE Country IN ('UK','Germany') ORDER BY Country,City

SELECT * FROM Customers WHERE  Phone IS NULL ORDER BY Country,City

SELECT * FROM Customers WHERE Country IN ('UK','Germany') AND Fax IS NOT NULL ORDER BY Country,City --ALMANYA veya UK 'de Fax çekilebilecek müşteriler 

SELECT * FROM Customers WHERE Fax IS NULL ORDER BY Country,City --Fax 'ı olmayan müşteriler

--En pahalı 5 ürün

SELECT Top(5) ProductName , UnitPrice FROM Products ORDER BY UnitPrice DESC

--En ucuz 5 ürün

SELECT Top(5) ProductName , UnitPrice FROM Products ORDER BY UnitPrice 

SELECT OrderID, ProductID, UnitPrice, Quantity, Discount
FROM     [Order Details]

SELECT OrderID,SUM(UnitPrice * Quantity) as TotalAmount FROM [Order Details] GROUP BY OrderID

SELECT OrderID,SUM(UnitPrice * Quantity *(1- Discount)) as DiscountedTotal
FROM     [Order Details] GROUP BY OrderID ORDER BY OrderID

-- 100 liralık ürün 75 liraya sattım.
--Normal fiyat oranım :75/100->Normal fiyat * (1-0.25)(indirim oranı))-> İndirimli Satış fiyatı


--Ne kadar indirim yapılmış

SELECT OrderID ,
	SUM(UnitPrice * Quantity) as OriginalTotal,
	SUM(UnitPrice * Quantity *(1- Discount)) as DiscountedTotal, 
	SUM(UnitPrice * Quantity) - SUM(UnitPrice * Quantity *(1- Discount)) As TotalDiscount
FROM [Order Details] GROUP BY OrderID ORDER BY OrderID

--Ürünlerin ortalama fiyatı

SELECT * FROM Products
SELECT AVG(UnitPrice) as OrtalamaFiyat FROM Products;
SELECT SUM(UnitPrice) / COUNT(*) as OrtalamaFiyat From Products;

--MAX ve Min

SELECT MIN(UnitPrice) AS CheapestProduct, MAX(UnitPrice) AS MostExpensiveProduct FROM Products;

SELECT ProductID,ProductName,UnitPrice FROM Products WHERE UnitPrice=(SELECT MIN(UnitPrice) FROM Products);

SELECT ProductID,ProductName,UnitPrice FROM Products WHERE UnitPrice=(SELECT MAX(UnitPrice) FROM Products);

--bunları tek tabloda gösterelim

SELECT 'Cheapest' as PriceType,ProductID,ProductName,UnitPrice FROM Products WHERE UnitPrice=(SELECT MIN(UnitPrice) FROM Products)
UNION
SELECT 'MostExpensive' as PriceType,ProductID,ProductName,UnitPrice FROM Products WHERE UnitPrice=(SELECT MAX(UnitPrice) FROM Products);

--Ortama Fiyat üstü ürünler

-- Koşul Ortalama fiyat üstü önce koşulu yaz

SELECT AVG(UnitPrice) FROM Products

SELECT ProductName,UnitPrice FROM Products WHERE UnitPrice > (SELECT AVG(UnitPrice) FROM Products) ORDER BY UnitPrice DESC

--Ortama Fiyat altı ürünler
SELECT ProductName,UnitPrice FROM Products WHERE UnitPrice <(SELECT AVG(UnitPrice) FROM Products) ORDER BY UnitPrice DESC

-- Category Bazında Ortalama Fiyat 

SELECT 
	Categories.CategoryName, 
	AVG(Products.UnitPrice) as CategoryAVGPrice
FROM Products 
	JOIN Categories ON Products.CategoryID=Categories.CategoryID 
GROUP BY Categories.CategoryName

--Stokta kaç ürün var
SELECT 
    SUM(UnitsInStock) AS TotalStock
FROM 
    Products
WHERE 
    Discontinued = 0;


-- Kategoriye göre en pahalı ürün

SELECT 
    C.CategoryName,
    P.ProductName,
    P.UnitPrice
FROM 
    Products P
JOIN 
    Categories C ON P.CategoryID = C.CategoryID
WHERE 
    P.UnitPrice = (
        SELECT MAX(P2.UnitPrice)
        FROM Products P2
        WHERE P2.CategoryID = P.CategoryID
    )
ORDER BY 
    C.CategoryName;



--- STOK değeri

SELECT 
    SUM(UnitPrice * UnitsInStock) AS TotalStockValue
FROM 
    Products;


-- Yıllık Enflasyon %65
-- Her ay ort 65/12= %5.5

-- Bu ay 100 liraya sattığım ürün gelecek tahmini fiyat-->100*1.055 =105.5

SELECT ROUND(100 * 1.055, 2) AS RoundedResult;

SELECT ProductName,UnitPrice as CurrentMountUP, ROUND(UnitPrice *1.055,2) as NextMountUP FROM Products

SELECT 
    ProductName,
    UnitPrice AS CurrentMonthUP,
    ROUND(UnitPrice * 1.055, 2) AS NextMonthUP,
    ROUND(UnitPrice * POWER(1.055, 6), 2) AS SixMonthsLaterUP
FROM 
    Products;

---SixMonthsLaterUP: 6 ay sonrası için %5.5 bileşik artışla tahmini fiyat
SELECT
    ProductName,
    UnitPrice AS CurrentMonthUP,
    ROUND(UnitPrice * POWER(1.055, 12), 2) AS OneYearLaterUP,
	ROUND(UnitPrice * POWER(1.055, 12), 2)/UnitPrice AS RateOfIncrease,
	ROUND(((UnitPrice * POWER(1.055, 12)) - UnitPrice) / UnitPrice * 100, 2) AS PercentageIncrease
FROM 
    Products;

---OneYearLaterUP: 1 yıl sonrası için %5.5 bileşik artışla tahmini fiyat, 
--CurrentMonthUP	Mevcut ürün fiyatı
--OneYearLaterUP	12 ay sonra %5.5 bileşik zamla tahmini fiyat
--RateOfIncrease	Fiyat kaç katına çıktı (örneğin 1.75 = %75 artış)
--PercentageIncrease	Yüzde olarak artış (örneğin 75.00 = %75)