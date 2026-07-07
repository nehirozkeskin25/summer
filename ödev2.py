asallar = [sayi for sayi in range(2, 101) if all(sayi % i != 0 for i in range(2, int(sayi**0.5)+1))]
print("Asal sayılar:", asallar)

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
ilk_20 = [next(fib) for _ in range(20)]
print("İlk 20 Fibonacci:", ilk_20)


liste = [[1, 2], [3, 4], [5, 6]]
tek_liste = [sayi for alt_liste in liste for sayi in alt_liste]
print("Düzleştirilmiş liste:", tek_liste)