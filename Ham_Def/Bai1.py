"""
1.	Viết hàm kiểm tra một số là số âm hay dương 
Gợi ý: Yêu cầu nhập vào số nguyên a trả về kết quả là True (nếu a là số dương)/False (nếu a là số âm)
VD: Hàm nhận tham số a = 2, kết quả trả về là True, và in ra “Số dương”
"""

# * Return sẽ trả về giá trị rồi ngưng chạy function (hàm) ngay thời điểm đó


def kiemtrasoduong(a):
    if a > 0:
        return True
    else:
        return False


a = int(input("Nhap so nguyen a: "))

if kiemtrasoduong(a) is True:
    print("Số dương")
else:
    print("Số âm")
