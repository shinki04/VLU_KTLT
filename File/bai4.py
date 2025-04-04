import os


def vietsonguyen(taptin):

    f = open(taptin, "w")
    for so in range(1, 11):
        f.write(f"{str(so)}\n")
    f.close()


if __name__ == "__main__":
    taptin = input("nhập tên file: ")
    vietsonguyen(taptin)
