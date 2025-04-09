with open('example1.txt', 'r') as file:
    file.seek(10) #10.Byte a git
    data = file.read(5) # sonraki 5 byte oku
    print(data)

    position=file.tell() #cursor un bulunduğu yer
    print(position)

    data2=file.read(position+5)
    print(data2)
    position2=file.tell()
    print(position2)