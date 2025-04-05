tek_tirnak_str='Merhaba'
cift_tirnak_str="Dünya"
cok_satir_str="""Bu
çok satırlı
bir
stringtir.
"""


print(tek_tirnak_str)
print(cift_tirnak_str)
print(cok_satir_str)

print("Merhaba dünya!")
print('Merhaba dünya!')
print("""
Test
çoklu
satır
""")

quato_mevlana="Mevlana dedi ki 'Ya olduğun gibi görün ya göründüğün gibi ol'"
quato_mevlana_2="Mevlana dedi ki \"Ya olduğun gibi görün ya göründüğün gibi ol\""

print(quato_mevlana)
print(quato_mevlana_2)
quato_yunusemre='Yunus dedi ki :"Ben denizde inciyim"'
print(quato_yunusemre)

quato_yunusemre_2='Yunus dedi ki :\'Ben denizde inciyim\''
print(quato_yunusemre_2)
# çift tırnak içinde tek tırnak veya tek tırnak içinde çift tırnak escape karakterden kurtarır
import  json

data='{"name":"John","surname":"Smith","age":30}'
parsed=json.loads(data)
print(parsed["name"])

#Ayırıcı /Separatör
print("Merhaba","dünya","!")
print("Merhaba","dünya","!",sep="-")
print("Merhaba","dünya","!",sep=";")

#Sonlandırıcı

print("Merhaba Dünya!",end=" BİTTİ\n")

yeni_satır_str= "\nMerhaba\nDünya\n!"
print(yeni_satır_str)

#cooking string
tab_str="Merhaba\tDünya\t!"
print(tab_str)
print('O "Merhaba" dedi')
print("O 'Merhaba' dedi")

print('O \'Merhaba\' dedi')
print("O \"Merhaba\" dedi")

ters_slash_str="bu bir ters slash \\"

print(ters_slash_str)

#Concanateation / String birleştirme işlemleri

merhaba_str="Merhaba"
dunya_str="Dunya"
merhaba_dunya_str=merhaba_str+dunya_str
print(merhaba_dunya_str)
merhaba_dunya_str2=merhaba_str+" "+dunya_str
print(merhaba_dunya_str2)

#tekrarlama

tekrar_str="merhaba"*3
print(tekrar_str)
uc_tırnak_str="""Bu bir çok satırlı ve 
'tek tırnak' ile "çift tırnak" 
içeren string"""
print(uc_tırnak_str)

#string yöntemleri
s="merhaba"
print(s.upper())
k="DÜNYA"
print(k.lower())
print(s.capitalize())
t="merhaba dünya, merhaba uzay"
print(t.title())

v="     Merhaba Dünya      "
print(len(v))
print(v.strip())
u=v.strip()
print(len(u))

z="merhaba dünya"

print(z.replace("dünya","python").title())

print(z.find("dünya"))
print("merhaba dünya ve python".title())
l="merhaba dünya, merhaba uzay , merhaba python"
print(l.count("merhaba"))

print("merhaba Python".startswith("mer"))

m="merhaba dünya, merhaba uzay , merhaba python"
print(m.endswith("python"))

g="merhaba"
print(g.isalpha())

print(g.isdigit())

print("12345".isdigit())
print("12345".isalpha())

print("12345".isspace())
print("     ".isspace())
print("     ".isalpha())


#String formatlama

#% operatörü

name="Alice"
age=30

formatted_str="İsim: %s, Yaş: %d"%(name,age)
print(formatted_str)

format_func_str="İsim: {}, Yaş: {}".format(name,age)
print(format_func_str)

#f string

f_str= f"İsim: {name}, Yaş: {age}"

print(f_str)

#Diğer yardımcılar

person={"name":"Alice","age":30}
formatted_dicti_str="İsim: {name}, Yaş: {age}".format(**person)
print(formatted_dicti_str)

from string import Template

template=Template("İsim: ${name}, Yaş: ${age}")
formatted_temp_str=template.substitute(name="Alice",age=30)
print(formatted_temp_str)
formatted_temp_str2=template.substitute(name=person["name"],age=person["age"])
print(formatted_temp_str2)


#Slicing s:[start:stop:step]

h="merhaba dünya"

print(h[0:7])
print(h[8:])
print(h[:7])
print(h[::2])
print(h[::-1])

#split

n=("merhaba dünya")
kelimeler=n.split()
print(kelimeler)

csv="John;Doe;30"
kisi=csv.split(";")
print(kisi)


#join

sozcukler=["merhaba","dünya","merhaba","python"]
print(' '.join(sozcukler))
print('\n'.join(sozcukler))
print('\t'.join(sozcukler))
print(';'.join(sozcukler))
print('|'.join(sozcukler))




