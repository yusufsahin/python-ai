#Class tanımlama
from email.quoprimime import body_check


class Arac:
    def __init__(self, marka,model):
        self.marka = marka
        self.model = model

class Araba(Arac):
    sayac=0
    def __init__(self, marka, model,kapi_sayisi):
        super().__init__(marka,model)
        self.kapi_sayisi = kapi_sayisi
        Araba.sayac+=1

    #classmethod
    @classmethod
    def araba_sayisi(cls):
        return cls.sayac
    #method
    def bilgi(self):
        return  f"{self.marka} {self.model} {self.kapi_sayisi}"
    def __str__(self):
        return f" from __str__ {self.marka} {self.model} {self.kapi_sayisi}"

#Nesne / Object Oluşturma

araba1= Araba("Toyota","Corolla",4)
araba2=Araba("BMW","320",4)

print(araba1.bilgi())
print(araba2.__str__())
print(araba1.araba_sayisi())

#Operatör Aşırı Yükleme (Operator Overloading)
#Operatör aşırı yükleme, Python'da operatörlerin özel anlamlar kazanmasını sağlar.
# Örneğin, + operatörünün __add__ yöntemi ile aşırı yüklenmesi.

class Vektor:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"{self.x} {self.y}"
    def __add__(self,other):
        return Vektor(self.x+other.x,self.y+other.y)

vektor1 = Vektor(10,20)
vektor2 = Vektor(4,5)
vektor3= vektor1 + vektor2

print(vektor3)

#Method

class Kare:
    def __init__(self,kenar):
        self.kenar = kenar
    def alan(self):
        return self.kenar **2

#Özellikler  ve Dekorator

class Dikdortgen:
    def __init__(self,en,boy):
        self.en = en
        self.boy = boy
    @property
    def alan(self):
        return self.en * self.boy
#property
dikdortgen = Dikdortgen(15,20)
print(dikdortgen.alan)
#Method
kare = Kare(10)
print(kare.alan())


