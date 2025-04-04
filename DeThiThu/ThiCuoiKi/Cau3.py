import os


def handleFile():
    file_name = input("Nhập tên tập tin: ")

    if os.path.exists(file_name):
        print(f"Nội dung của tập tin {file_name} là:")
        with open(file_name, 'r', encoding='utf-8') as file:
            print(file.read())
    else:
        print("Chưa có tập tin, tạo tập tin mới...")
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write("")  # Tạo file rỗng
        print(f"Đã tạo tập tin {file_name} thành công.")


handleFile()


def sumOddInFile(file_name):
    total = 0

    try:
        with open(file_name, 'r', encoding='utf-8') as file:

            for lines in file:
                line = lines.split()
                print(line)  # Nếu các bạn muốn kiểm tra thì uncomment dòng này
                for char in line:
                    try:
                        so = int(char)
                        if so % 2 != 0:
                            total += so
                    except ValueError:
                        pass

        print(f"Tổng các số lẻ có trong file là: {total}")

    except FileNotFoundError:
        print(f"Tập tin {file_name} không tồn tại!")


# Gọi hàm để tính tổng số lẻ trong test.txt
sumOddInFile("test.txt")
