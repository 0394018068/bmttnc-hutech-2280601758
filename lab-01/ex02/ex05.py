# Nhap so gio lam moi tuan
so_gio_lam = float(input("Nhap so gio lam moi tuan: "))

# Nhap thu lao tren moi gio lam
luong_gio = float(input("Nhap thu lao tren moi gio lam: "))

# Gio tieu chuan
gio_tieu_chuan = 44

# Gio vuot chuan
gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan)

# Tinh thuc linh
thuc_linh = gio_tieu_chuan * luong_gio + gio_vuot_chuan * luong_gio * 1.5

# In ket qua
print(f"So tien thuc linh cua nhan vien: {thuc_linh}")
