''' 5.	Bài tập về hàm với đối số hỗn hợp (list và dictionary): 
viết 1 hàm với đối số truyền vào là 1 list và 1 dictionary, trong đó list là danh sách các số nguyên bất kỳ (cho trước) 
và dictionary là các kết quả thống kê của list (tổng (sum), trung bình (average), số nhỏ nhất (min), số lớn nhất (max))

'''
def doiso_honhop(list, dict):
    def tinh_tong():
        tong = 0
        for i in list:
            tong = tong + i
        return tong

    def tinh_tb():
        tb = tinh_tong() / len(list)
        return round(tb, 2)

    def tim_min():
        min = list[0]
        for i in list:
            if i < min:
                min = i
        return min

    def tim_max():
        max = list[0]
        for i in list:
            if i > max:
                max = i
        return max

    kqtong = tinh_tong()
    kqTB = tinh_tb()
    kmin = tim_min()
    kmax = tim_max()
    dict = {"sum": kqtong, "average": kqTB, "min": kmin, "max": kmax}
    return dict

#* stats = dict() là để khai báo stats là 1 dictionnary rỗng 
stats = dict()
list = [5, 4, 3, 7]
print("ket qua: ", doiso_honhop(list, dict))
