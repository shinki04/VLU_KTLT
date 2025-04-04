import Bai3.hinhhoc.hinhchunhat as cthcn
import Bai3.hinhhoc.hinhtron as ctht
import Bai3.hinhhoc.tamgiac as cttg
#* Các bạn có nhiều cách để gọi
# from Bai3.hinhhoc.hinhchunhat import*
# from Bai3.hinhhoc.tamgiac import*
# from Bai3.hinhhoc.hinhtron import*


print("Bạn muốn tính hình gì")
n = int(input("1:Hình chữ nhật,2:Hình tam giác,3:Hình tròn : "))
if n == 1:
    # Gọi chu vi và diện tích hình chữ nhật
    print("Hình chữ nhật")
    a = float(input("Nhập chiều dài: "))
    b = float(input("Nhập chiều rộng: "))
    cvhcn = cthcn.cv_chunhat(a, b)
    dthcn = cthcn.dt_chunhat(a, b)
    print("Chu vi hình chữ nhật là: ", cvhcn)
    print("Diện tích hình chữ nhật: ", dthcn)
elif n == 2:
    # Gọi chu vi và diện tích hình tam giác
    print("Hình tam giác")
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))
    chuvi = cttg.cv_tamgiac(a, b, c)
    h = float(input("Nhập chiều cao: "))
    dientich = cttg.dt_tamgiac(a, h)
    print("Chu vi tam giác là: ", chuvi)
    print("Diện tích tam giác: ", dientich)
elif n == 3:
    # Gọi chu vi và diện tích hình tròn
    print("Hình tròn")
    R = float(input("Nhập đường kính: "))
    cvht = ctht.cv_hinhtron(R)
    dtht = ctht.dt_hinhtron(R)
    print("Chu vi hình tròn là: ", cvht)

    print("Diện tích hình tròn là: ", dtht)
