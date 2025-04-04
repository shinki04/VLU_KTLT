class NhanVien:
    def __init__(self, manv="", ten_nv="", ngay_sinh="", so_ngaycong=0, luong=0):
        """Phương thức khởi tạo nhân viên"""
        self.manv = manv
        self.ten_nv = ten_nv
        self.ngay_sinh = ngay_sinh
        self.so_ngaycong = so_ngaycong
        self.luong = luong

    def input_info(self):
        """Nhập thông tin nhân viên"""
        self.manv = input("Nhập Mã Nhân Viên: ")

        while True:
            ten_nv = input("Nhập Tên Nhân Viên (bắt đầu bằng L hoặc H): ")
            if ten_nv and (ten_nv[0] == 'L' or ten_nv[0] == 'H'):
                self.ten_nv = ten_nv
                break
            print("Tên nhân viên phải bắt đầu bằng chữ 'L' hoặc 'H'!")

        self.ngay_sinh = input("Nhập Ngày Sinh (dd/mm/yyyy): ")

        while True:
            try:
                so_ngaycong = int(input("Nhập Số Ngày Công: "))
                if so_ngaycong >= 0:
                    self.so_ngaycong = so_ngaycong
                    break
                else:
                    print("Số ngày công phải là số không âm!")
            except ValueError:
                print("Vui lòng nhập số hợp lệ!")

        while True:
            try:
                luong = int(input("Nhập Lương (lớn hơn 3.000.000): "))
                if luong > 3000000:
                    self.luong = luong
                    break
                else:
                    print("Lương phải lớn hơn 3.000.000!")
            except ValueError:
                print("Vui lòng nhập số hợp lệ!")

    def show_info(self):
        """Xuất thông tin nhân viên"""
        print("\nThông tin Nhân Viên:")
        print(f"Mã Nhân Viên: {self.manv}")
        print(f"Tên Nhân Viên: {self.ten_nv}")
        print(f"Ngày Sinh: {self.ngay_sinh}")
        print(f"Số Ngày Công: {self.so_ngaycong}")
        # ===== Nó là định dạng số, các bạn có thể đọc thêm =====
        # https://www.raymondcamden.com/2023/01/05/short-number-formatting-in-python
        # https://queirozf.com/entries/python-number-formatting-examples
        
        print(f"Lương: {self.luong:,} VND")
        print(f"Thưởng: {self.reward():,} VND")

    def reward(self):
        """Tính thưởng cho nhân viên"""
        if self.so_ngaycong > 25:
            return self.luong * 0.1  # Thưởng 10% lương
        return 0


nv = NhanVien()
nv.input_info()
nv.show_info()
