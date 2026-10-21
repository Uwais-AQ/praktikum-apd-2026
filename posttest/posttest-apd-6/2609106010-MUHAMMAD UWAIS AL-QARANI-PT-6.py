import os

# ==================
# INISIALISASI DATA 
# ==================
admin_akun = ("admin_gudang", "admin123") 

staff_akun = {
    "budi_staff": "pass123",
    "siti_staff": "pass321"
}
inventaris = {
    "001": {
        "nama": "Meja tanpa kaki", 
        "kategori": "Furnitur", 
        "harga": 450000, 
        "stok": 25
            },
    "002": {
        "nama": "Kursi roda bertenaga kuda", 
        "kategori": "Furnitur", 
        "harga": 850000, 
        "stok": 10
        },
    "003": {
        "nama": "Lampu gantung mahasiswa", 
        "kategori": "Aksesoris", 
        "harga": 150000, 
        "stok": 50
        }
}

# ====================
# SISTEM GERBANG UTAMA
# ====================
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
=== SISTEM INVENTARIS GUDANG IKEA ===
1. Login (Admin / Staff)
2. Register Akun Staff
3. Keluar Program
=====================================
""")
    menu_awal = input("Pilih menu (1/2/3): ")

    if menu_awal == '1':
        print("\n--- LOGIN TOWER ---")
        in_user = input("Masukkan Username: ")
        in_pass = input("Masukkan Password: ")
        
        role_aktif = ""
        user_aktif = ""
        
        # Cek Login Admin
        if in_user == admin_akun[0] and in_pass == admin_akun[1]:
            role_aktif = "Admin"
            user_aktif = in_user
            print(f"Login berhasil! Selamat datang Admin {user_aktif}.")
            input("Tekan Enter untuk melanjutkan...")
            
            # ==========
            # MENU ADMIN
            # ==========
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"""
=== DASHBOARD ADMIN: {user_aktif} ===
1. Tambah Barang Baru 
2. Lihat Semua Barang 
3. Update Harga & Stok
4. Hapus Barang 
5. Kelola Akun Staff 
6. Ubah Profil Admin
7. Logout
=====================================
                """)
                pilih_admin = input("Pilih menu (1-7): ")

                if pilih_admin == '1':
                    print("\n--- TAMBAH BARANG BARU ---")
                    id_brg = input("Masukkan ID Barang: ")
                    
                    if id_brg in inventaris:
                        print("GAGAL! ID Barang sudah terdaftar di sistem.")
                    else:
                        nama_brg = input("Masukkan Nama Barang: ")
                        kategori = input("Masukkan Kategori: ")
                        harga_brg = input("Masukkan Harga (Hanya angka): ")
                        stok_brg = input("Masukkan Stok (Hanya angka): ")
                        
                        if harga_brg.isdigit() and stok_brg.isdigit():
                            inventaris[id_brg] = {
                                "nama": nama_brg,
                                "kategori": kategori,
                                "harga": int(harga_brg),
                                "stok": int(stok_brg)
                            }
                            print(f"Barang {nama_brg} berhasil ditambahkan!")
                        else:
                            print("GAGAL! Harga dan Stok wajib angka mutlak.")
                    input("Tekan Enter untuk kembali...")

                elif pilih_admin == '2':
                    print("\n--- DAFTAR BARANG ---")
                    if len(inventaris) == 0:
                        print("Gudang kosong.")
                    else:
                        for key_id, detail in inventaris.items():
                            print(f"[{key_id}] {detail['nama']} | Kategori: {detail['kategori']} | Harga: Rp{detail['harga']} | Stok: {detail['stok']}")
                    input("Tekan Enter untuk kembali...")

                elif pilih_admin == '3':
                    print("\n--- UPDATE HARGA & STOK ---")
                    if len(inventaris) == 0:
                        print("Gudang kosong.")
                    else:
                        for key_id, detail in inventaris.items():
                            print(f"[{key_id}] {detail['nama']} (Stok: {detail['stok']})")

                        id_update = input("Masukkan ID Barang yang ingin di-update: ")
                        
                        if id_update in inventaris:
                            hrg_baru = input("Harga Baru (Angka): ")
                            stk_baru = input("Stok Baru (Angka): ")
                            if hrg_baru.isdigit() and stk_baru.isdigit():
                                inventaris[id_update]["harga"] = int(hrg_baru)
                                inventaris[id_update]["stok"] = int(stk_baru)
                                print("Data berhasil di-update!")
                            else:
                                print("GAGAL! Input harus angka.")
                        else:
                            print("ID Barang tidak ditemukan.")
                    input("Tekan Enter untuk kembali...")

                elif pilih_admin == '4':
                    print("\n--- HAPUS BARANG ---")
                    for key_id, detail in inventaris.items():
                        print(f"[{key_id}] {detail['nama']}")
                    
                    id_hapus = input("Masukkan ID Barang yang dihapus: ")
                    if id_hapus in inventaris:
                        brg_del = inventaris.pop(id_hapus)
                        print(f"[{id_hapus}] {brg_del['nama']} dihapus dari gudang.")
                    else:
                        print("ID Barang tidak valid/tidak ditemukan.")
                    input("Tekan Enter untuk kembali...")

                elif pilih_admin == '5':
                    print("\n--- HAPUS AKUN STAFF ---")
                    for staff_user in staff_akun.keys():
                        print(f"- {staff_user}")
                    
                    hps_staff = input("Ketik username staff yang ingin dihapus: ")
                    if hps_staff in staff_akun:
                        del staff_akun[hps_staff]
                        print(f"Akun '{hps_staff}' berhasil dihapus!")
                    else:
                        print("Username tidak ditemukan.")
                    input("Tekan Enter untuk kembali...")

                elif pilih_admin == '6':
                    print("\n--- UBAH PROFIL ADMIN ---")
                    new_user = input("Username Admin baru: ")
                    new_pass = input("Password Admin baru: ")
                    admin_akun = (new_user, new_pass)
                    user_aktif = new_user
                    print("Profil Admin diperbarui!")
                    input("Tekan Enter untuk kembali...")

                elif pilih_admin == '7':
                    break 
                else:
                    print("Pilihan tidak valid!")
                    input("Tekan Enter untuk kembali...")

        # Cek Login Staff 
        elif in_user in staff_akun and staff_akun[in_user] == in_pass:
            role_aktif = "Staff"
            user_aktif = in_user
            print(f"Login berhasil! Selamat datang Staff {user_aktif}.")
            input("Tekan Enter untuk melanjutkan...")
            
            # ===================
            # TAHAP 4: MENU STAFF
            # ===================
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"""
=== DASHBOARD STAFF: {user_aktif} ===
1. Lihat Daftar Barang
2. Update Stok Barang
3. Ubah Profil Akun
4. Logout
=====================================
                """)
                pilih_staff = input("Pilih menu (1-4): ")

                if pilih_staff == '1':
                    print("\n--- DAFTAR BARANG ---")
                    if len(inventaris) == 0:
                        print("Gudang kosong.")
                    else:
                        for key_id, detail in inventaris.items():
                            print(f"[{key_id}] {detail['nama']} | Stok: {detail['stok']}")
                    input("Tekan Enter untuk kembali...")

                elif pilih_staff == '2':
                    print("\n--- UPDATE STOK BARANG ---")
                    if len(inventaris) == 0:
                        print("Gudang kosong.")
                    else:
                        for key_id, detail in inventaris.items():
                            print(f"[{key_id}] {detail['nama']} (Stok: {detail['stok']})")
                        
                        id_update = input("Masukkan ID Barang: ")
                        if id_update in inventaris:
                            stk_baru = input("Stok Akhir (Angka): ")
                            if stk_baru.isdigit():
                                inventaris[id_update]["stok"] = int(stk_baru)
                                print("Stok berhasil diperbarui!")
                            else:
                                print("GAGAL! Stok wajib angka.")
                        else:
                            print("ID Barang tidak ditemukan.")
                    input("Tekan Enter untuk kembali...")

                elif pilih_staff == '3':
                    print("\n--- UBAH PROFIL STAFF ---")
                    new_user = input("Username baru: ")
                    new_pass = input("Password baru: ")
                    
                    if new_user == admin_akun[0] or (new_user in staff_akun and new_user != user_aktif):
                        print("Gagal! Username sudah dipakai oleh admin atau staff lain.")
                    else:
                        # Hapus akun lama, buat Key baru
                        del staff_akun[user_aktif]
                        staff_akun[new_user] = new_pass
                        user_aktif = new_user
                        print("Profil berhasil diperbarui!")
                    input("Tekan Enter untuk kembali...")

                elif pilih_staff == '4':
                    break 
                else:
                    print("Pilihan tidak valid!")
                    input("Tekan Enter untuk kembali...")
        else:
            print("Username/Password salah atau tidak terdaftar.")
            input("Tekan Enter untuk kembali...")

    elif menu_awal == '2':
        print("\n--- REGISTER STAFF BARU ---")
        reg_user = input("Masukkan Username baru: ")
        
        if reg_user == admin_akun[0] or reg_user in staff_akun:
            print("Gagal! Username sudah digunakan.")
        else:
            reg_pass = input("Masukkan Password baru: ")
            staff_akun[reg_user] = reg_pass
            print(f"Akun Staff '{reg_user}' berhasil didaftarkan!")
        input("Tekan Enter untuk kembali...")

    elif menu_awal == '3':
        print("Terima kasih telah menggunakan sistem inventaris IKEA!")
        break 

    else:
        print("Pilihan tidak valid! Masukkan angka 1, 2, atau 3.")
        input("Tekan Enter untuk kembali.")