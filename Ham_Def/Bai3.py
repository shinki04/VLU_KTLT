"""
3.	Viết hàm với tham số truyền vào là nhiệt độ F, trả về kết quả nhiệt độ C theo công thức. Sử dụng hàm vừa cài đặt, nhập vào độ F và in ra màn hình độ C.

Gợi ý: C = 5*(F - 32) / 9, với C: nhiệt độ C; F: nhiệt độ F
VD: Hàm nhận tham số nhiệt độ F và trả về “Nhiệt độ C là…” theo công thức
"""


def kiemtra(F):
    C = 5 * (F - 32) / 9
    return C


F = float(input("Nhập F: "))
print("Đổi sang độ C là: %.1F" % kiemtra(F))

# * Muốn hiểu %.1F thì các bạn tìm "decimal formating python 3" để hiểu thêm
