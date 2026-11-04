import database as data

def get_input_login():
    in_user = input("Masukkan Username: ")
    in_pass = input("Masukkan Password: ")
    return in_user, in_pass

def cek_username_ganda(username_baru, user_aktif_sekarang=""):
    if username_baru == data.admin_akun[0] and username_baru != user_aktif_sekarang:
        return True
    
    if username_baru in data.staff_akun and username_baru != user_aktif_sekarang:
        return True
        
    return False