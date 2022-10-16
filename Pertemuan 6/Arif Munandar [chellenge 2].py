print("+" *44)
print("+ Program Mengubah Angka Menjadi Terbilang +")
print("+"*44)


def Terbilang(bil):
    angka = ["Nol","Satu","Dua","Tiga","Empat","Lima","Enam","Tujuh","Delapan",
             "Sembilan", "Sepuluh", "Sebelas"]
    result = " "
    n = int(bil)
    if n >= 0 and n <= 11:
        result = result + angka[n]
    elif n < 20:
        result = Terbilang(n % 10) + " Belas"
    elif n < 100:
        result = Terbilang(n/10) + " Puluh" + Terbilang(n % 10)
    else:
        result = "Melebihi Batas dan Melampauinya"
    return result


if __name__ == '__main__':
    bil = input("Masukkan angka (0-99) : ")
    tbl = Terbilang(bil)
    print(tbl)
