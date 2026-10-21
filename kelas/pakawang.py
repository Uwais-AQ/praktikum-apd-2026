header = " x"
for i in range(1, 6):
    header += f"{i:4}"
print(header)

for j in range(1, 6):
    cetak_baris = f"{j:2}" 
    for k in range(1, 6):
        cetak_baris += f"{j * k:4}"
    print(cetak_baris)