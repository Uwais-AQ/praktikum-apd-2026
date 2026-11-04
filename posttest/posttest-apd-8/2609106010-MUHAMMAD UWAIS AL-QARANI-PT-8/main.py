import database as data
import login
import crud

def menu_utama():
    crud.clear_screen()
    print("\n=== SISTEM INVENTARIS GUDANG IKEA ===")
    print("1. Login (Admin / Staff)")
    print("2. Register Akun Staff")
    print("3. Keluar Program")
    print("=====================================")
    return input("Pilih menu (1/2/3): ")

if __name__ == "__main__":
    while True:
        pilihan_menu = menu_utama()

        if pilihan_menu == '1':
            print("\n--- LOGIN TOWER ---")
            u_login, p_login = login.get_input_login()
            
            # Akses Admin
            if u_login == data.admin_akun[0] and p_login == data.admin_akun[1]:
                user_aktif = u_login 
                print(f"Login berhasil! Selamat datang Admin {user_aktif}.")
                input("Tekan Enter untuk melanjutkan...")
                
                while True:
                    crud.clear_screen()
                    print(f"\n=== DASHBOARD ADMIN: {user_aktif} ===")
                    print("1. Tambah Barang Baru")
                    print("2. Lihat Semua Barang")
                    print("3. Update Harga & Stok")
                    print("4. Hapus Barang")
                    print("5. Kelola Akun Staff")
                    print("6. Ubah Profil Admin")
                    print("7. Logout")
                    print("=====================================")
                    pilih_admin = input("Pilih menu (1-7): ")

                    if pilih_admin == '1':
                        print("\n--- TAMBAH BARANG BARU ---")
                        id_brg = input("Masukkan ID Barang: ")
                        if crud.cek_id_tersedia(id_brg):
                            print("GAGAL! ID Barang sudah terdaftar di sistem.")
                        else:
                            nama_brg = input("Masukkan Nama Barang: ")
                            kategori = input("Masukkan Kategori: ")
                            harga_brg = crud.input_angka_rekursif("Masukkan Harga (Hanya angka): ")
                            stok_brg = crud.input_angka_rekursif("Masukkan Stok (Hanya angka): ")
                            
                            data.inventaris[id_brg] = {
                                "nama": nama_brg,
                                "kategori": kategori,
                                "harga": harga_brg,
                                "stok": stok_brg
                            }
                            print(f"Barang {nama_brg} berhasil ditambahkan!")
                        input("Tekan Enter untuk kembali...")

                    elif pilih_admin == '2':
                        print("\n--- DAFTAR BARANG ---")
                        crud.tampilkan_barang() 
                        input("Tekan Enter untuk kembali...")

                    elif pilih_admin == '3':
                        print("\n--- UPDATE HARGA & STOK ---")
                        if not data.inventaris:
                            print("Gudang kosong.")
                        else:
                            crud.tampilkan_barang()
                            id_update = input("Masukkan ID Barang yang ingin di-update: ")
                            if crud.cek_id_tersedia(id_update):
                                hrg_baru = crud.input_angka_rekursif("Harga Baru (Angka): ")
                                stk_baru = crud.input_angka_rekursif("Stok Baru (Angka): ")
                                data.inventaris[id_update]["harga"] = hrg_baru
                                data.inventaris[id_update]["stok"] = stk_baru
                                print("Data berhasil di-update!")
                            else:
                                print("ID Barang tidak ditemukan.")
                        input("Tekan Enter untuk kembali...")

                    elif pilih_admin == '4':
                        print("\n--- HAPUS BARANG ---")
                        crud.tampilkan_barang()
                        id_hapus = input("Masukkan ID Barang yang dihapus: ")
                        if crud.cek_id_tersedia(id_hapus):
                            brg_del = data.inventaris.pop(id_hapus)
                            print(f"[{id_hapus}] {brg_del['nama']} dihapus dari gudang.")
                        else:
                            print("ID Barang tidak valid/tidak ditemukan.")
                        input("Tekan Enter untuk kembali...")

                    elif pilih_admin == '5':
                        print("\n--- HAPUS AKUN STAFF ---")
                        crud.tampilkan_staff()
                        hps_staff = input("Ketik username staff yang ingin dihapus: ")
                        if hps_staff in data.staff_akun:
                            del data.staff_akun[hps_staff]
                            print(f"Akun '{hps_staff}' berhasil dihapus!")
                        else:
                            print("Username tidak ditemukan.")
                        input("Tekan Enter untuk kembali...")

                    elif pilih_admin == '6':
                        print("\n--- UBAH PROFIL ADMIN ---")
                        new_user = input("Username Admin baru: ")
                        new_pass = input("Password Admin baru: ")
                        
                        if login.cek_username_ganda(new_user, user_aktif):
                            print("GAGAL! Username sudah digunakan oleh akun lain.")
                        else:
                            data.admin_akun = (new_user, new_pass) 
                            user_aktif = new_user
                            print("Profil Admin diperbarui!")
                        input("Tekan Enter untuk kembali...")

                    elif pilih_admin == '7':
                        break
                    else:
                        print("Pilihan tidak valid!")
                        input("Tekan Enter untuk kembali...")

            # Akses Staff
            elif u_login in data.staff_akun and data.staff_akun[u_login] == p_login:
                user_aktif = u_login
                print(f"Login berhasil! Selamat datang Staff {user_aktif}.")
                input("Tekan Enter untuk melanjutkan...")
                
                while True:
                    crud.clear_screen()
                    print(f"\n=== DASHBOARD STAFF: {user_aktif} ===")
                    print("1. Lihat Daftar Barang")
                    print("2. Update Stok Barang")
                    print("3. Ubah Profil Akun")
                    print("4. Logout")
                    print("=====================================")
                    pilih_staff = input("Pilih menu (1-4): ")

                    if pilih_staff == '1':
                        print("\n--- DAFTAR BARANG ---")
                        crud.tampilkan_barang()
                        input("Tekan Enter untuk kembali...")

                    elif pilih_staff == '2':
                        print("\n--- UPDATE STOK BARANG ---")
                        if not data.inventaris:
                            print("Gudang kosong.")
                        else:
                            crud.tampilkan_barang()
                            id_update = input("Masukkan ID Barang: ")
                            if crud.cek_id_tersedia(id_update):
                                stk_baru = crud.input_angka_rekursif("Stok Akhir (Angka): ")
                                data.inventaris[id_update]["stok"] = stk_baru
                                print("Stok berhasil diperbarui!")
                            else:
                                print("ID Barang tidak ditemukan.")
                        input("Tekan Enter untuk kembali...")

                    elif pilih_staff == '3':
                        print("\n--- UBAH PROFIL STAFF ---")
                        new_user = input("Username baru: ")
                        new_pass = input("Password baru: ")
                        
                        if login.cek_username_ganda(new_user, user_aktif):
                            print("Gagal! Username sudah dipakai oleh admin atau staff lain.")
                        else:
                            del data.staff_akun[user_aktif]
                            data.staff_akun[new_user] = new_pass
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
            print("\n--- REGISTER STAFF BARU ---")
            reg_user = input("Masukkan Username baru: ")
            
            if login.cek_username_ganda(reg_user):
                print("Gagal! Username sudah digunakan.")
            else:
                reg_pass = input("Masukkan Password baru: ")
                data.staff_akun[reg_user] = reg_pass
                print(f"Akun Staff '{reg_user}' berhasil didaftarkan!")
            input("Tekan Enter untuk kembali...")

        elif pilihan_menu == '3':
            print("Terima kasih telah menggunakan sistem inventaris IKEA!")
            break

        else:
            print("Pilihan tidak valid! Masukkan angka 1, 2, atau 3.")
            input("Tekan Enter untuk kembali...")