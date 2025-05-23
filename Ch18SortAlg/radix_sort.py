def counting_sort_by_digit(arr,exp):
    n = len(arr)
    output= [0]*n
    count=[0]*10

    #1.Sayıları basamağa göre say
    for num in arr:
        index = (num//exp)%10
        count[index]+=1

    #2.Kümülatif toplama
    for i in range(1,10):
        count[i]+=count[i-1]

    #Output dizisini oluştur(ters sırada->kararlılık için)
    for i in range(n-1,-1,-1):
        index = (arr[i]//exp)%10
        output[count[index]-1]=arr[i]
        count[index]-=1

    #4. Orijinal diziyi kopyala
    for i in range(n):
        arr[i]=output[i]

def radix_sort(arr):
    if not arr:
        return
    max_val = max(arr)
    exp = 1
    while max_val//exp > 0:
        counting_sort_by_digit(arr,exp)
        exp*=10

if __name__ == "__main__":
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Orijinal Dizi:", arr)
    radix_sort(arr)
    print("Sıralı Dizi:", arr)