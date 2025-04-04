def tong(n):
    if n == 1:
        return 1
    else:
        return n + tong(n - 1)


n = int(input("nhập N: "))
print(tong(n))
