import matplotlib.pyplot as plt
import time

def draw_array(arr, title):
    plt.clf()
    plt.bar(range(len(arr)), arr, color='skyblue')
    plt.title(title)
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.pause(0.8)

def selection_sort_visual(arr):
    n = len(arr)
    plt.ion()
    for i in range(n):
        min_index = i
        draw_array(arr, f"Adım {i+1} - Başlangıç")
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        draw_array(arr, f"Adım {i+1} - Swap ({i}, {min_index})")
    plt.ioff()
    plt.show()

# Selection Sort
def selection_sort(arr):
    n=len(arr)  #length of the array
    for i in range(n): #iterating through the array
        min_index=i #index of the minimum element
        for j in range(i+1,n): #iterating through the array
            if arr[j]<arr[min_index]: #if the current element is less than the minimum element
                min_index=j #update the index of the minimum element
        arr[i],arr[min_index]=arr[min_index],arr[i] #swap the elements

def selection_sort_trace(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        print(f"\nAdım {i+1}:")
        print(f"Başlangıç dizisi: {arr}")
        for j in range(i + 1, n):
            print(f"Karşılaştır: arr[{j}] = {arr[j]} vs arr[{min_index}] = {arr[min_index]}")
            if arr[j] < arr[min_index]:
                min_index = j
                print(f"Yeni minimum bulundu: arr[{min_index}] = {arr[min_index]}")
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"arr[{i}] ile arr[{min_index}] yer değiştirildi: {arr}")


arr=[29,10,14,37,13]
print(arr)
#calling the function
# Selection Sort
selection_sort(arr) #calling the function
print("Sorted array is:",arr) #printing the sorted array
arr2=[29,10,14,37,13]
# Selection Sort with Trace
selection_sort_trace(arr2)
print("Sorted array is:",arr)
arr3=[29,10,14,37,13]
# Visualize Selection Sort
selection_sort_visual(arr3)
print("Sorted array is:",arr)