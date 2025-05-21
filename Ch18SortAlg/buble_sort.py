import matplotlib.pyplot as plt
import time

def draw_array(arr, highlight=None, title=""):
    plt.clf()
    colors = ['red' if i in highlight else 'skyblue' for i in range(len(arr))]
    plt.bar(range(len(arr)), arr, color=colors)
    plt.title(title)
    plt.xlabel("Index")
    plt.ylabel("Değer")
    plt.pause(0.5)

def bubble_sort_visual(arr):
    n = len(arr)
    plt.ion()
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            draw_array(arr, highlight=[j, j+1], title=f"Karşılaştır: arr[{j}] ve arr[{j+1}]")
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                draw_array(arr, highlight=[j, j+1], title=f"Swap: arr[{j}] ve arr[{j+1}]")
        if not swapped:
            break
    plt.ioff()
    draw_array(arr, title="Sıralı Dizi")
    plt.show()



def buble_sort(arr):
    n=len(arr)  #length of the array
    for i in range(n): #iterating through the array
        swapped = False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]: #if the current element is greater than the next element
                arr[j],arr[j+1]=arr[j+1],arr[j] #swap the elements
                swapped = True
        if not swapped:
            break

def bubble_sort_trace(arr):
    n = len(arr)
    for i in range(n):
        print(f"\nTur {i+1}:")
        swapped = False
        for j in range(0, n - i - 1):
            print(f"  Karşılaştırılıyor: arr[{j}] = {arr[j]} ve arr[{j+1}] = {arr[j+1]}")
            if arr[j] > arr[j + 1]:
                print(f"    Yer değiştiriliyor: {arr[j]} > {arr[j+1]} → swap")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            else:
                print(f"    Sıralı: {arr[j]} ≤ {arr[j+1]}")
            print(f"    Ara durum: {arr}")
        if not swapped:
            print("  Hiçbir değişiklik yapılmadı, erken çıkış.")
            break
    print("\nSıralanmış dizi:", arr)


arr=[5,1,4,2,8]
print(arr)
buble_sort(arr)
print("Sorted array is:",arr)

# Bubble Sort with Trace
arr2=[5,1,4,2,8]

bubble_sort_trace(arr2)

arr3=[5,1,4,2,8]

bubble_sort_visual(arr3)