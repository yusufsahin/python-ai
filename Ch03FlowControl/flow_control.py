x=int(input("Bir sayı giriniz: "))

if x>5:
    print("x, 5'ten büyüktür.")
elif x==5:
    print("x, 5'e eşittir.")
else:
    print("x, 5'ten küçüktür.")

if not []:
    print("Empty list is considered False.")

a=True
b=False

print(a and b) #False
print(a or b) #True
print(not a) #False

k=7
print(k>1 and k<10)
#zincir karşılaştırma
print(1<k<10)  # k>1 and k<10 and=>&&
print(10<k<20)

meyveler=["elma","portakal","mandalina"]
print("elma" in meyveler)
print("üzüm" in meyveler)
print("üzüm" not in meyveler)

z=42
print(type(z) is int)
print(isinstance(z,int))

z=42.5
print(type(z) is int)
print(type(z) is  not int)
print(type(z) is float)
print(isinstance(z,int))
print(isinstance(z,float))
print("///////")
try:
    #result=10/0
    result=10//2
except:
    print("sayi sifira bölünemez")
else:
    print(result)
    print(type(result) is float)
    print("Hata ile karşılaşılmadı")
finally:
    print("Her durumda çalışır")


count=0
while count <5:
    print(count)
    if count==3:
        break
    count+=1 #count=count+1

for i in range(10):
    if i==5:
        break
    print(i)

for j in range(1,10):
    print("*"*j)

import  random

rastgele_sayilar= [random.randint(1,100) for _ in range(5)]
for s in rastgele_sayilar:
    print("Rastgele sayi:", s)

for a in range(3):
    for b in range(3):
         print(f"a={a}, b={b}")

for meyve in meyveler:
    print(meyve)

for index,meyve in enumerate(meyveler):
    print(index,meyve)

names=["Alice","Bob","Charlie"]
ages=[10,20,30]
for name,age in zip(names,ages):
    print(f"{name} is {age} years old")

age=17
status="Adult" if age>=18 else "Minor"
print(status)

m=4
if m>0:
    pass # Henüz kodlanmadı
else:
    print("Negatif sayi")

numbers=[]
print(numbers)
for number in range(10):
    numbers.append(number)
print(numbers)

c= range(3,6)

for d in c:
    print("sayi : "+ str(d))