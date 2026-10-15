import os

# ===========================
# Bagian 1: INISIALISASI DATA
#============================
admin_akun = ("admin_gudang", "admin123") 
staff_akun = [
    ["budi", "pass123"],
    ["siti", "pass321"]
] 
inventaris = [
    ["001", "Meja Belajar LINNMON", "Furnitur", 450000, 25],
    ["002", "Kursi Kerja FLINTAN", "Furnitur", 850000, 10],
    ["003", "Lampu Meja TERTIAL", "Aksesoris", 150000, 50]
] 

# ==============================
# Bagian 2: SISTEM GERBANG UTAMA
# ==============================
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
=== SISTEM INVENTARIS GUDANG IKEA ===
1. Login (Admin / Staff)
2. Register (Khusus Akun Staff)
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
        
        # jika yang login admin
        if in_user == admin_akun[0] and in_pass == admin_akun[1]:
            role_aktif = "Admin"
            user_aktif = in_user
            print(f"Login berhasil! Selamat datang Admin {user_aktif}.")
            input("Tekan Enter untuk melanjutkan...")
            
            # ==========================================
            # Bagian 3: MENU ADMIN
            # ==========================================
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
                    id_brg = input("Masukkan 3 Digit ID Barang: (ex: 004) ")
                    nama_brg = input("Masukkan Nama Barang: ")
                    kategori = input("Masukkan Kategori: ")
                    harga_brg = input("Masukkan Harga (Hanya angka): ")
                    stok_brg = input("Masukkan Stok (Hanya angka): ")
                    
                    if harga_brg.isdigit() and stok_brg.isdigit():
                        inventaris.append([id_brg, nama_brg, kategori, int(harga_brg), int(stok_brg)])
                        print(f"Barang {nama_brg} berhasil ditambahkan!")
                    else:
                        print("GAGAL! Harga dan Stok wajib angka mutlak.")
                    input("Tekan Enter untuk kembali...")

                elif pilih_admin == '2':
                    print("\n--- DAFTAR BARANG ---")
                    if len(inventaris) == 0:
                        print("Gudang kosong.")
                    else:
                        for i in range(len(inventaris)):
                            brg = inventaris[i]
                            print(f"{i+1}. [{brg[0]}] {brg[1]} | Kategori: {brg[2]} | Harga: Rp{brg[3]} | Stok: {brg[4]}")
                    input("Tekan Enter untuk kembali...")

                elif pilih_admin == '3':
                    print("\n--- UPDATE HARGA & STOK ---")
                    if len(inventaris) == 0:
                        print("Gudang kosong.")
                    else:
                        for i in range(len(inventaris)):
                            print(f"{i+1}. {inventaris[i][1]} (Stok: {inventaris[i][4]})")
                        
                        idx_in = input("Pilih nomor barang: ")
                        if idx_in.isdigit():
                            indeks = int(idx_in) - 1
                            if 0 <= indeks < len(inventaris):
                                hrg_baru = input("Harga Baru (Angka): ")
                                stk_baru = input("Stok Baru (Angka): ")
                                if hrg_baru.isdigit() and stk_baru.isdigit():
                                    inventaris[indeks][3] = int(hrg_baru)
                                    inventaris[indeks][4] = int(stk_baru)
                                    print("Data berhasil di-update!")
                                else:
                                    print("GAGAL! Input harus angka.")
                            else:
                                print("Nomor tidak ditemukan.")
                        else:
                            print("Input tidak valid.")
                    input("Tekan Enter untuk kembali...")

                elif pilih_admin == '4':
                    print("\n--- HAPUS BARANG ---")
                    for i in range(len(inventaris)):
                        print(f"{i+1}. {inventaris[i][1]}")
                    
                    idx_hapus = input("Pilih nomor barang yang dihapus: ")
                    if idx_hapus.isdigit():
                        indeks = int(idx_hapus) - 1
                        if 0 <= indeks < len(inventaris):
                            brg_del = inventaris.pop(indeks)
                            print(f"{brg_del[1]} dihapus dari gudang.")
                        else:
                            print("Nomor tidak valid.")
                    else:
                        print("Input harus angka.")
                    input("Tekan Enter untuk kembali...")

                elif pilih_admin == '5':
                    print("\n--- HAPUS AKUN STAFF ---")
                    for i in range(len(staff_akun)):
                        print(f"{i+1}. {staff_akun[i][0]}")
                    
                    hps_staff = input("Pilih nomor urut staff: ")
                    if hps_staff.isdigit():
                        idx = int(hps_staff) - 1
                        if 0 <= idx < len(staff_akun):
                            stf_out = staff_akun.pop(idx)
                            print(f"Akun '{stf_out[0]}' dihapus!")
                        else:
                            print("Nomor tidak valid.")
                    else:
                        print("Input harus angka.")
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
            
        else:
            # Jika yang login staff
            staff_ditemukan = False
            for staff in staff_akun:
                if in_user == staff[0] and in_pass == staff[1]:
                    role_aktif = "Staff"
                    user_aktif = in_user
                    staff_ditemukan = True
                    break 
            
            if staff_ditemukan:
                print(f"Login berhasil! Selamat datang Staff {user_aktif}.")
                input("Tekan Enter untuk melanjutkan...")
                
                # =====================
                # Bagian 4: MENU STAFF
                # =====================
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
                            for i in range(len(inventaris)):
                                brg = inventaris[i]
                                print(f"{i+1}. [{brg[0]}] {brg[1]} | Stok: {brg[4]}")
                        input("Tekan Enter untuk kembali...")

                    elif pilih_staff == '2':
                        print("\n--- UPDATE STOK BARANG ---")
                        if len(inventaris) == 0:
                            print("Gudang kosong.")
                        else:
                            for i in range(len(inventaris)):
                                print(f"{i+1}. {inventaris[i][1]} (Stok: {inventaris[i][4]})")
                            
                            idx_in = input("Pilih nomor barang: ")
                            if idx_in.isdigit():
                                indeks = int(idx_in) - 1
                                if 0 <= indeks < len(inventaris):
                                    stk_baru = input("Stok Akhir (Angka): ")
                                    if stk_baru.isdigit():
                                        inventaris[indeks][4] = int(stk_baru)
                                        print("Stok berhasil diperbarui!")
                                    else:
                                        print("GAGAL! Stok wajib angka.")
                                else:
                                    print("Nomor tidak ditemukan.")
                            else:
                                print("Input tidak valid.")
                        input("Tekan Enter untuk kembali...")

                    elif pilih_staff == '3':
                        print("\n--- UBAH PROFIL STAFF ---")
                        new_user = input("Username baru: ")
                        new_pass = input("Password baru: ")
                        
                        user_ada = False
                        if new_user == admin_akun[0]:
                            user_ada = True
                        for s in staff_akun:
                            if new_user == s[0] and new_user != user_aktif:
                                user_ada = True
                                break
                        
                        if user_ada:
                            print("Gagal! Username sudah dipakai.")
                        else:
                            for i in range(len(staff_akun)):
                                if staff_akun[i][0] == user_aktif:
                                    staff_akun[i][0] = new_user
                                    staff_akun[i][1] = new_pass
                                    user_aktif = new_user
                                    print("Profil berhasil diperbarui!")
                                    break
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
        
        user_ada = False
        if reg_user == admin_akun[0]:
            user_ada = True
        for staff in staff_akun:
            if reg_user == staff[0]:
                user_ada = True
                break
                
        if user_ada:
            print("Gagal! Username sudah digunakan.")
        else:
            reg_pass = input("Masukkan Password baru: ")
            staff_akun.append([reg_user, reg_pass])
            print(f"Akun Staff '{reg_user}' berhasil didaftarkan!")
        input("Tekan Enter untuk kembali...")

    elif menu_awal == '3':
        print("Terima kasih telah menggunakan sistem inventaris IKEA!")
        break 

    else:
        print("Pilihan tidak valid! Masukkan angka 1, 2, atau 3.")
        input("Tekan Enter untuk kembali")