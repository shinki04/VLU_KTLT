def tong_binh_phuong(n):
    if n == 1:
        return n
    elif n < 1:
        return "không có giá trị."
    else:
        return n**2 + tong_binh_phuong(n - 1)


n = int(input("nhập N: "))
print(tong_binh_phuong(n))
