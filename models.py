from db import get_connection

def get_all_categories():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT kategori FROM makanan;")
    rows = [r["kategori"] for r in cur.fetchall()]
    conn.close()
    return rows

def get_makanan_by_category(kategori=None):
    conn = get_connection()
    cur = conn.cursor()

    if kategori and kategori != "Semua":
        cur.execute("""
            SELECT * FROM makanan WHERE kategori = ?;
        """, (kategori,))
    else:
        cur.execute("SELECT * FROM makanan;")

    rows = cur.fetchall()
    conn.close()
    return rows
