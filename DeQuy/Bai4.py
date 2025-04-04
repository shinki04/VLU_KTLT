def tongso(n):
    if n < 10:
        return n
    elif n <= 0:
        return "giá trị không hợp lệ"
    else:
        return n % 10 + tongso(n // 10)


n = int(input("nhập N: "))
print(int(tongso(n)))

