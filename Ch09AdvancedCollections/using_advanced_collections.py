sayilar=[1,2,3,4,5,6]

cift_sayilar=[]

for sayi in sayilar:
    if sayi%2==0:
        cift_sayilar.append(sayi)

print(cift_sayilar)

cift_sayilar_2=list(filter(lambda x:x%2==0,sayilar))
print(cift_sayilar_2)

tek_sayilar=list(filter(lambda x:x%2==1,sayilar))
print(tek_sayilar)

#Küme ve Sözlük Anlayışları(Set and Dictionary Comprehensions)

#Küme
sayilar2= [1,2,3,4,4,5,5]

kareler_kumesi={x**2 for x in sayilar2}
print(kareler_kumesi)

#Sözlük / dictinary

sayilar2= [1,2,3,4,5,]

kareler_sozlugu= {x:x**2 for x in sayilar2}
print(kareler_sozlugu)

kupler_sozlugu={x:x**3 for x in sayilar2}
print(kupler_sozlugu)

#Lazy List
#, veri üretilene kadar hesaplamayı
# erteleyen bir yaklaşımdır.
# Bu özellikle büyük
# veri kümeleri ile çalışırken
# bellek tasarrufu sağlar.

lazy_list=(x*x for x in range(1000000))
for i in range(5):
    print(next(lazy_list))

lazy_list2 = (x**2 for x in range(10))
for sayi in lazy_list2:
    print(sayi)


#Generator yield

def kareler(n):
    for i in range(n):
        yield i**2

lazy_kareler= kareler(10)
for k in lazy_kareler:
    print(k)

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a,b = b, a+b

for sayi in fibonacci(10):
    print(sayi)

#Generator - next()

def basit_generator():
    yield 1
    yield 2
    yield 3
    yield 4

gen= basit_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
#print(next(gen)) #hata verir

#Liste anlayışları ile generator

generator=(x**2 for x in range(5))
for x in generator:
    print(x)

#kopyalama problemi
original_p=[1,2,3]

kopya_p=original_p
kopya_p.append(4)
print(kopya_p)
print(original_p)

import copy
kopya_p_deep=copy.deepcopy(original_p)
kopya_p_deep.append(5)
print(kopya_p_deep)
print(original_p)

#dilimleme ile copya

original=[1,2,3]
kopya=original[:]
kopya.append(4)
print(kopya)
print(original)