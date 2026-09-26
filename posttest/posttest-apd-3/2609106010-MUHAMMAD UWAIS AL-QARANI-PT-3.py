nama = input("Masukkan Nama Pembeli: ")
umur = int(input("Masukkan Umur Pembeli: "))

if umur < 13:
    print("Mohon maaf, anda belum cukup umur untuk menonton.")
else:
    print("\n--- Pilihan Tiket: Reguler, Premium, VIP ---")
    jenis_tiket = input("Masukkan Jenis Tiket: ").lower()
    status_member = input("Apakah anda Member? (Ya/Tidak): ").lower()

    if jenis_tiket == "reguler":
        harga_tiket = 50000
    elif jenis_tiket == "premium":
        harga_tiket = 75000
    elif jenis_tiket == "vip":
        harga_tiket = 100000
    else:
        harga_tiket = 0 # nandain kalau inputnya gak valid.

    if harga_tiket == 0:
        print("Peringatan: Jenis tiket tidak valid! Transaksi dibatalkan.")
    else:
        diskon = 0.20 if status_member == "ya" else 0
        biaya_admin = 0 if status_member == "ya" else 2000

        nominal_diskon = int(harga_tiket * diskon)
        total_bayar = int(harga_tiket - nominal_diskon + biaya_admin)

        print(f"\nTotal yang harus dibayar: Rp {total_bayar}")
        uang_bayar = int(input("Masukkan Nominal Pembayaran: Rp "))

        if uang_bayar < total_bayar:
            print(f"Peringatan: Uang bayar kurang! Total yang harus dibayar adalah Rp{total_bayar}.")
        else:
            kembalian = uang_bayar - total_bayar
            
            print(f"""
==================================
          STRUK BIOSKOP           
==================================
Nama Pembeli  : {nama}
Umur          : {umur} Tahun
Jenis Tiket   : {jenis_tiket.capitalize()}
Status Member : {status_member.capitalize()}
Harga Tiket   : Rp {harga_tiket}
Diskon        : Rp {nominal_diskon}
Biaya Admin   : Rp {biaya_admin}
Total Bayar   : Rp {total_bayar}
Pembayaran    : Rp {uang_bayar}
Kembalian     : Rp {kembalian}
==================================""")