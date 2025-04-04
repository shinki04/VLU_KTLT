"""
1.	Viết hàm kiểm tra một số là số âm hay dương 
Gợi ý: Yêu cầu nhập vào số nguyên a trả về kết quả là True (nếu a là số dương)/False (nếu a là số âm)
VD: Hàm nhận tham số a = 2, kết quả trả về là True, và in ra “Số dương”
"""

def ktraso(so):
    if so > 0 :
        return True
    else :
        return False


a = int(input("Nhap so vao tk kia: "))

if ktraso(a):
    print("So Duong")
else:
    print("So Am")
    
    
# string str = ['a','b','c',....]
# int = [1,2,3,4,5]
# float = [0.0, 0.1,0.2,...]
# sohoc = [2, 3]

