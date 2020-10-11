nama_buah = []

def tambah_nama_buah(nama):
    nama_buah.append(nama)
    for buah in nama_buah:
        print(buah)
    print("_______")

tambah_nama_buah("Jeruk")
tambah_nama_buah("Apel")
tambah_nama_buah("Melon")
tambah_nama_buah("Pisang")

def total(x, y):
    total = x * y
    return total

def total_buah_sisa():
    return 20

jumlah = total(3, 2)
print(jumlah)

total_buah = len(nama_buah) + total_buah_sisa()
print(total_buah)