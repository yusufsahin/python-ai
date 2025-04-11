"""
Bu modül toplama işlemi sağlar
"""
def topla(a,b):
    """
    İki sayıyı toplar.

    Args:
        a (float): Birinci sayi
        b (float): İkinci sayi

    Returns:
        float: a ve b 'nin toplamı.
    """
    return a+b
if __name__ == '__main__':
    #Test Kodu
    print(topla(2,3)) #Çıktı 8