SELECT MIN(UnitPrice) AS EnUcuzFiyat
FROM Products;

SELECT MAX(UnitPrice) AS EnPahaliFiyat
FROM Products;

SELECT COUNT(*) AS ToplamUrunSayisi
FROM Products;

SELECT COUNT(UnitsInStock) AS StoktaOlanUrunSayisi
FROM Products; --Null olan sütunlarda sadece NULL olmayanlar sayılacaksa

SELECT AVG(UnitPrice) AS OrtalamaFiyat
FROM Products;

SELECT SUM(UnitsInStock) AS ToplamStok
FROM Products

SELECT QuantityPerUnit,SUM(UnitsInStock) AS ToplamStok
FROM Products GROUP BY QuantityPerUnit
UNION
SELECT 'Total',SUM(UnitsInStock) from Products

--Müşteri adının karakter uzunluğu

SELECT CustomerID, ContactName, LEN(ContactName) AS AdUzunlugu
FROM Customers;


SELECT ContactName, LEFT(ContactName, 3) AS Ilk3Harf
FROM Customers;

SELECT ContactName, RIGHT(ContactName, 4) AS Son4Harf
FROM Customers;

SELECT ContactName, City, CONCAT(ContactName, ' - ', City) AS AdSehir
FROM Customers;

SELECT ContactName, City, CONCAT(ContactName, ' , ', CompanyName) AS AdSehir
FROM Customers;

SELECT ContactName + ' - ' + City AS AdSehir
FROM Customers;

SELECT ContactName, LOWER(ContactName) AS KucukHarfAd
FROM Customers;

SELECT ContactName, UPPER(ContactName) AS BuyukHarfAd
FROM Customers;

SELECT '   John Doe   ' AS Orijinal,
       TRIM('   John Doe   ') AS Temizlenmis;



SELECT LTRIM(RTRIM('   John Doe   ')) AS Temizlenmis; -- Once sağı sonra solu temizler-->TRIM() gibi çalışırSELECT ContactName

SELECT ContactName FROM Customers
WHERE LEN(ContactName) < 10;


--GROUP BY, aynı değerlere sahip satırları tek bir grup altında toplar. Genellikle toplama fonksiyonlarıyla (SUM, COUNT, AVG vs.) birlikte kullanılır.

SELECT CategoryID, COUNT(*) AS UrunSayisi
FROM Products
GROUP BY CategoryID;

SELECT SupplierID, COUNT(*) AS UrunSayisi
FROM Products
GROUP BY SupplierID;


SELECT DISTINCT Country
FROM Customers;

SELECT DISTINCT Country, City
FROM Customers;

Select * From Customers

SELECT *  FROM Customers WHERE Country='Germany'

SELECT COUNT(*) as C,Country FROM Customers GROUP BY Country HAVING COUNT(*)>5 Order By C DESC;

--Kategori ortalama fiyatı 50 birimin üzerine olan ürünler

SELECT CategoryID, AVG (UnitPrice) as AP FROM Products GROUP BY CategoryID HAVING AVG(UnitPrice) >50;

Select * From Categories;

SELECT p.CategoryID,c.CategoryName ,AVG (p.UnitPrice) as AP FROM Products p JOIN Categories c ON p.CategoryID=c.CategoryID GROUP BY p.CategoryID,c.CategoryName HAVING AVG(UnitPrice) >30;


--KAtegori ye göre ürün sayısı 10 dan fazla olanları getir

SELECT p.CategoryID,c.CategoryName,COUNT(*) as PC FROM Products p JOIN Categories c ON p.CategoryID=c.CategoryID GROUP BY p.CategoryID,c.CategoryName HAVING COUNT(*) > 10;

--Her müşterinin verdiği toplam sipariş tutarı 10.000’den fazla olanları getir

SELECT o.CustomerID,c.CompanyName,SUM(UnitPrice * Quantity) As ToplamSiparisTutari From [Order Details] od 
JOIN Orders o ON od.OrderID=o.OrderID 
JOIN Customers c ON o.CustomerID=c.CustomerID
GROUP BY o.CustomerID,c.CompanyName
HAVING SUM(UnitPrice * Quantity) > 10000;

--USA deki müşterlerden verdiği toplam sipariş tutarı 10.000’den fazla olanları getir  
SELECT o.CustomerID,c.CompanyName,SUM(UnitPrice * Quantity) As ToplamSiparisTutari From [Order Details] od 
JOIN Orders o ON od.OrderID=o.OrderID 
JOIN Customers c ON o.CustomerID=c.CustomerID
WHERE c.Country='USA'
GROUP BY o.CustomerID,c.CompanyName
HAVING SUM(UnitPrice * Quantity) > 10000;



