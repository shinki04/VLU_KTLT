try:
    a = int(input("Nhập vào số nguyên a: "))
    b = int(input("Nhập vào số nguyên b: "))
except ValueError:
    print("Không phải là số nguyên.")
else:
    sum = a + b
    print(f"Tổng 2 số là : {sum}")