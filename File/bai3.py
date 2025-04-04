import os


def tinhtiong(taptin):
    if os.path.exists(taptin):
        f = open(taptin, "r")
        nd = f.read()
        ds = nd.split()
        tong = 0
        d = 0
        for i in ds:
            try:
                so = float(i)
                d = d + 1
                tong = tong + so
            except:
                pass
        print(tong)

        #! Nhớ đóng file
        f.close()
    else:
        print("không có file này.")


if __name__ == "__main__":
    taptin = input("nhập tên file: ")
    tinhtiong(taptin)
