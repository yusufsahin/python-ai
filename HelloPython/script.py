# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.

def greet(name):
    """
    Greet the person with the given name.

    Parameters:
    name (str): The name of the person to greet.

    Returns:
    str: A greeting message.
    """
    return f"Hello, {name}!"


if __name__ == '__main__':
    print("Hello Python!")
    print_hi('PyCharm')
    print(greet.__doc__)
    print(dir(math))

    age=25
    print(age)
    print(type(age))

    sicaklik=23.7
    print(sicaklik)
    print(type(sicaklik))

    isim="John"
    print(isim)
    print(type(isim))

    meyveler={"Elma","Armut","Portakal"}
    print(meyveler)
    print(type(meyveler))

    meyveler2=["Elma","Armut","Portakal"]
    print(meyveler2)
    print(type(meyveler2))

    print(len(meyveler2))

    #name= input("What is your name? ")
    #print(name)

    age2=int("25")
    print(age2)

    print(abs(-10))  # 10

    for index, meyve in enumerate(meyveler2):
        print(index,meyve)

    print(round(3.14159, 2))  # 3.14
    for i in range(3):
        print(i)  # 0, 1, 2
