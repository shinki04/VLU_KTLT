'''
Nhập 3 số a,b,c - tìm số lớn nhất
'''

def solonnhat(a, b, c):
    if a > b and a > c:
        return a
    elif b > c and b > a:
        return b
    else:
        return c


a = int(input("Nhập vào số nguyên a: "))
b = int(input("Nhập vào số nguyên b: "))
c = int(input("Nhập vào số nguyên c: "))
sln = solonnhat(a, b, c)
print(f'Số lớn nhất trong 3 số {a},{b},{c} là : {sln}')
