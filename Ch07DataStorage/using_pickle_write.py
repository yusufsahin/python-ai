import pickle

data = {'isim':'John','soyisim':'Doe','yas':45} #python oluşturun bir sözlük
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file,protocol=pickle.HIGHEST_PROTOCOL)