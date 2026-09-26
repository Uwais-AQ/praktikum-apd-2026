angka = int(input("Masukkan angka: "))

if angka < 6:
    print("angka kurang dari 6")
else:
    print("angka tidak kurang dari 6")

###ternary operator
# Jarang dipake, karena ini buat satu baris aja, kalo lebih dari satu baris mending pake if else biasa
# syntax awalnya adalah: result = "value_if_true" if condition else "value_if_false"
result = "angka kurang dari 6" if angka < 6 else "angka tidak kurang dari 6"
print(result)

if angka > 10:
    print("angka lebih dari 10")