
danh_sach=[]
def danhsach(danh_sach):
    a= int(input("nhap so phan tu danh sach: "))
    for i in range (a):
        b = int (input('nhap phan tu vao danh sach: '))
        danh_sach.append(b)
    return danh_sach

def countNumber(lst):
    count =0
    for i in lst :
        if i > 5:
            count+=1
    return count

lst = danhsach(danh_sach)
dem = countNumber(lst)
print(f"Có {dem} phần tử trong list lớn hơn 5")