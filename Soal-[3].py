teori = float(input("Masukkan Nilai Ujian Teori Anda: "))
praktek = float(input("Masukkan Nilai Ujian Praktek Anda: "))

if teori >= 70.0 and praktek >= 70.0:
    print("Selamat, anda lulus!")
elif teori >= 70.0 and praktek < 70.0:
    print("Anda harus mengulang ujian praktek.")
elif teori < 70.0 and praktek >= 70.0:
    print("Anda harus mengulang ujian teori.")
else:
    print("Anda harus mengulang ujian teori dan praktek.")