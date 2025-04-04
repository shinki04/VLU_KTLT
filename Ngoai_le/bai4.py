try:
    with open("testfile.txt", "r") as file:
        a = file.read()
        print(a)
except FileNotFoundError as error:
    print("Không có file tồn tại", error)
