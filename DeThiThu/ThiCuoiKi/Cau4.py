class SinhVien:
    def __init__(self, masv="", ho_ten="", ngay_sinh="", thuong_tru="", dtb=0.0):
        """Phương thức khởi tạo sinh viên"""
        self.masv = masv
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.thuong_tru = thuong_tru
        self.dtb = dtb

    def input_info(self):
        """Nhập thông tin sinh viên"""
        while True:
            masv = input("Nhập MASV (5 ký tự): ")
            if len(masv) == 5:
                self.masv = masv
                break
            print("MASV phải có đúng 5 ký tự!")

        while True:
            ho_ten = input("Nhập Họ và Tên: ")
            if len(ho_ten) !=0 :
                self.ho_ten = ho_ten
                break
            print("Họ tên không được rỗng")
        
        # ===== Các bạn nhớ kiểm tra chuỗi rỗng tương tự =====
        # Nếu các bạn giỏi thì các bạn kiểm tra ngày sinh
        self.ngay_sinh = input("Nhập Ngày Sinh (dd/mm/yyyy): ")
    
        self.thuong_tru = input("Nhập Địa Chỉ Thường Trú: ")

        while True:
            try:
                dtb = float(input("Nhập Điểm Trung Bình (0 - 10): "))
                if 0.0 <= dtb <= 10.0:
                    self.dtb = dtb
                    break
                else:
                    print("DTB phải nằm trong khoảng từ 0 đến 10!")
            except ValueError:
                print("Vui lòng nhập một số hợp lệ!")

    def show_info(self):
        """Xuất thông tin sinh viên"""
        print("\nThông tin sinh viên:")
        print(f"MASV: {self.masv}")
        print(f"Họ và Tên: {self.ho_ten}")
        print(f"Ngày Sinh: {self.ngay_sinh}")
        print(f"Thường Trú: {self.thuong_tru}")
        print(f"Điểm Trung Bình: {self.dtb}")
        print(f"Xếp Loại: {self.rank()}")

    def rank(self):
        """Xếp loại sinh viên dựa trên điểm trung bình"""
        if self.dtb >= 9:
            return "Xuất sắc"
        elif self.dtb >= 8:
            return "Giỏi"
        elif self.dtb >= 7:
            return "Khá"
        elif self.dtb >= 5:
            return "Trung bình"
        else:
            return "Yếu"


sv = SinhVien()
sv.input_info()
sv.show_info()
