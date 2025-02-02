# Data
uang_jalan = 1500000  # Biaya per mobil per hari
jumlah_hari = 31  # Jumlah hari dalam sebulan
list_plat_nomor = [8993, 2198, 2501, 2735, 3772, 4837, 9152]  # Daftar nomor plat mobil

# Pengecekan kendaraan dengan nomor pelat ganjil atau genap
kendaraan_genap = 0  # Jumlah mobil dengan nomor plat genap
kendaraan_ganjil = 0  # Jumlah mobil dengan nomor plat ganjil

for plat_nomor in list_plat_nomor:
    if plat_nomor % 2 == 0:  # Cek apakah nomor plat genap
        kendaraan_genap += 1
    else:  # Jika ganjil
        kendaraan_ganjil += 1

# Total pengeluaran untuk kendaraan dengan nomor pelat ganjil dan genap dalam 1 bulan
i = 1  # Inisialisasi hari pertama
total_pengeluaran = 0  # Inisialisasi total pengeluaran

while i <= jumlah_hari:  # Loop selama masih ada hari dalam sebulan
    if i % 2 == 0:  # Jika hari genap
        total_pengeluaran += (kendaraan_genap * uang_jalan)  # Tambahkan biaya mobil plat genap
    else:  # Jika hari ganjil
        total_pengeluaran += (kendaraan_ganjil * uang_jalan)  # Tambahkan biaya mobil plat ganjil
    i += 1  # Lanjut ke hari berikutnya

# Cetak total pengeluaran
print(total_pengeluaran)