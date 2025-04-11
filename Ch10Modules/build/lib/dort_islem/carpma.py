"""
Bu modül çarpma işlemi sağlar.
"""


def carp(a, b):
    """
    İki sayıyı çarpar.

    Args:
        a (float): Birinci sayı.
        b (float): İkinci sayı.

    Returns:
        float: a ve b'nin çarpımı.
    """
    return a * b


if __name__ == "__main__":
    # Test kodu
    print(carp(5, 3))  # Çıktı: 15