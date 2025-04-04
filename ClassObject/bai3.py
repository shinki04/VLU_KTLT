class Student:
    def __init__(self, msv="", dtb=0, tuoi=0, lop=""):
        self.msv = msv
        self.dtb = dtb
        self.tuoi = tuoi
        self.lop = lop

    def input_info(self):
        while True:
            self.msv = input("Nhap ma sinh vien : ")
            if len(self.msv) == 8:
                if "a" <= self.msv <= "z" and self.msv not in range(0, 10):
                    break
            else:
                print("Ma sinh vien phai la 8 ky tu. ")
        while True:
            self.dtb = float(input("Nhap diem trung binh: "))
            if 10 >= self.dtb >= 0:
                break
            else:
                print("Nhap lai diem trung binh phai tu 0 den 10.")
        while True:
            self.tuoi = int(input("Nhap tuoi: "))
            if self.tuoi >= 18:
                break
            else:
                print("Nhap lai tuoi phai lon hon hoac bang 18.")
        while True:
            self.lop = input('Nhap lop phai bat dau bang ky tu "A" hoac ky tu "C": ')
            if self.lop[0] == "A" or self.lop[0] == "C":
                break
            else:
                print('Nhap lai ten lop phai bat dau bang ky tu "A" hoac ky tu "C". ')

    def show_info(self):
        print("Ma sinh vien", self.msv)
        print("Diem trung binh: ", self.dtb)
        print("Tuoi: ", self.tuoi)
        print("Lop", self.lop)

    def hocbong(self):
        if self.dtb >= 8.0:
            return "Sinh vien danh duoc hoc bong"
        else:
            return "Sinh vien khong nhan duoc hoc bong"


if __name__ == "__main__":
    sv = Student()
    sv.input_info()
    sv.show_info()
    print(sv.hocbong())
