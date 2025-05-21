import matplotlib.pyplot as plt
import time

def draw_merge(arr, title=""):
    plt.clf()
    plt.bar(range(len(arr)), arr, color='skyblue')
    plt.title(title)
    plt.pause(0.6)

def merge_sort_visual(arr, level=0):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort_visual(L, level + 1)
        merge_sort_visual(R, level + 1)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            draw_merge(arr, title=f"Merge: {arr}")

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            draw_merge(arr, title=f"Left ekleniyor: {arr}")

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            draw_merge(arr, title=f"Right ekleniyor: {arr}")



def merge_sort(arr):
    if len(arr) > 1:
        mid=len(arr)//2 #Ortayı bul
        L=arr[:mid] #Sol alt dizi
        R=arr[mid:] #Sağ alt dizi
        merge_sort(L)
        merge_sort(R)
        i=j=k=0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1
        while i < len(L):
            arr[k]=L[i]
            i+=1
            k+=1
        while j < len(R):
            arr[k]=R[j]
            j+=1
            k+=1
def merge_sort_trace(arr, level=0):
    indent = "  " * level
    print(f"{indent}Giriş: {arr}")
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        print(f"{indent}Sol böl: {L}")
        merge_sort_trace(L, level + 1)

        print(f"{indent}Sağ böl: {R}")
        merge_sort_trace(R, level + 1)

        i = j = k = 0

        print(f"{indent}Birleştiriliyor: {L} + {R}")
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

        print(f"{indent}Sonuç: {arr}")

arr=[38,27,43,3,9,82,10]
print("Orijinal dizi:", arr)
merge_sort(arr)
print("Sıralı dizi:", arr)

arr2=[38,27,43,3,9,82,10]
merge_sort_trace(arr2)
arr3 = [38, 27, 43, 3, 9, 82, 10]
plt.ion()
merge_sort_visual(arr3)
plt.ioff()
draw_merge(arr3, "Sıralanmış Sonuç")
plt.show()
