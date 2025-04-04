def chuyenDoiNhiPhan(n):
    try:
        n = int(n) 
        if n < 0:
            return "Lỗi: Số phải không âm."
        if n in (0, 1):
            return str(n)
        return chuyenDoiNhiPhan(n // 2) + str(n % 2)
    except:
        return "Lỗi: Đầu vào không hợp lệ."

print(chuyenDoiNhiPhan(10))   # Output: "1010"
print(chuyenDoiNhiPhan(0))    # Output: "0"
print(chuyenDoiNhiPhan(-5))   # Output: "Lỗi: Số phải không âm."
print(chuyenDoiNhiPhan("abc")) # Output: "Lỗi: Đầu vào không hợp lệ."
