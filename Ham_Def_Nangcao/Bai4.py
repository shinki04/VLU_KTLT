"""
4.	Viết hàm hiện thực hàm map trong python
 (yêu cầu dùng hàm lambda bên trong hàm chính)
Gợi ý: Hàm nhận vào 1 function (ví dụ hàm mũ 2) và 1 list,
 áp dụng hàm mũ 2 này lên từng phần tử trong list
"""


def nhap_ds(a):
    ds = []
    for i in range(1, a + 1):
        b = int(input(f"Giá trị phần tử thứ {i} là: "))
        ds.append(b)
    return ds


a = int(input("Số phần tử có trong danh sách là: "))
ds = nhap_ds(a)
print("ds da nhap", ds)


#* Các bạn lên gg tìm hiểu map() và tại sao phải list(kq)
def mu_ds(fun, ds):
    kq = map(fun, ds)
    return list(kq)


#* Hàm ẩn danh
fun = lambda a: a**2
print("ds sau khi mũ 2", mu_ds(fun, ds))
