import os

# ======================
# INISIALISASI DATA AWAL
# ======================
admin_akun = ("admin_gudang", "admin123") 
staff_akun = {
    "budi_staff": "pass123",
    "siti_staff": "pass321"
}
inventaris = {
    "001": {"nama": "Meja tanpa kaki", "kategori": "Furnitur", "harga": 450000, "stok": 25},
    "002": {"nama": "Kursi roda bertenaga kuda", "kategori": "Furnitur", "harga": 850000, "stok": 10},
    "003": {"nama": "Lampu gantung mahasiswa", "kategori": "Furnitur", "harga": 120000, "stok": 50}
}

# ===========================
# PRE-DEFINED ITULAH POKOKNYA
# ===========================
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_barang():
    if not inventaris:
        print("Gudang kosong.")
    else:
        for key_id, detail in inventaris.items():
            print(f"[{key_id}] {detail['nama']} | Kategori: {detail['kategori']} | Harga: Rp{detail['harga']} | Stok: {detail['stok']}")

def tampilkan_staff():
    if not staff_akun:
        print("Tidak ada akun staff terdaftar.")
    else:
        for staff_user in staff_akun.keys():
            print(f"- {staff_user}")

def menu_utama():
    clear_screen()
    print("""
=== SISTEM INVENTARIS GUDANG IKEA ===
1. Login (Admin / Staff)
2. Register Akun Staff
3. Keluar Program
=====================================
""")
    return input("Pilih menu (1/2/3): ")

def get_input_login():
    in_user = input("Masukkan Username: ")
    in_pass = input("Masukkan Password: ")
    return in_user, in_pass

def cek_id_tersedia(id_brg):
    return id_brg in inventaris

def cek_username_ganda(username_baru, user_aktif_sekarang=""):
    if username_baru == admin_akun[0] and username_baru != user_aktif_sekarang:
        return True
    if username_baru in staff_akun and username_baru != user_aktif_sekarang:
        return True
    return False

def input_angka_rekursif(pesan_prompt):
    try:
        nilai_int = int(input(pesan_prompt))
        return nilai_int 
    except ValueError:
        print("GAGAL! Input wajib berupa angka mutlak (tanpa huruf/simbol). Coba lagi.")
        return input_angka_rekursif(pesan_prompt)  
