pelanggan = {
    "nama" : "Andy",
    "umur" : 30
}

print("Nama: {}".format(pelanggan["nama"]))
print("Umur: {}".format(pelanggan["umur"]))

pelanggan["umur"] = 22

pelanggan_2 = {
    "nama" : "Rizqy",
    "umur" : 33
}


print("Nama: {}".format(pelanggan["nama"]))
print("Umur: {}".format(pelanggan["umur"]))

for x in pelanggan:
    print(x)
    print(pelanggan[x])

daftar_pelanggan = []
daftar_pelanggan.append(pelanggan)
daftar_pelanggan.append(pelanggan_2)

for pelanggan in daftar_pelanggan:
    print("Nama: {}".format(pelanggan["nama"]))
    print("Umur: {}".format(pelanggan["umur"]))