teori = float(input("Masukkan Nilai Ujian Teori Anda: "))
praktek = float(input("Masukkan Nilai Ujian Praktek Anda: "))
nilai_minimum = 70.0

if teori >= nilai_minimum and praktek >= nilai_minimum:
    print("Selamat, anda lulus!")
elif teori >= nilai_minimum and praktek < nilai_minimum:
    print("Anda harus mengulang ujian praktek.")
elif teori < nilai_minimum and praktek >= nilai_minimum:
    print("Anda harus mengulang ujian teori.")
else:
    print("Anda harus mengulang ujian teori dan praktek.")
