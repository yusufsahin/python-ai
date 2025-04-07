import re

pattern = r"\d+" # Bir veya daha fazla rakamı eşler

p=re.compile(pattern)

match=re.match(r"\d+","123abc") #başta eşleme arar
#match=re.match(r"\d+","abc123")

if match:
    print(match.group())

search=re.search(r"\d+","abc123dfe") #Tüm metin içinde eşleşme arar

if search:
    print(search.group())

matches= re.findall(r"\d+","abc123def456ghi789") # tüm eşleşmeleri liste halinde verir
print(matches)

matches2=re.findall(r"\D+","abc123def456ghi789")
print(matches2)

for match in re.finditer(r"\d+","abc123def456ghi789"):
    print(match.group())
for match in re.finditer(r"\D+","abc123def456ghi789"):
    print(match.group())

result= re.sub(r"\d+","###","abc123def456ghi789")
print(result)

result2= re.sub(r"\D+","???","abc123def456ghi789")
print(result2)

pattern2 = re.compile(r"cat|dog")

# search: yalnızca ilk eşleşmeyi bulur
match3 = pattern2.search("I have a cat and a dog and a bird")
if match3:
    print("search:", match3.group())  # sadece "cat" (ilk eşleşme)

# findall: tüm eşleşmeleri listeler
match3_1 = pattern2.findall("I have a cat and a dog")
print("findall:", match3_1)  # ['cat', 'dog']

# Eğer tüm eşleşmeleri tek tek yazdırmak istersen:
for animal in match3_1:
    print("eşleşme:", animal)

#Çapa Anchor dizgedeki konumu eşler ^ ve $

pattern3= re.compile(r"^hello")
match4= pattern3.search("hello world")
if match4:
    print("search:", match4.group())

pattern4 = re.compile(r"world$")
match5= pattern4.search("hello world")
if match5:
    print("search:", match5.group())

#Sınıf kısa yolları
#Karakter Sınıfları:
#Köşeli parantezler [] kullanarak bir karakter sınıfı tanımlayın, bu sınıf içindeki herhangi bir karakteri eşler.

#\d: Herhangi bir rakamı eşler (eşdeğer [0-9]).
#\D: Rakam olmayan herhangi bir karakteri eşler.
#\w: Herhangi bir kelime karakterini eşler (alfanumerik + alt çizgi).
#\W: Kelime olmayan herhangi bir karakteri eşler.
#\s: Herhangi bir boşluk karakterini eşler.
#\S: Boşluk olmayan herhangi bir karakteri eşler.

pattern5= re.compile(r"\d+")
#pattern5 = re.compile(r"\D+")
match6= pattern5.search("There are 123 apple")

print("search:", match6.group())

#Flags/bayraklar

pattern6= re.compile(r"hello",re.IGNORECASE)
match7= pattern6.search("Hello World")
if match7:
    print("search:", match7.group())

#Tekrarlayıcılar
#*: 0 veya daha fazla tekrar eşler.
#+: 1 veya daha fazla tekrar eşler.
#?: 0 veya 1 tekrar eşler.
#{m}: Tam olarak m tekrar eşler.
#{m,}: m veya daha fazla tekrar eşler.
#{m,n}: m ile n arasında tekrar eşler.
pattern7=re.compile(r"\d{3,}")
match8= pattern7.search("12345")
if match8:
    print("search:", match8.group())

text="Kod: 12 , fiyat : 999 , stok: 10000"

match9=re.findall(r"\d{3,}",text)
print("search:", match9)


#Açgözlü ve Açgözsüz
#Tekrarlayıcılar varsayılan olarak açgözlüdür, yani mümkün olan en fazla karakteri eşler.
#Tekrarlayıcıları açgözsüz yapmak için ? ekleyin (yani mümkün olan en az karakteri eşler).

greedy_pattern= re.compile(r"<.*>")
non_greedy_pattern= re.compile(r"<.*?>")
text="<div>hello</div>"

greedy_match=greedy_pattern.search(text)
print("search:", greedy_match.group())

non_greedy_pattern=non_greedy_pattern.search(text)
print("search:", non_greedy_pattern.group())

#Parantez Grupları

pattern8=re.compile(r"(hello) (world)")
match9=pattern8.search("hello world")
print("search:", match9.group(0))
print("search:", match9.group(1))
print("search:", match9.group(2))

#Geriye dönük referansler \number
pattern9= re.compile(r"(\b\w+)\s+\1")
match10=pattern9.search("hello hello")
#(\b\w+)
#1. grup: kelime başında başlayıp bir veya daha fazla harf/rakam/alt çizgi (\w) içerir.
#\b ile kelime sınırını belirtir. Örn: hello
#\s+
#Bir veya daha fazla boşluk karakteri (space, tab vs.)
#\1
#Yukarıda tanımlanan ilk grup ile aynı içeriği tekrar bekler.
if match10:
    print(match10.group())

pattern10= re.compile(r"\b\w+\b")
matches3=pattern10.findall("hello world")
print("search:", matches3)
for match in pattern10.finditer("hello world"):
    print(match.group())



import re
def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

email="example@example.com"
print(validate_email(email))

name="John Doe"
print(validate_email(name))

import re
def validate_phone_number(phone_number):
    pattern = r'^\+?(\d{1,3})?[-.\s]?\(?\d{1,4}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}$'
    return re.match(pattern, phone_number) is not None

phone_number="+123 456 789"
print(validate_phone_number(phone_number))

import re
def validate_ip_address(ip_address):
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    return re.match(pattern, ip_address) is not None

ip_address= "172.16.31.10"
print(validate_ip_address(ip_address))

mac_address="00-B0-D0-63-C2-26"
print(validate_ip_address(mac_address))

import  re
def validate_date(date):
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    return re.match(pattern, date) is not None
date="2002-06-11"
print(validate_date(date))

import re
def validate_url(url):
    pattern = r'^(https?|ftp)://[^\s/$.?#].[^\s]*$'
    return re.match(pattern, url) is not None
url="http://www.google.com"
print(validate_url(url))