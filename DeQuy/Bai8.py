def tongchuoihuuhan(n):
    if n == 1:
        return n
    elif n < 1:
        return "không có giá trị."
    else:
        return 1 / n + tongchuoihuuhan(n - 1)


n = int(input("nhập N: "))
print(tongchuoihuuhan(n))