--USA de Toplam sipariş tutarı 10.000'in üzerinde olacak
SELECT 
    o.CustomerID,
    c.CompanyName,
    COUNT(DISTINCT o.OrderID) AS SiparisSayisi,
    MAX(o.OrderDate) AS SonSiparisTarihi,
    SUM(od.UnitPrice * od.Quantity) AS ToplamSiparisTutari
FROM [Order Details] od
JOIN Orders o ON od.OrderID = o.OrderID
JOIN Customers c ON o.CustomerID = c.CustomerID
WHERE c.Country = 'USA'
GROUP BY o.CustomerID, c.CompanyName
HAVING SUM(od.UnitPrice * od.Quantity) > 10000;

--USA de Toplam sipariş tutarı 10.000'in üzerinde olacak VE sipariş sayısı 20'nin üzerinde olacak.
--Kesişim

SELECT 
    o.CustomerID,
    c.CompanyName,
    COUNT(DISTINCT o.OrderID) AS SiparisSayisi,
    MAX(o.OrderDate) AS SonSiparisTarihi,
    SUM(od.UnitPrice * od.Quantity) AS ToplamSiparisTutari
FROM [Order Details] od
JOIN Orders o ON od.OrderID = o.OrderID
JOIN Customers c ON o.CustomerID = c.CustomerID
WHERE c.Country = 'USA'
GROUP BY o.CustomerID, c.CompanyName
HAVING 
    SUM(od.UnitPrice * od.Quantity) > 10000 AND 
    COUNT(DISTINCT o.OrderID) > 20;

--USA de Toplam sipariş tutarı 10.000'in üzerinde olacak VEYA sipariş sayısı 20'nin üzerinde olacak.
--Bileşim 
SELECT 
    o.CustomerID,
    c.CompanyName,
    COUNT(DISTINCT o.OrderID) AS SiparisSayisi,
    MAX(o.OrderDate) AS SonSiparisTarihi,
    SUM(od.UnitPrice * od.Quantity) AS ToplamSiparisTutari
FROM [Order Details] od
JOIN Orders o ON od.OrderID = o.OrderID
JOIN Customers c ON o.CustomerID = c.CustomerID
WHERE c.Country = 'USA'
GROUP BY o.CustomerID, c.CompanyName
HAVING 
    SUM(od.UnitPrice * od.Quantity) > 10000 OR 
    COUNT(DISTINCT o.OrderID) > 20;


---En çok sipariş veren ilk 5 müşteri (ülke, toplam sipariş sayısı ve tutarı)

SELECT * FROM Customers;
SELECT * FROM Orders;
SELECT * FROM [Order Details];

SELECT TOP 5 c.CustomerID,c.CompanyName,c.Country,COUNT(DISTINCT o.OrderID) as SiparisSayisi ,SUM(od.UnitPrice * od.Quantity) AS ToplamTutar
FROM Customers c
JOIN Orders o ON c.CustomerID=o.CustomerID
JOIN [Order Details] od on o.OrderID=od.OrderID
GROUP BY c.CustomerID, c.CompanyName, c.Country;


-- Yıllara göre ülke bazlı toplam sipariş tutarı ve sipariş sayısı
SELECT 
    YEAR(o.OrderDate) AS Yil,
    c.Country,
    COUNT(DISTINCT o.OrderID) AS SiparisSayisi,
    SUM(od.UnitPrice * od.Quantity) AS ToplamTutar
FROM Orders o
JOIN [Order Details] od ON o.OrderID = od.OrderID
JOIN Customers c ON o.CustomerID = c.CustomerID
GROUP BY YEAR(o.OrderDate), c.Country
ORDER BY Yil, ToplamTutar DESC;


---Müşteri Segmenti

SELECT 
    c.CustomerID,
    c.CompanyName,
    SUM(od.UnitPrice * od.Quantity) AS ToplamHarcama,
    CASE 
        WHEN SUM(od.UnitPrice * od.Quantity) >= 20000 THEN 'Premium'
        WHEN SUM(od.UnitPrice * od.Quantity) >= 10000 THEN 'Gold'
        WHEN SUM(od.UnitPrice * od.Quantity) >= 5000 THEN 'Silver'
        ELSE 'Bronze'
    END AS HarcamaSegmenti
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
JOIN [Order Details] od ON o.OrderID = od.OrderID
GROUP BY c.CustomerID, c.CompanyName
ORDER BY ToplamHarcama DESC;


