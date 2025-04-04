# 2.	Viết hàm tìm giá trị x có tồn tại trong danh sách hay không?
# Ví dụ: Hàm nhận vào tham số là 1 danh sách [1, 4, 7, 5, 8, 9] và 1 số cần tìm là 7.
#  trả về True và in “Có trong danh sách”

def tim_gia_tri_trong_danh_sach(danh_sach, x):
    if x in danh_sach:
        return True
    else:
        return False


n = int(input("Nhập số phần tử của mảng: "))
arr = []

for i in range(n):
    phan_tu = int(input("Nhập phần tử thứ {} của mảng: ".format(i + 1)))
    arr.append(phan_tu)

print("Mảng đã nhập:", arr)


x = int(input("Nhập số cần tìm: "))

#* Ta có thể ghi điều kiện như này thay vì "if tim_gia_tri_trong_danh_sach(arr, x) is True"
if tim_gia_tri_trong_danh_sach(arr, x):
    print("Có trong danh sách")
else:
    print("Không có trong danh sách")
