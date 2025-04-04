def main():
    try:
        a = int(input("Nhập vào số thập phân cần đổi: "))
        if a < 0:
            raise ValueError("Số thập phân không được là số âm.")
    except ValueError as error:
        print("Số không hợp lệ:", error)
    else:
        kq = bin(a)[2:]
        print("Kết quả là: ", kq)


if __name__ == "__main__":
    main()
