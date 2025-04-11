"""
Bu modül bölme işlemi sağlar.
"""


def bol(a, b):
    """
    İki sayıyı böler.

    Args:
        a (float): Birinci sayı.
        b (float): İkinci sayı.

    Returns:
        float: a'nın b'ye bölümü.
    """
    if b == 0:
        raise ValueError("Bölme işlemi için bölen 0 olamaz.")
    return a / b


if __name__ == "__main__":
    # Test kodu
    print(bol(6, 3))  # Çıktı: 2.0