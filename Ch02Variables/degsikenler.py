x=5
y=5.0
a =4.5
name="John"
is_student=True


print(x)
print(type(x))
print(y)
print(type(y))
print(a)
print(type(a))
print(name)
print(type(name))
print(is_student)
print(type(is_student))
###hatalı tanımlamalar
#2degisken=7
#benim-degiskenim=9
#print(benim-degiskenim)

benim_degiskenim=9

print(benim_degiskenim)

print(name.upper())

print(name.lower())

k=5
l=7
print(k+l)

m=6.3
n=7.1
p=m+n
print(m+n)
print(p)

g=5
h=7.3

i=g+h
print(i)
print(type(i))

print(int(i))

c=8
c+=2
# c=c+2
print(c)

i*=3
print(i)

d=24
d/=2

print(d)

w=24//2
print(w)


str1="Hello"
str2="World"

print(str1+str2)

#Listeler
meyveler=["apple","banana","cherry"]

print(meyveler)
print(len(meyveler))
print(type(meyveler))
meyveler[0]="ananas"
print(meyveler)

numbers = [1, 2, 3, 4, 5]
print(sum(numbers))
mixed=[1,"apple",3.5,True]
print(mixed)


#Tuples - Demetler
point=(20,30)
print(point)
print(type(point))
coordinates=(5.0,6.7,8.3)
print(coordinates)
print(coordinates.index(8.3))

print(coordinates.count(8.3))

#dictionaries / sözlükler

person={"name":"John","age":25,"city":"New York"}
print(person)
print(type(person))
print(person["age"])
del person["age"]
print(person)


for key in person.keys():
    print(key,person[key])

for key,value in person.items():
    print(key,value)

values = person.values()
print(values)  # dict_values(['John', 26])

items = person.items()
print(items)  # dict_items([('name', 'John'), ('age', 26)])
person.update({"city":"Texas"})
print(person)


person2 = {
    "name": "John",
    "age": 25,
    "address": {
        "city": "New York",
        "zip": "10001"
    }
}

# İç içe sözlüğe erişim
print(person2["address"]["city"])  # New York
print(person2["address"]["zip"])   # 10001