import congthuc as ct


def tinhtoan():
    a = int(input("Nhập a= "))
    b = int(input("Nhập b= "))
    cong = ct.add(a, b)
    tru = ct.sub(a, b)
    nhan = ct.multiple(a, b)
    chia = ct.divide(a, b)
    cb2 = ct.can_bac_hai(a)
    print("Cộng: ", cong)
    print("Trừ: ", tru)
    print("Nhân: ", nhan)
    print("Chia: ", chia)
    print("Căn bậc 2: %.1f" % cb2)


tinhtoan()
