"""
7.	Viết hàm tính số trung bình cộng dãy số trong khoảng [a,b]. 
Gợi ý: Hàm nhận 2 tham số là số nguyên a và b (với điều kiện b > a). Tính tổng các giá trị từ a đến b từ đó tính trung bình cộng trong khoảng [a,b]

"""


def trungbinhcong(a, b):
    
    if a > b:
        return "Tham số không hợp lệ"
    tong = sum(range(a, b + 1))
    so_luong = b - a + 1
    tinh_trung_binh_cong = tong / so_luong
    return tinh_trung_binh_cong


a = int(input("Nhập số bất kì: "))
b = int(input("Nhập số bất kì: "))
print(trungbinhcong(a, b))

#* Như bài trước , bên cạnh print(trungbinhcong(a,b)) ta có thể sài cách khác 
'''
kq = trungbinhcong(a,b)
print(kq)
'''
#! Câu hỏi ở đây sẽ là : Tại sao ta phải dùng biến để lưu giá trị return của function mà không sử dụng tinh_trung_binh_cong để xuất ra màn luôn cho ngắn
'''
trungbinhcong(a,b)
print(tinh_trung_binh_cong)
'''
# Phần này các bạn học kĩ lại về hàm trong slide của trường, phân biệt biến global (toàn cục) và biến nonglobal (cục bộ)
