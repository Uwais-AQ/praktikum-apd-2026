import os
from prettytable import PrettyTable
from colorama import Fore, Style, init
import database as data

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_barang():
    if not data.inventaris:
        print("Gudang kosong.")
        return

    tabel = PrettyTable()
    tabel.field_names = ["ID", "Nama Barang", "Kategori", "Harga", "Stok"]
    
    for key_id, detail in data.inventaris.items():
        tabel.add_row([
            key_id, 
            detail['nama'], 
            detail['kategori'], 
            f"Rp{detail['harga']}", 
            detail['stok']
        ])
    
    print(tabel)

def tampilkan_staff():
    if not data.staff_akun:
        print("Tidak ada akun staff terdaftar.")
        return
    
    tabel = PrettyTable()
    tabel.field_names = ["Username Staff"]
    
    for username in data.staff_akun.keys():
        tabel.add_row([username])
        
    print(tabel)

def cek_id_tersedia(id_brg):
    return id_brg in data.inventaris

def input_angka_rekursif(pesan_prompt):
    try:
        nilai_int = int(input(pesan_prompt))
        return nilai_int 
    except ValueError:
        print(Fore.RED + "GAGAL! Input wajib berupa angka mutlak (tanpa huruf/simbol). Coba lagi." + Style.RESET_ALL)
        return input_angka_rekursif(pesan_prompt)