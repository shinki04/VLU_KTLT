import math

try:
    a = float(input("Nhập vào a: "))
    b = float(input("Nhập vào b: "))
    c = float(input("Nhập vào c: "))
    if a == 0:
        raise ValueError("Đây là phương trình bậc 1.")
except ValueError as e:
    print("Lỗi giá trị",e)
else:
    delta = (b**2) - (4 * a * c)
    can_delta = math.sqrt(delta)
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"Phương trình có nghiệm kép x1=x2={x}")
    else:
        x1 = (-b + can_delta) / (2 * a)
        x2 = (-b - can_delta) / (2 * a)
        print(f"Phương trình có 2 nghiệm x1 = {x1} và x2 = {x2}")
