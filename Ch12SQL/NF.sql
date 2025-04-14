--//DERS KAYIT SİSTEMi


--KAYITLAR TABLOSU


--NORMALİZASYON YOK

CREATE TABLE Kayitlar (
    OgrenciID INT,
    OgrenciAdSoyad NVARCHAR(100),
    Ders1 NVARCHAR(50),
    Ders2 NVARCHAR(50),
    Ders3 NVARCHAR(50),
    Ogretmen1 NVARCHAR(100),
    Ogretmen2 NVARCHAR(100),
    Ogretmen3 NVARCHAR(100)
);

--1NF
CREATE TABLE Kayitlar1NF (
    OgrenciID INT,
    OgrenciAdSoyad NVARCHAR(100),
    Ders NVARCHAR(50),
    Ogretmen NVARCHAR(100)
);
--
--1	Ali Veli	Matematik	Ayşe Hoca
--1	Ali Veli	Fizik	Ahmet Hoca
--1	Ali Veli	Kimya	Zeynep Hoca


-- 2NF 
CREATE TABLE Ogrenci (
    OgrenciID INT PRIMARY KEY,
    AdSoyad NVARCHAR(100)
);


CREATE TABLE Kayitlar2NF (
    OgrenciID INT,
    Ders NVARCHAR(50),
    Ogretmen NVARCHAR(100),
    FOREIGN KEY (OgrenciID) REFERENCES Ogrenci(OgrenciID)
);

--3NF

CREATE TABLE Ders (
    DersID INT PRIMARY KEY,
    DersAdi NVARCHAR(50),
    OgretmenID INT
);

CREATE TABLE Ogretmen (
    OgretmenID INT PRIMARY KEY,
    AdSoyad NVARCHAR(100)
);

CREATE TABLE Kayitlar3NF (
    OgrenciID INT,
    DersID INT,
    FOREIGN KEY (OgrenciID) REFERENCES Ogrenci(OgrenciID),
    FOREIGN KEY (DersID) REFERENCES Ders(DersID)
);


--Elde Edilen Yapı

--OgrenciID | AdSoyad
------------|--------
--1         | Ali Veli

--DersID | DersAdi    | OgretmenID
---------|------------|-----------
--101    | Matematik  | 201
--102    | Fizik      | 202
--103    | Kimya      | 203


--OgretmenID | AdSoyad
-------------|---------------
--201        | Ayşe Hoca
--202        | Ahmet Hoca
--203        | Zeynep Hoca


--OgrenciID | DersID
------------|--------
--1         | 101
--1         | 102
--1         | 103


--BCNF, 4NF, 5NF

CREATE TABLE Siniflar (
    SinifKodu NVARCHAR(10),
    Ogretmen NVARCHAR(100),
    Ders NVARCHAR(100),
    PRIMARY KEY (SinifKodu, Ders)
);

CREATE TABLE Siniflar (
    SinifKodu NVARCHAR(10),
    Ders NVARCHAR(100),
    PRIMARY KEY (SinifKodu, Ders)
);

CREATE TABLE SinifOgretmen (
    SinifKodu NVARCHAR(10) PRIMARY KEY,
    Ogretmen NVARCHAR(100)
);

--4NF

CREATE TABLE Projeler (
    CalisanID INT,
    Yetenek NVARCHAR(50),
    Proje NVARCHAR(50),
    PRIMARY KEY (CalisanID, Yetenek, Proje)
);

CREATE TABLE CalisanYetenek (
    CalisanID INT,
    Yetenek NVARCHAR(50),
    PRIMARY KEY (CalisanID, Yetenek)
);

CREATE TABLE CalisanProje (
    CalisanID INT,
    Proje NVARCHAR(50),
    PRIMARY KEY (CalisanID, Proje)
);


-- 5NF – Beşinci Normal Form (Join Normal Form)

--Bir ürünün birçok tedarikçisi olabilir
--Aynı ürün birçok ülkede satılabilir
--Her tedarikçi de bazı ülkelere teslimat yapabilir
--Ama ürün–tedarikçi–ülke bilgisi tek tabloya sıkıştırılmış

CREATE TABLE Uretim (
    UrunID INT,
    TedarikciID INT,
    Ulke NVARCHAR(50),
    PRIMARY KEY (UrunID, TedarikciID, Ulke)
);

CREATE TABLE UrunTedarikci (
    UrunID INT,
    TedarikciID INT,
    PRIMARY KEY (UrunID, TedarikciID)
);

CREATE TABLE UrunUlke (
    UrunID INT,
    Ulke NVARCHAR(50),
    PRIMARY KEY (UrunID, Ulke)
);

CREATE TABLE TedarikciUlke (
    TedarikciID INT,
    Ulke NVARCHAR(50),
    PRIMARY KEY (TedarikciID, Ulke)
);


--NForm	- Amaç
--1NF	- Tekil (atomik) hücreler
--2NF	- Kısmi bağımlılıkları kaldır
--3NF	- Geçişli bağımlılıkları kaldır
--BCNF	- Aday anahtar olmayan bağımlılıkları kaldır --%80
--4NF	- Çok değerli bağımlılıkları parçala
--5NF	- Join'den oluşan gizli tekrarları ayrıştır  --%20