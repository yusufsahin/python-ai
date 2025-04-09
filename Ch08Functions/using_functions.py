def merhaba():
    print("Merhaba Dünya")

merhaba()

#parametre kullanımı
def topla(a,b):
    return a+b

sonuc=topla(10,20)

print(sonuc)
print(type(sonuc))

sonuc2=topla(10.5,20)
print(sonuc2)
print(type(sonuc2))

sonuc3=topla(10.5,20.9)
print(sonuc3)
print(type(sonuc3))

sonuc4=topla(10,20.6)
print(sonuc4)
print(type(sonuc4))

#değişken sayıda parametre

def topla(*sayilar):
    return sum(sayilar)

print(topla(10,20,30,40,50))

#keyword anahtar - değer çiftine göre çoklu parametre

def bilgiler(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")
        print("-----------------")

bilgiler(isim="Ali",yas=30)
bilgiler(isim="Ahmet",yas=35,sehir="İstanbul")
bilgiler(isim="Mehmet",yas=40,sehir="Ankara",ilce="Mamak")

#Default Değer Parametre

def selamla(isim="Misafir"):
    print(f"Merhaba, ", isim)
selamla()
selamla(isim="John")

def kare(x=0):
    return x*x

kare_sonuc=kare(5)
print(kare_sonuc)
kare_sonuc2=kare()
print(kare_sonuc2)

#Global ve yerel değişkenler

x=10 #Global
def fonksiyon():
    x=5 #yerel
    print(x)
fonksiyon()
print(x)

#iç içe

def dis_fonksiyon():
    print("Dış fonksiyon")
    def ic_fonksiyon():
        print("İç fonksiyon")
        def son_fonksiyon():
            print("Son fonksiyon")
        son_fonksiyon()
    ic_fonksiyon()
dis_fonksiyon()

#kapsam

def dis_fonksiyon_kapsam():
    x=10
    print("dış: ",x)
    def ic_fonksiyon_kapsam():
        print("iç: ",x)
    ic_fonksiyon_kapsam()
dis_fonksiyon_kapsam()

#Docstring

def carp(a,b):
    """
    Bu fonksiyon 2 sayıyı carpar
    """
    return a*b
print(carp(2,3))
print(carp.__doc__)

## lamda

kare = lambda x:x*x
print(kare(10))

toplama = lambda a,b: a+b
print(toplama(10,20))

selam=lambda isim="Misafir": f"Merhaba {isim}"
print(selam())
print(selam("John"))


liste=[(2,3),(1,2),(4,1)]
liste.sort(key=lambda x:x[1])
print(liste)

#regex re.sub

import re
text= "Merhaba 123 Dünya"

result= re.sub(r'\d+',lambda x:str(int(x.group(0))*2),text)
print(result)


#rekürsif / kendi kendini cagiran fonkiyon

def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1) #5*4*3*2*1
print(factorial(5))
print(factorial(10))
print(factorial(100))

def fibonacci(n):
    if n<0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

n=20
fib_series=[fibonacci(i) for i in range(n)]
print(fib_series)