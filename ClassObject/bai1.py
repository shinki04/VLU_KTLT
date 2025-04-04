class sohoc:
    
    def __init__(self, number1=0, number2=0):
        self.number1 = number1
        self.number2 = number2

#   Method
    def input_info(self):
        self.number1 = float(input("Nhap number1: "))
        self.number2 = float(input("Nhap number2: "))
        

    def print_info(self):
        print("Number1: ", self.number1)
        print("Number2: ", self.number2)

    def addition(self):
       return self.number1 + self.number2

    def subtract(self):
        print("Hieu 2 so la: ", self.number1 - self.number2)

    def multi(self):
        print("Tich 2 so la: ", self.number1 * self.number2)

    def division(self):
        if self.number2 != 0:
            print("Thuong 2 so la: ", self.number1 / self.number2)
        else:
            print("Khong chia duoc cho so 0")


if __name__ == "__main__":
    # tinh = sohoc()
    test = sohoc()
    # tinh.input_info()
    # tinh.print_info()
   
    # tinh.subtract()
    # tinh.multi()
    # tinh.division()
    
    print("Cho nay la test")
    test.input_info()
    test.print_info()
    print("Nhan : " , test.addition() + 4)

    
