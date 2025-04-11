"""
Bu modül çıkarma işlemi sağlar.
"""


def cikar(a, b):
    """
    İki sayıdan birini çıkarır.

    Args:
        a (float): Birinci sayı.
        b (float): İkinci sayı.

    Returns:
        float: a'dan b'nin çıkarılması sonucu.
    """
    return a - b


if __name__ == "__main__":
    # Test kodu
    print(cikar(5, 3))  # Çıktı: 2