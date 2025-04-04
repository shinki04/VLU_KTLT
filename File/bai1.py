import os


def kttt(file):
    if os.path.exists(file):
        f = open(file, "r")
        print("nội dung của file là: ", f.read())
        #! Nhớ đóng file
        f.close()
    else:
        print("không có file này")


if __name__ == "__main__":
    file = input("nhập vào tên file: ")
    kttt(file)
