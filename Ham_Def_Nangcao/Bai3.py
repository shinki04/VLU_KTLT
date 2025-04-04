"""3.	Viết hàm sắp xếp mảng tăng dần (yêu cầu: dùng nested function)
Gợi ý: 
-	Viết 1 hàm chính với tham số truyền vào là 1 list
-	Trong hàm chính, viết 1 hàm con để hoán đổi và sắp xếp vị trí các phần tử của list
"""


def nhap_ds(a):
    ds = []
    # * Tại sao a+1 thì các bạn nên tự nghĩ , vđe này dễ lắm , nếu hiểu rõ thì khoẻ về sau cho các bạn
    for i in range(1, a + 1):
        b = int(input(f"Giá trị phần tử thứ {i} là: "))
        ds.append(b)
    return ds


def sapxep_giam(list):

    # * function hoandoi nó sẽ đổi vị trí của 2 số , các bạn có thể tìm hiểu sắp xếp nổi bọt
    def hoandoi(i, j):
        list[i], list[j] = list[j], list[i]

    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] > list[j]:
                hoandoi(i, j)

    return list


a = int(input("Số phần tử có trong danh sách là: "))
ds = nhap_ds(a)
print("ds da nhap", ds)
print("ds sau khi sap xep", sapxep_giam(ds))

# * Giải thích cho function hoandoi
"""
        Nghĩa là :
        list[i] = list[j]
        list[j] = list[i]
        Đó là cách giải thích cho bạn hiểu nhưng chạy code như v sẽ lỗi 
        Ta có thể sử dụng biến khác để lưu trữ tạm giá trị nếu muốn 
        temp = list[i]
        list[i] = list[j]
        list[j] = temp
"""
