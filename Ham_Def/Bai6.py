"""
6.	Viết hàm với tham số truyền vào là một năm và trả về kết quả năm đó là năm Nhuận hay không?
Gợi ý: Những năm dương lịch nào chia hết cho 4 thì năm đó là năm nhuận. Ví dụ: 2016 chia hết cho 4 nên năm 2016 là năm nhuận. Ngoài ra, với những năm tròn thế kỷ (những năm có 2 số cuối là số 0) thì các bạn lấy số năm chia cho 400, nếu chia hết thì năm đó là năm có nhuận  
Ví dụ: Hàm nhận vào tham số là năm 2023, kết quả trả về là “Không phải năm nhuận”

"""


def namnhuan(y):
    if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
        return "Năm Nhuận"
    else:
        return "Năm không nhuận"


y = int(input("Nhập số năm: "))

#* Chỗ này ta phải print(function) bởi vì function return ko có xuất ra màn hình , các bạn có thể xoá print để tự xem <3
print(namnhuan(y))

# Cách 2 
'''
Khi hàm return về ta có thể lưu giá trị vào 1 biến
Các bạn có thể thử 

kq = namnhuan(y)
print(kq)

'''
