# Cau A
def nhap_tt():
    while True:
        so_p = input("Nhap so hieu phong:")
        if so_p == "":
            print("Loi, nhap lai so hieu phong: ")
            continue
        else:
            break
    while True:
        so_htn = input("Nhap so hieu toa nha:")
        if so_htn == "":
            print("Loi,nhap lai so hieu toa nha : ")
            continue
        else:
            break
    while True:
        ten_cn = input("Nhap ten chu nha:")
        if ten_cn == "":
            print("Loi, nhap lai ten chu nha : ")
            continue
        else:
            break
    while True:
        so_kw = int(input("Nhap so kw dien tieu thu:"))
        if so_kw < 0:
            print("Loi, nhap lai so kw dien tieu thu  : ")
            continue
        else:
            break
    return {
        "so_hieu_phong": so_p,
        "so_hieu_toa_nha": so_htn,
        "ten_chu_nha": ten_cn,
        "so_dien_tieu_thu": so_kw,
    }


# Cau B
def tiendien(so_kw):
    if so_kw <= 100:
        tien = so_kw * 1450
    elif 101 <= so_kw <= 150:
        tien = 100 * 1450 + (so_kw - 100) * 1750
    elif 151 <= so_kw <= 250:
        tien = 100 * 1450 + 50 * 1750 + (so_kw - 150) * 2000
    else:
        tien = 100 * 1450 + 50 * 1750 + 200 * 2000 + (so_kw - 250) * 2500
    # Tien thue
    tienthue = tien * 0.1
    return tien + tienthue


# Cau C
def ds_td(dshgd):
    print("Toa nha\t Phong\tTen chu nha\t So dien tieu thu\t So tien dien phai tra")
    for i in dshgd:
        print(
            f"toa nha:{i['so_hieu_toa_nha']}\tphong:{i['so_hieu_phong']}\tten:{i['ten_chu_nha']}\tSo  dien tieu thu:{i['so_dien_tieu_thu']}\t so tien phai tra:{tiendien(i['so_dien_tieu_thu'])}\n"
        )


# Cau D
def ghi_thong_tin_vao_file(dshgd):
    for i in dshgd:
        so_kw = i["so_dien_tieu_thu"]
        tien_phai_tra = tiendien(so_kw)
        file = f"{i['so_hieu_toa_nha']}.txt"
        f = open(file, "a")
        f.write(
            f"phong:{i['so_hieu_phong']}\tten:{i['ten_chu_nha']}\tso dien tieu thu:{so_kw}\ttien dien phai tra{tien_phai_tra}\n"
        )
    f.close()


def main():
    ds = []
    while True:
        ho_gd = nhap_tt()
        ds.append(ho_gd)
        ds_td(ds)
        ghi_thong_tin_vao_file(ds)
        while True:
            xac_nhan = input("Nhan c de thoat, nhan b de tiep tuc: ")
            if xac_nhan == "b":
                break
            elif xac_nhan == "c":
                return
            else:
                print("Nhap b hoac c")


if __name__ == "__main__":
    main()
