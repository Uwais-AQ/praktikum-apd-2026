# nama = ["Andi", 55, "Budi", "Caca", "Dedi", "Eka"]
# Perintah modifikasi list
# nama.append = tambhkan data di paling akhir
# nama.extend = 
# nama.insert = menambahkan data di index tertentu
# modifikasi juga bisa pakai slicing
######## Cara menghapus data di list
# nama.remove = menghapus data berdasarkan nilai
# nama.pop = menghapus data berdasarkan index
# nama.clear = menghapus semua data


# bab5_menara.py
# Penjelajah Menara Berputar


# 1. while: energi berkurang tiap langkah naik
energi = 10
while energi > 0:
    print("Energi tersisa:", energi)
    energi = energi - 3
print("Energi habis. Istirahat dulu.")


# 2. nested loop + continue + break: periksa lantai dan kamar
for lantai in range(1, 4):
    for kamar in range(1, 4):
        if kamar == 2:
            continue
        if lantai == 2 and kamar == 1:
            print("Tangga ditemukan di lantai", lantai, "kamar", kamar)
            break
        print("Memeriksa lantai", lantai, "kamar", kamar)
