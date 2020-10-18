daftar_kontak = []
def kembali_ke_menu():
    tampilkan_menu()

def Daftar_kontak(daftar_kontak):
    print("Daftar kontak:")
    for kontak in daftar_kontak:
        print("Nama: {}".format(kontak["Nama"]))
        print("No Telepon: {}".format(kontak["Telepon"]))

def Tambah_kontak():
    Nama = input("Nama: ")
    Telepon = input("Telepon: ")
    kontak = {
        "Nama" : Nama,
        "Telepon" : Telepon
    }
    print("Kontak berhasil ditambahkan")
    return kontak

def tampilkan_menu():
    print("Selamat datang!")
    print("--- Menu ---")
    print(" 1. Daftar Kontak")
    print(" 2. Tambah Kontak")
    print(" 3. Keluar")
    Menu = int(input("Pilih Menu: "))
    if(Menu == 1):
        Daftar_kontak(daftar_kontak)
    elif(Menu == 2):
        kontak = Tambah_kontak()
        daftar_kontak.append(kontak)
    elif(Menu == 3):
        print("Program selesai, sampai jumpa!")
        exit()
    else:
        print("Menu tidak tersedia")

if __name__ == "__main__":
    while True:
        tampilkan_menu()