# ==========
# MENU UTAMA
# ==========
if __name__ == "__main__":
    while True:
        pilihan_menu = menu_utama()

        if pilihan_menu == '1':
            u_login, p_login = get_input_login()
            
            if u_login == admin_akun[0] and p_login == admin_akun[1]:
                user_aktif = u_login 
                print(f"Login berhasil! Selamat datang Admin {user_aktif}.")
                input("Tekan Enter untuk melanjutkan...")
                
                while True:
                    clear_screen()
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
                        print("--- TAMBAH BARANG BARU ---")
                        id_brg = input("Masukkan ID Barang: ")
                        if cek_id_tersedia(id_brg):
                            print("GAGAL! ID Barang sudah terdaftar di sistem.")
                        else:
                            nama_brg = input("Masukkan Nama Barang: ")
                            kategori = input("Masukkan Kategori: ")
                            harga_brg = input_angka_rekursif("Masukkan Harga (Hanya angka): ")
                            stok_brg = input_angka_rekursif("Masukkan Stok (Hanya angka): ")
                            
                            inventaris[id_brg] = {
                                "nama": nama_brg,
                                "kategori": kategori,
                                "harga": harga_brg,
                                "stok": stok_brg
                            }
                            print(f"Barang {nama_brg} berhasil ditambahkan!")
                        input("Tekan Enter untuk kembali...")

                    elif pilih_admin == '2':
                        print("--- DAFTAR BARANG ---")
                        tampilkan_barang() 
                        input("Tekan Enter untuk kembali...")

                    elif pilih_admin == '3':
                        print("--- UPDATE HARGA & STOK ---")
                        if not inventaris:
                            print("Gudang kosong.")
                        else:
                            tampilkan_barang()
                            id_update = input("Masukkan ID Barang yang ingin di-update: ")
                            if cek_id_tersedia(id_update):
                                hrg_baru = input_angka_rekursif("Harga Baru (Angka): ")
                                stk_baru = input_angka_rekursif("Stok Baru (Angka): ")
                                inventaris[id_update]["harga"] = hrg_baru
                                inventaris[id_update]["stok"] = stk_baru
                                print("Data berhasil di-update!")
                            else:
                                print("ID Barang tidak ditemukan.")
                        input("Tekan Enter untuk kembali...")

                    elif pilih_admin == '4':
                        print("--- HAPUS BARANG ---")
                        tampilkan_barang()
                        id_hapus = input("Masukkan ID Barang yang dihapus: ")
                        if cek_id_tersedia(id_hapus):
                            brg_del = inventaris.pop(id_hapus)
                            print(f"[{id_hapus}] {brg_del['nama']} dihapus dari gudang.")
                        else:
                            print("ID Barang tidak valid/tidak ditemukan.")
                        input("Tekan Enter untuk kembali...")

                    elif pilih_admin == '5':
                        print("--- HAPUS AKUN STAFF ---")
                        tampilkan_staff()
                        hps_staff = input("Ketik username staff yang ingin dihapus: ")
                        if hps_staff in staff_akun:
                            del staff_akun[hps_staff]
                            print(f"Akun '{hps_staff}' berhasil dihapus!")
                        else:
                            print("Username tidak ditemukan.")
                        input("Tekan Enter untuk kembali...")

                    elif pilih_admin == '6':
                        print("--- UBAH PROFIL ADMIN ---")
                        new_user = input("Username Admin baru: ")
                        new_pass = input("Password Admin baru: ")
                        
                        if cek_username_ganda(new_user, user_aktif):
                            print("GAGAL! Username sudah digunakan oleh akun lain.")
                        else:
                            admin_akun = (new_user, new_pass) 
                            user_aktif = new_user
                            print("Profil Admin diperbarui!")
                        input("Tekan Enter untuk kembali...")

                    elif pilih_admin == '7':
                        break
                    else:
                        print("Pilihan tidak valid!")
                        input("Tekan Enter untuk kembali...")

            elif u_login in staff_akun and staff_akun[u_login] == p_login:
                user_aktif = u_login
                print(f"Login berhasil! Selamat datang Staff {user_aktif}.")
                input("Tekan Enter untuk melanjutkan...")
                
                while True:
                    clear_screen()
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
                        print("--- DAFTAR BARANG ---")
                        tampilkan_barang()
                        input("Tekan Enter untuk kembali...")

                    elif pilih_staff == '2':
                        print("--- UPDATE STOK BARANG ---")
                        if not inventaris:
                            print("Gudang kosong.")
                        else:
                            tampilkan_barang()
                            id_update = input("Masukkan ID Barang: ")
                            if cek_id_tersedia(id_update):
                                stk_baru = input_angka_rekursif("Stok Akhir (Angka): ")
                                inventaris[id_update]["stok"] = stk_baru
                                print("Stok berhasil diperbarui!")
                            else:
                                print("ID Barang tidak ditemukan.")
                        input("Tekan Enter untuk kembali...")

                    elif pilih_staff == '3':
                        print("--- UBAH PROFIL STAFF ---")
                        new_user = input("Username baru: ")
                        new_pass = input("Password baru: ")
                        
                        if cek_username_ganda(new_user, user_aktif):
                            print("Gagal! Username sudah dipakai oleh admin atau staff lain.")
                        else:
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

        elif pilihan_menu == '2':
            print("--- REGISTER STAFF BARU ---")
            reg_user = input("Masukkan Username baru: ")
            
            if cek_username_ganda(reg_user):
                print("Gagal! Username sudah digunakan.")
            else:
                reg_pass = input("Masukkan Password baru: ")
                staff_akun[reg_user] = reg_pass
                print(f"Akun Staff '{reg_user}' berhasil didaftarkan!")
            input("Tekan Enter untuk kembali...")

        elif pilihan_menu == '3':
            print("Terima kasih telah menggunakan sistem inventaris IKEA!")
            break

        else:
            print("Pilihan tidak valid! Masukkan angka 1, 2, atau 3.")
            input("Tekan Enter untuk kembali...")