import gzip

with gzip.open('example1.txt.gz', 'wb') as file:
    data="Merhaba Dünya,Merhaba Python!".encode('utf-8')
    file.write(data)
    print("Veri sıkıştırıldı ve yazıldı.")