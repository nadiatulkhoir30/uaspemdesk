import sqlite3

DB_NAME = "pemesanan_makanan.db"

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")

# ---- DATA makanan ----
cursor.executemany("""
INSERT INTO makanan (id_makanan, nama_makanan, harga_default, kategori, nama_gambar)
VALUES (?, ?, ?, ?, ?)
""", [
    (41, "Nasi Rawon", 10000, "Kuah", "Rawon.jpg"),
    (42, "Tahu Goreng", 8000, "Gorengan", "Tahu.jpg"),
    (43, "Lumpur Kentang", 3000, "Jajanan Pasar", "LumpurKentang.jpg"),
    (44, "Dadar Jagung", 5000, "Gorengan", "dadarjagung.jpg"),
    (45, "Nasi Briyani", 25000, "Nasi", "briyani.jpg")
])

# ---- DATA pembeli ----
cursor.executemany("""
INSERT INTO pembeli (id_pembeli, nama_pembeli, no_hp)
VALUES (?, ?, ?)
""", [
    (1, "Aulia", "081234567890"),
    (2, "Rizky", "081223344556"),
    (3, "Nadia", "081220987654"),
    (4, "Fikri", "081355667788"),
    (5, "Salsa", "081399887766")
])

# ---- DATA kasir ----
cursor.executemany("""
INSERT INTO kasir (id_kasir, nama_kasir, username)
VALUES (?, ?, ?)
""", [
    (1, "Dewi", "dewi01"),
    (2, "Putri", "putri22"),
    (3, "Baskara", "Baskara11"),
    (4, "Bima", "bima99"),
    (5, "Rina", "rina77")
])

# ---- DATA diskon_voucher ----
cursor.executemany("""
INSERT INTO diskon_voucher (id_voucher, nama_voucher, nilai, kode_voucher)
VALUES (?, ?, ?, ?)
""", [
    (1, "Diskon Awal Tahun", 10, "DISC10"),
    (2, "Diskon Pelajar", 15, "DISC15"),
    (3, "Promo Weekend", 20, "WEEK20"),
    (4, "Diskon Member", 5, "MEM5"),
    (5, "Promo Akhir Bulan", 25, "END25")
])

# ---- DATA transaksi ----
cursor.executemany("""
INSERT INTO transaksi (id_transaksi, tgl_transaksi, id_pembeli, id_kasir, id_voucher, total)
VALUES (?, ?, ?, ?, ?, ?)
""", [
    (1, "2025-11-01", 1, 1, 1, 20000),
    (2, "2025-11-02", 2, 2, 2, 40000),
    (3, "2025-11-03", 3, 3, None, 9000),
    (4, "2025-11-04", 4, 4, 4, 20000),
    (5, "2025-11-05", 5, 5, None, 25000)
])

# ---- DATA detail_transaksi ----
cursor.executemany("""
INSERT INTO detail_transaksi (id_detail, id_transaksi, id_makanan, kuantitas, harga_satuan, subtotal)
VALUES (?, ?, ?, ?, ?, ?)
""", [
    (41, 1, 41, 2, 10000, 20000),
    (42, 2, 42, 5, 8000, 40000),
    (43, 3, 43, 3, 3000, 9000),
    (44, 4, 44, 4, 5000, 20000),
    (45, 5, 45, 1, 25000, 25000)
])

conn.commit()
conn.close()

print("SEMUA DATA BERHASIL DIINSERT!")