--Çalışan başına yıl bazlı satış performansı (ciro ve sipariş sayısı

SELECT * FROM Employees
SELECT * FROM Orders
SELECT [Order Details].*
FROM     [Order Details]

SELECT TOP 1 e.EmployeeID, 
e.FirstName + ' ' + e.LastName AS Calisan, 
YEAR(o.OrderDate) AS Yil, COUNT(DISTINCT o.OrderID) AS SiparisSayisi, 
SUM(od.UnitPrice * od.Quantity) AS ToplamSatis
FROM     Employees AS e INNER JOIN
Orders AS o ON e.EmployeeID = o.EmployeeID INNER JOIN
[Order Details] AS od ON o.OrderID = od.OrderID
WHERE YEAR(o.OrderDate)=1998
GROUP BY e.EmployeeID, e.FirstName, e.LastName, YEAR(o.OrderDate)
ORDER BY ToplamSatis DESC;

---Ençok sipariş alan
SELECT TOP 1 e.EmployeeID, 
e.FirstName + ' ' + e.LastName AS Calisan, 
YEAR(o.OrderDate) AS Yil, COUNT(DISTINCT o.OrderID) AS SiparisSayisi, 
SUM(od.UnitPrice * od.Quantity) AS ToplamSatis
FROM     Employees AS e INNER JOIN
Orders AS o ON e.EmployeeID = o.EmployeeID INNER JOIN
[Order Details] AS od ON o.OrderID = od.OrderID
WHERE YEAR(o.OrderDate)=1998
GROUP BY e.EmployeeID, e.FirstName, e.LastName, YEAR(o.OrderDate)
ORDER BY SiparisSayisi DESC;


--Her Yılın En Fazla Ciro Yapan Çalışanını Getiren Sorgu
SELECT 
    e.EmployeeID, 
    e.FirstName + ' ' + e.LastName AS Calisan, 
    YEAR(o.OrderDate) AS Yil, 
    COUNT(DISTINCT o.OrderID) AS SiparisSayisi, 
    SUM(od.UnitPrice * od.Quantity) AS ToplamSatis,
    CASE 
        WHEN SUM(od.UnitPrice * od.Quantity) = (
            SELECT MAX(Satislar.ToplamSatis)
            FROM (
                SELECT 
                    e2.EmployeeID,
                    SUM(od2.UnitPrice * od2.Quantity) AS ToplamSatis
                FROM Employees e2
                JOIN Orders o2 ON e2.EmployeeID = o2.EmployeeID
                JOIN [Order Details] od2 ON o2.OrderID = od2.OrderID
                WHERE YEAR(o2.OrderDate) = 1998
                GROUP BY e2.EmployeeID
            ) AS Satislar
        ) THEN 'Winner'
        ELSE ''
    END AS 'Not Winner'
FROM Employees e
JOIN Orders o ON e.EmployeeID = o.EmployeeID
JOIN [Order Details] od ON o.OrderID = od.OrderID
WHERE YEAR(o.OrderDate) = 1998
GROUP BY e.EmployeeID, e.FirstName, e.LastName, YEAR(o.OrderDate)
ORDER BY ToplamSatis DESC;

WITH YillikSatislar AS (
    SELECT 
        e.EmployeeID, 
        e.FirstName + ' ' + e.LastName AS Calisan, 
        YEAR(o.OrderDate) AS Yil, 
        SUM(od.UnitPrice * od.Quantity) AS ToplamSatis,
        COUNT(DISTINCT o.OrderID) AS SiparisSayisi,
        ROW_NUMBER() OVER (PARTITION BY YEAR(o.OrderDate) ORDER BY SUM(od.UnitPrice * od.Quantity) DESC) AS Sira
    FROM Employees AS e
    JOIN Orders o ON e.EmployeeID = o.EmployeeID
    JOIN [Order Details] od ON o.OrderID = od.OrderID
    GROUP BY e.EmployeeID, e.FirstName, e.LastName, YEAR(o.OrderDate)
)
SELECT *
FROM YillikSatislar
WHERE Sira = 1
ORDER BY Yil;


SELECT 
    e.EmployeeID,
    e.FirstName + ' ' + e.LastName AS Calisan,
    Y.Yil,
    Y.ToplamSatis,
    Y.SiparisSayisi
FROM Employees e
JOIN (
    SELECT 
        o.EmployeeID,
        YEAR(o.OrderDate) AS Yil,
        SUM(od.UnitPrice * od.Quantity) AS ToplamSatis,
        COUNT(DISTINCT o.OrderID) AS SiparisSayisi
    FROM Orders o
    JOIN [Order Details] od ON o.OrderID = od.OrderID
    GROUP BY o.EmployeeID, YEAR(o.OrderDate)
) Y ON e.EmployeeID = Y.EmployeeID
WHERE Y.ToplamSatis = (
    SELECT TOP 1
        SUM(od2.UnitPrice * od2.Quantity)
    FROM Orders o2
    JOIN [Order Details] od2 ON o2.OrderID = od2.OrderID
    WHERE YEAR(o2.OrderDate) = Y.Yil
    GROUP BY o2.EmployeeID
    ORDER BY SUM(od2.UnitPrice * od2.Quantity) DESC
)
ORDER BY Y.Yil;
