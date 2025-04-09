import json
try:
    with open("data.json","r",encoding="utf-8") as json_file:
        data = json.load(json_file)
        print(data)
        print(type(data))
        print("İsim:  ",data["isim"])
except FileNotFoundError:
    print("Dosya Bulunamadı.")
except json.JSONDecodeError:
    print("JSON formatında problem var.")
