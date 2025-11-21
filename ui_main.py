import tkinter as tk
from tkinter import ttk, messagebox
from models import get_all_categories, get_makanan_by_category

class MainUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Toko Makanan")

        # DATA
        self.data = []
        self.index_now = 0

        # ================================
        # HEADER
        # ================================
        header = tk.Label(root, text="Toko Makanan ABC", font=("Arial", 18, "bold"))
        header.pack(pady=10)

        # ================================
        # FILTER
        # ================================
        frame_filter = tk.Frame(root)
        frame_filter.pack(pady=5)

        tk.Label(frame_filter, text="Filter berdasarkan kategori:").grid(row=0, column=0)

        categories = get_all_categories()
        categories = ["Semua"] + categories

        self.combo_kategori = ttk.Combobox(frame_filter, values=categories, width=20)
        self.combo_kategori.current(0)
        self.combo_kategori.grid(row=0, column=1, padx=5)
        self.combo_kategori.bind("<<ComboboxSelected>>", lambda e: self.load_data())

        # ================================
        # LIST MAKANAN
        # ================================
        self.tree = ttk.Treeview(root, columns=("nama", "harga", "kategori"), show="headings", height=10)
        self.tree.heading("nama", text="Nama Makanan")
        self.tree.heading("harga", text="Harga")
        self.tree.heading("kategori", text="Kategori")

        self.tree.pack(pady=10)

        # ================================
        # NAVIGASI & INPUT JUMLAH
        # ================================
        nav_frame = tk.Frame(root)
        nav_frame.pack(pady=5)

        tk.Button(nav_frame, text="<< Previous", command=self.prev_item).grid(row=0, column=0, padx=5)
        tk.Button(nav_frame, text="Next >>", command=self.next_item).grid(row=0, column=1, padx=5)

        # Input jumlah
        tk.Label(nav_frame, text="Jumlah:").grid(row=0, column=2, padx=5)
        self.entry_jumlah = tk.Entry(nav_frame, width=5)
        self.entry_jumlah.grid(row=0, column=3)

        # Button Tambah
        tk.Button(nav_frame, text="Tambahkan", command=self.add_item).grid(row=0, column=4, padx=10)

        # Load pertama kali
        self.load_data()

    # ================================
    # FUNGSI LOAD DATA
    # ================================
    def load_data(self):
        kategori = self.combo_kategori.get()
        self.data = get_makanan_by_category(kategori)
        self.index_now = 0

        # Clear table
        for i in self.tree.get_children():
            self.tree.delete(i)

        # Insert rows
        for d in self.data:
            self.tree.insert("", tk.END, values=(d["nama"], d["harga_default"], d["kategori"]))

    # ================================
    # NAVIGASI LIST MAKANAN
    # ================================
    def prev_item(self):
        if not self.data:
            return

        self.index_now = (self.index_now - 1) % len(self.data)
        self.highlight_current()

    def next_item(self):
        if not self.data:
            return

        self.index_now = (self.index_now + 1) % len(self.data)
        self.highlight_current()

    def highlight_current(self):
        children = self.tree.get_children()
        if children:
            self.tree.selection_set(children[self.index_now])
            self.tree.see(children[self.index_now])

    # ================================
    # ADD ITEM
    # ================================
    def add_item(self):
        if not self.data:
            return

        try:
            jumlah = int(self.entry_jumlah.get())
        except ValueError:
            messagebox.showerror("Error", "Jumlah harus angka!")
            return

        item = self.data[self.index_now]
        messagebox.showinfo(
            "Ditambahkan",
            f"{jumlah}x {item['nama']} berhasil ditambahkan!"
        )