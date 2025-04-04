class NhanVien:
    def __init__(self, ten="", tuoi="", diachi="", tienluong=0, tongsogiolam=0):
        self.ten = ten
        self.tuoi = tuoi
        self.diachi = diachi
        self.tienluong = tienluong
        self.tongsogiolam = tongsogiolam

    def input_info(self):
        self.ten = input("Nhap ten: ")
        self.tuoi = int(input("Nhap tuoi: "))
        self.diachi = input("Nhap dia chi: ")
        self.tienluong = int(input("Nhap tien luong: "))
        self.tongsogiolam = int(input("Nhap tong so gio lam: "))

    def print_info(self):
        print("Thong tin nhan vien: ")
        print("Ten: ", self.ten)
        print("Tuoi", self.tuoi)
        print("Dia chi: ", self.diachi)
        print("Tien luong: ", self.tienluong)
        print("Tong so gio lam: ", self.tongsogiolam)

    def tinhthuong(self):
        if self.tongsogiolam >= 200:
            return self.tienluong * 0.2
        elif 100 <= self.tongsogiolam < 200:
            return self.tienluong * 0.1
        else:
            return 0


if __name__ == "__main__":
    tinh = NhanVien()
    tinh.input_info()
    tinh.print_info()
    print("Tong tien thuong: ", tinh.tinhthuong())
    thuong = tinh.tinhthuong()
    print("Tong tien luong va tien thuong", tinh.tienluong + thuong)
