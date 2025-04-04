def fibonacci(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    elif n < 0:
        return "không hợp lệ"
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("nhập N: "))
print(fibonacci(n))

'''
Các step nó chạy :
f0 = 0
f1 = 1
f2 = (f2-1) + f(2-2) = f1 + f0 = 1 + 0 = 1
f3 = (f3-1) + f(3-2) = f2 + f1 = 1 + 1 = 2
f4 = (f4-1) + f(4-2) = f3 + f2 = 2 + 1 = 3

'''
