def S_chan(n):

    if n < 10:
        return 0 if n % 2 != 0 else n
    else:
        if n % 2 != 0:
            return S_chan(n // 10)
        else:
            return n % 10 + S_chan(n // 10)


def S_le(n):
    if n == 0:
        return 0
    elif n % 2 == 1:
        return n % 10 + S_le(n // 10)
    else:
        return S_le(n // 10)

#* Nếu thắc mắc if __name__ là gì thì lên gg sợt nha , hàm này khá qtrong về sau
if __name__ == "__main__":
    n = int(input("Nhập n: "))
    print(f"Tổng chữ số chẵn của {n} là: {S_chan(n)}")
    print(f"Tổng chữ số lẻ của {n} là: {S_le(n)}")
