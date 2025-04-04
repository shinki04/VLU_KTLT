def sumDigits(n):
    if n == 0:
        return 0
    return n % 10 + sumDigits(n // 10)

n = int(input("Nhập số nguyên dương n: "))

if n < 0:
    print("Vui lòng nhập số nguyên dương.")
else:
    print(f"Kết quả = {sumDigits(n)}")
