def docdulieu(file):
    try:
        f = open(file, "r", encoding="utf-8")
        nd = f.read()
        print(nd)
        f.close()
    except FileNotFoundError:
        print("không tìm thấy file này")


if __name__ == "__main__":
    file = input("nhập tên file: ")
    docdulieu(file)
