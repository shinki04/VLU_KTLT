def thongtin(ten, tuoi):
    f = open("data6.txt", "a", encoding="utf-8")
    f.write(f"tên: {ten}, tuổi: {tuoi}\n")
    f = open("data6.txt", "r", encoding="utf-8")
    nd = f.read()
    print(nd)
    f.close()


if __name__ == "__main__":
    ten = input("nhập tên: ")
    tuoi = int(input("nhập tuổi: "))
    thongtin(ten, tuoi)
