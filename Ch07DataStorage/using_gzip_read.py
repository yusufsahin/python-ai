import gzip

with gzip.open('example1.txt.gz', 'rb') as file:
    data=file.read()
    print("Okunan sıkıştırılmış veri")
    print(data)
    decoded_data=data.decode('utf-8')
    print("Çözülen veri")
    print(decoded_data)