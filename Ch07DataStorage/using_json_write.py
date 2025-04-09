import json

data = {'isim': 'John', 'soyisim': 'Doe', 'yas': 45}
with open("data.json",'w',encoding='utf-8') as json_file:
   json.dump(data, json_file, ensure_ascii=False, indent=4)