"""
Ví dụ: 	Hàm nhận tham số vào là tháng 2, trả về kết quả là “mùa Xuân”.
Từ tháng 1 đến tháng 3: Mùa Xuân
Từ tháng 4 đến tháng 6: Mùa Hạ
Từ tháng 7 đến tháng 9: Mùa Thu
Từ tháng 10 đến tháng 12: Mùa Đông	

"""


def mua(thang):
    if thang in [1, 2, 3]:
        print("Mùa xuân")
    elif thang in [4, 5, 6]:
        print("Mùa hạ")
    elif thang in [7, 8, 9]:
        print("Mùa thu")
    elif thang in [10, 11, 12]:
        print("Mùa đông")
    else:
        print("không có mùa này bạn ơi")


thang = int(input("Nhâp vào một tháng: "))
mua(thang)
