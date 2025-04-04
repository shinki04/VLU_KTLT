"""
2.	Viết hàm kiểm tra một số là số nguyên tố hay không?
Định nghĩa: Số nguyên tố là số chia hết cho 1 và chính nó
VD: Hàm nhận tham số a = 12, kết quả trả về “Không phải số nguyên tố”

"""


def kiem_tra_so_nguyen_to(a):
    if a < 1:
        return "khong phai so nguyen to"
    for i in range(1, a):
        if a % i == 0:
            return False
    return True


a = int(input("Nhập vào số nguyên a: "))
if kiem_tra_so_nguyen_to(a) is True:
    print("Số nguyên tố")
else:
    print("Không là số nguyên tố")
