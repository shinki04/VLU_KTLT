
#* Bài không sử dụng đệ quy
# def nhi_phan(n):
#     if n==0:
#         return 0 
#     day_np=''
#     while n>0:
#         du=n%2
#         day_np=str(du)+day_np
#         n=n//2 
#     return day_np 

def nhiphan(n):
    if n < 0:
        return "phải là số dương"
    elif n == 0:
        return "0"
    else:
        return nhiphan(n // 2) + str(n % 2)


n = int(input("nhập N: "))
print(nhiphan(n))

'''
Các step nó chạy 
vd n = 10

10//2 = 5 dư 0
5//2 = 2 dư 1
2//2 = 1 dư 0
1//2 = 0 dư 1
0 return 0

Nhị phân lấy từ dưới đếm lên là lấy kq dư từ 1//2 -> 2//2 -> 5//2 -> 10//2 là 1010 

Nếu cảm thấy khó hiểu thì xem gg nhé , xem luôn cách tính nhị phân , từ hệ số 10 về nhị phân (từ dec về bin)
'''