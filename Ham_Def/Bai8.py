"""
8.	Viết hàm tìm các số nguyên tố trong khoảng [a,b]
Gợi ý: Hàm này nhận vào hai số nguyên a và b. Hàm sẽ trả về danh sách các số nguyên tố trong khoảng từ a đến b.

"""


# * Function này chỉ chịu trách nhiệm kiểm tra
def kiem_tra_so_nguyen_to(a):
    if a < 1:
        return "khong phai so nguyen to"
    for i in range(1, a):
        if a % i == 0:
            return False
    return True


# * Function chịu trách nhiệm thêm số nguyên tốc vào danh sách
def dsnt(a, b):
    ds = []
    for i in range(a, b + 1):
        if kiem_tra_so_nguyen_to(i) is True:
            ds.append(i)
    return ds


a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print("Các số nguyên tố là ", dsnt(a, b))

#! Câu hỏi : Liệu ds có thể sử dụng bên ngoài như bài trước không, kiểu:
"""
dsnt(a,b)
print(ds)
"""
# * Các bạn có thể thử
