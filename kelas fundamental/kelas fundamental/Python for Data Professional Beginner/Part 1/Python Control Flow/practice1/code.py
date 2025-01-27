# Data tagihan
tagihan_ke = 'Mr. Yoyo'

# Data layanan
warehousing = {'harga_harian': 1000000, 'total_hari': 15}
cleansing = {'harga_harian': 1500000, 'total_hari': 10}
integration = {'harga_harian': 2000000, 'total_hari': 15}
transform = {'harga_harian': 2500000, 'total_hari': 10}

# Menghitung subtotal masing-masing layanan
sub_warehousing = warehousing['harga_harian'] * warehousing['total_hari']
sub_cleansing = cleansing['harga_harian'] * cleansing['total_hari']
sub_integration = integration['harga_harian'] * integration['total_hari']
sub_transform = transform['harga_harian'] * transform['total_hari']

# Menghitung total harga
total_harga = sub_warehousing + sub_cleansing + sub_integration + sub_transform

# Menampilkan hasil
print("Tagihan kepada:")
print(tagihan_ke)
print("Selamat pagi, anda harus membayar tagihan sebesar:")
print(total_harga)