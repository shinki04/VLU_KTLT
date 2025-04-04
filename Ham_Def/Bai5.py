"""
5.	Viết hàm tính diện tích, chu vi hình tròn với tham số truyền vào là bán kính
Gợi ý: Công thức tính diện tích hình tròn:
S=PI*R*R
C = 2*PI*R
Ví dụ: 	Hàm nhận tham số bán kính là 3, trả về kết quả là “Diện tích: …” và “Chu vi…” theo công thức tương ứng.

"""


def hinhtron(r):
    PI = 3.14
    S = PI * r * r
    C = 2 * PI * r
    return S, C


r = int(input("Nhập vào bán kính: "))

# * Các bạn có thể tự ngẫm bài này theo cách của riêng mình

Dientich = hinhtron(r)[0]
Chuvi = hinhtron(r)[1]
print(f"Chu vi : {Chuvi} , Diện tích : {Dientich} ")
