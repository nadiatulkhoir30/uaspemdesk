import sqlite3

# Nama database
DB_NAME = "pemesanan_makanan.db"

# Koneksi
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

# Aktifkan foreign key
cursor.execute("PRAGMA foreign_keys = ON;")

# ===============================
# Eksekusi pembuatan tabel
# ===============================

tables_sql = [

    # ---------------------------
    # TABEL makanan
    # ---------------------------
    """
    CREATE TABLE IF NOT EXISTS makanan (
        id_makanan     INTEGER PRIMARY KEY,
        nama_makanan   VARCHAR(50),
        harga_default  DECIMAL,
        kategori       VARCHAR(50)
    );
    """,

    # ---------------------------
    # TABEL pembeli
    # ---------------------------
    """
    CREATE TABLE IF NOT EXISTS pembeli (
        id_pembeli     INTEGER PRIMARY KEY,
        nama_pembeli          VARCHAR(50),
        no_hp          VARCHAR(50)
    );
    """,

    # ---------------------------
    # TABEL kasir
    # ---------------------------
    """
    CREATE TABLE IF NOT EXISTS kasir (
        id_kasir   INTEGER PRIMARY KEY,
        nama_kasir     VARCHAR(50),
        username   VARCHAR(30)
    );
    """,

    # ---------------------------
    # TABEL diskon
    # ---------------------------
    # """
    # CREATE TABLE IF NOT EXISTS diskon (
    #     id_diskon   INTEGER PRIMARY KEY,
    #     nama        VARCHAR(50),
    #     type        TEXT CHECK(type IN ('persen', 'nominal')),
    #     nilai       DECIMAL,
    #     keterangan  TEXT
    # );
    # """,

    # ---------------------------
    # TABEL diskon_voucher
    # ---------------------------
    """
    CREATE TABLE IF NOT EXISTS diskon_voucher (
        id_voucher   INTEGER PRIMARY KEY,
        nama_voucher         VARCHAR(50),
        nilai        DECIMAL,
        kode_voucher   TEXT
    );
    """,

    # ---------------------------
    # TABEL transaksi
    # ---------------------------
    """
    CREATE TABLE IF NOT EXISTS transaksi (
        id_transaksi   INTEGER PRIMARY KEY,
        tgl_transaksi  DATETIME,
        id_pembeli     INTEGER,
        id_kasir       INTEGER,
        id_voucher     INTEGER,
        total          DECIMAL,
        FOREIGN KEY (id_pembeli) REFERENCES pembeli(id_pembeli),
        FOREIGN KEY (id_kasir) REFERENCES kasir(id_kasir),
        FOREIGN KEY (id_voucher) REFERENCES diskon_voucher(id_voucher)
    );
    """,

    # ---------------------------
    # TABEL detail_transaksi
    # ---------------------------
    """
    CREATE TABLE IF NOT EXISTS detail_transaksi (
        id_detail      INTEGER PRIMARY KEY,
        id_transaksi   INTEGER,
        id_makanan     INTEGER,
        kuantitas      INTEGER,
        harga_satuan   DECIMAL,
        
        subtotal       DECIMAL,
        FOREIGN KEY (id_transaksi) REFERENCES transaksi(id_transaksi),
        FOREIGN KEY (id_makanan) REFERENCES makanan(id_makanan)
    );
    """
]

# Eksekusi semua SQL
for sql in tables_sql:
    cursor.execute(sql)

# Commit & close
conn.commit()
conn.close()

print(f"Database '{DB_NAME}' berhasil dibuat dengan semua tabel!")
