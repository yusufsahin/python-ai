
#Demet oluşturma
t=(1,2,3,4,2,5,6,2)
print(t)
print(t[1])

print(type(t))
print(len(t))
print(t.count(2))
print(t.index(3))

#Liste

my_list=[1,2,3]
print(my_list)
my_list.append(4)
print(my_list)
my_list.extend([5,6])
print(my_list)
my_list.insert(0,0)
print(my_list)
my_list.remove(3) #değere göre siler
print(my_list)
my_list.pop(5) #konuma göre siler
print(my_list)


liste=['elma','armut','muz']
meyve=liste.pop(1)
print(meyve)
print(liste)
liste.remove('muz')
print(liste)
my_list.reverse()
print(my_list)
my_list.sort()
print(my_list)

#slicing

l=[1,2,3,4,5,6]

print(l)
print(l[1:4])
print(l[:4])
print(l[2:])
print(l[::1])
print(l[::2])
print(l[::-1])

a,b,*rest=[1,2,3,4,5]

print(a,b,rest)

print(type(a),type(b),type(rest))
a=[1,2,3]

print(type(a))
a.append(4)
print(a)
a.extend([5,6])
print(a)
a.insert(0,0)
print(a)
a.pop(1)
print(a)
del a[0]
print(a)

b=[1, 2, 3, 4, 2, 5]

b.remove(2)
print(b)
b.remove(2)
print(b)

c=[3,1,4,1,5,9]
c.sort()
print(c)

sorted_c=sorted(c)
print(sorted_c)

d=c.copy()
print(d)
print(c.count(1))

#Kümeler { }

s1={1,2,3,7}
s2={4,5,6,7}
print(s1)
print(s2)

print(s1 | s2) #bileşimi
print(s1 & s2)
print(s1 - s2)
print(s2 - s1)
print(s1 ^ s2) #simetrik fark
print(s1.intersection(s2))
print(s2.intersection(s1))

#Küme Operatörleri
a1={1,2,3}
a2={1,2}

print(a2<=a1)
print(a2<a1)
print(a1>=a2)
print(a1>a2)

#Sözlükler key - value

d={'isim':'Alice','yaş':25}
print(d['isim']) #değer erişim
print(d)
d['yaş']=30  # değer güncelleme
print(d)


# Temel Methodlar

sozluk={'isim':'John','yaş':25}

print(sozluk.keys())
print(sozluk.values())
print(type(sozluk.keys()))
print(type(sozluk.values()))
print(sozluk.items())
print(sozluk.get('isim'))
print(sozluk.get('yaş'))
print(sozluk.get('şehir')) #Hata vermez ,None döner


#update

sozluk.update({'yaş':27,'şehir':'Texas'})

print(sozluk)

#View Object / Görünüm nesnleri

v= {'isim':'Alice','yaş':25}
print(v)
keys_view=v.keys()
print(keys_view)
v['şehir']='Texas'
print(keys_view)
values_view=v.values()
items_view=v.items()

v['ülke']='USA'

print(keys_view)
print(values_view)
print(items_view)

# Sözlük üzerinde döngü

person={'isim':'Ali','yaş':35,'şehir':'Ankara'}
for k in person.keys():
    print(k)
for v in person.values():
    print(v)


for k,v in person.items():
    print(f"{k} : {v}")

if 'isim' in person:
    print(person['isim'])

squares ={x: x**2 for x in range(5)}
print(squares)

ogreciler ={
    '001':{'isim':'Ahmet' ,'not':65},
    '002':{'isim':'Fatma' ,'not':75},
}

print(ogreciler.get('001'))
print(ogreciler.get('002'))
print(ogreciler['001']['isim'])