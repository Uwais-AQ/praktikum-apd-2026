username = "uwais"
password = "010"
pin = "010010"
saldo = 5000000

kesempatan_login = 3
login_sukses = False

while kesempatan_login > 0:
    print(f"\n[Sisa percobaan login: {kesempatan_login}]")
    input_user = input("Masukkan Username: ")
    input_pass = input("Masukkan Password: ")

    if input_user == username and input_pass == password:
        print("Login berhasil!")
        login_sukses = True
        break
    elif input_user != username and input_pass != password:
        print("Error: Username dan Password anda salah.")
    elif input_user != username:
        print("Error: Username anda salah.")
    elif input_pass != password:
        print("Error: Password anda salah.")
    
    kesempatan_login -= 1

if kesempatan_login == 0:
    print("Akun anda diblokir karena gagal login 3x. Mampus! >:]")
else:
    while login_sukses:
        print("\n=== MENU UTAMA ===")
        print("1. Transfer Uang")
        print("2. Logout")
        pilihan = input("Pilih menu (1/2): ")

        if pilihan == "2":
            print("Anda telah logout. Terima kasih!")
            break
        elif pilihan == "1":
            lanjut_transfer = "y"
            while lanjut_transfer == "y":
                print(f"\nSaldo saat ini: Rp{saldo}")
                penerima = input("Masukkan username penerima: ")

                nominal_valid = False
                while not nominal_valid:
                    nominal = int(input("Masukkan nominal transfer: Rp"))
                    if nominal < 50000:
                        print("Error: Nominal transfer minimal Rp50.000.")
                    elif nominal > 1000000:
                        print("Error: Nominal transfer maksimal Rp1.000.000.")
                    elif nominal > saldo:
                        print("Error: Saldo tidak mencukupi.")
                    else:
                        nominal_valid = True

                kesempatan_pin = 3
                pin_valid = False
                while kesempatan_pin > 0:
                    input_pin = input(f"Masukkan PIN (sisa {kesempatan_pin}x): ")
                    if input_pin == pin:
                        pin_valid = True
                        break
                    else:
                        print("Error: PIN salah.")
                        kesempatan_pin -= 1

                if kesempatan_pin == 0:
                    print("Akun anda diblokir karena salah PIN 3x. Tolong kerummah sakit kalau ada riwayat amnesia!")
                    login_sukses = False 
                    break

                if pin_valid:
                    saldo -= nominal
                    print("\n=== STRUK BUKTI TRANSFER ===")
                    print(f"Pengirim : {username}")
                    print(f"Penerima : {penerima}")
                    print(f"Nominal  : Rp{nominal}")
                    print("============================\n")

                lanjut_transfer = input("Apakah pengguna ingin melakukan transfer lagi (y/n)? ").lower()
        else:
            print("Pilihan tidak valid. Silakan pilih 1 atau 2.")

print("Terima kasih telah menggunakan layanan kami. Sampai jumpa!")