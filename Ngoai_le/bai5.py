import math


def tamgiac():
    try:
        a = float(input("Nhập vào độ dài cạnh a: "))
        b = float(input("Nhập vào độ dài cạnh b: "))
        c = float(input("Nhập vào độ dài cạnh c: "))
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Độ dài cạnh phải lơn hơn 0.")
    except ValueError as error:
        print("Lỗi giá trị", error)
    else:
        if a + b > c and b + c > a and a + c > b:
            cv = a + b + c
            p = cv / 2
            dt = math.sqrt(p * (p - a) * (p - b) * (p - c))
            print(f"Chu vi hình tam giác là: {round(cv,2)}")
            print(f"Diện tích hình tam giác là: {round(dt,2)}")
        else:
            print("Đây không phải độ dài 3 cạnh tam giác")


if __name__ == "__main__":
    tamgiac()
