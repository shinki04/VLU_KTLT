import os


def tap_tin(taptin_1, taptin_2):
    if os.path.exists(taptin_1):
        f = open(taptin_1, "r")
        w = open(taptin_2, "w")
        stt = 1
        for dong in f:
            w.write(f"{str(stt)}. {dong}\n")
            stt = stt + 1

        #! Nhớ đóng file
        f.close()
        w.close()
    else:
        print("không có file này.")


if __name__ == "__main__":
    taptin_1 = input("nhập vào tập tin nguòn: ")
    taptin_2 = input("nhập vào tập tin đích: ")
    print(tap_tin(taptin_1, taptin_2))
