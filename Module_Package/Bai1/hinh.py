import hinhhoc

print("Bạn muốn tính hình gì")
n = int(input("1:Hình chữ nhật,2:Hình tam giác,3:Hình tròn : "))

if n == 1:
    # Gọi chu vi và diện tích hình chữ nhật
    print("Hình chữ nhật")
    a = float(input("Nhập chiều dài: "))
    b = float(input("Nhập chiều rộng: "))
    cvhcn = hinhhoc.cv_chunhat(a, b)
    dthcn = hinhhoc.dt_chunhat(a, b)
    print("Chu vi hình chữ nhật là: ", cvhcn)
    print("Diện tích hình chữ nhật: ", dthcn)
    
elif n == 2:
    # Gọi chu vi và diện tích hình tam giác
    print("Hình tam giác")
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))
    chuvi = hinhhoc.cv_tamgiac(a, b, c)
    h = float(input("Nhập chiều cao: "))
    dientich = hinhhoc.dt_tamgiac(a, h)
    print("Chu vi tam giác là: ", chuvi)
    print("Diện tích tam giác: ", dientich)
    
elif n == 3:
    # Gọi chu vi và diện tích hình tròn
    print("Hình tròn")
    r = float(input("Nhập đường kính: "))
    cvht = hinhhoc.cv_hinhtron(r)
    dtht = hinhhoc.dt_hinhtron(r)
    print("Chu vi hình tròn là: ", cvht)
    print("Diện tích hình tròn là: ", dtht)
