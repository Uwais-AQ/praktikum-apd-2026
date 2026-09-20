barang_1 = 15000
barang_2 = 25000
barang_3 = 10000
barang_4 = 5500
barang_5 = 5000
barang_6 = 20000
list_nama_barang = ["Barang 1", "Barang 2", "Barang 3", "Barang 4", "Barang 5", "Barang 6"]

subtotal = barang_1 + barang_2 + barang_3 + barang_4 + barang_5 + barang_6
total_bayar = subtotal + (0.15 * subtotal)

kurs_usd = 18000
kurs_euro = 20000
total_euro = total_bayar / kurs_euro
total_usd = total_bayar / kurs_usd

barang_istimewa = list_nama_barang[::2]

nim = 10
rata_rata = total_bayar / len(list_nama_barang)
bolean = nim < rata_rata
print("Hasil perhitungan belanjaan Andi",
      "\nTotal bayar dalam Rupiah: Rp.", total_bayar,
      "\nTotal dalam USD: $", total_usd,
      "\nTotal dalam Euro: €", total_euro,
      "\nRata-rata: ", rata_rata,
      "\nApakah rata-rata lebih besar dari NIM?", bolean,
      "\nApa saja barang istimewa?: ", barang_istimewa)
