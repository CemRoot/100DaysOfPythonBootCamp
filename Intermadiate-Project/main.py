def func(n):
    if n == 1:
        return 1
    else:
        return n * func(n - 1)

    sonuc = func(6)
    print(sonuc)

