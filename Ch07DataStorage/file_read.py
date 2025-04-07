with open("example1.txt", "r") as file:
    content = file.read()
    print(content)

with open("example1.txt", "r") as file:
    line=file.readline()
    while line:
        print(line,end='')
        line = file.readline()

with open("example2.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line,end='')

with open("example2.txt", "r") as file:
    for line in file:
        print(line,end='')