def demso(n):
    if n < 10:
        return 1
    elif n < 0:
        return "giá trị không hợp lệ"
    else:
        return 1 + demso(n//10)

n = int(input("nhập N: "))
print(demso(n))    

#* Bài này dễ hơn nên tự ngẫm nhé