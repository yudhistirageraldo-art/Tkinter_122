
import tkinter as tk
from tkinter import ttk

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("500x650")
root.resizable(False, False)

# Judul aplikasi
judul = tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Times New Roman", 16, "bold")
)
judul.pack(pady=20)

# Frame input nilai
frame_input = tk.Frame(root)
frame_input.pack(pady=5)

# Daftar mata pelajaran
mapel = [
    "Matematika",
    "Bahasa Indonesia",
    "Bahasa Inggris",
    "Informatika",
    "Fisika",
    "Kimia",
    "Biologi",
    "Ekonomi",
    "Sejarah",
    "Sejarah Indonesia",
]

entries = []

# Membuat label dan input
for i, nama in enumerate(mapel):
    label = tk.Label(
        frame_input,
        text=nama,
        width=20,
        anchor="w",
        font=("Times New Roman", 12)
    )
    label.grid(row=i, column=0, padx=10, pady=5)

    entry = ttk.Entry(frame_input, width=20)
    entry.grid(row=i, column=1, padx=10, pady=5)

    entries.append(entry)

# Fungsi hasil prediksi
def hasil_prediksi():
    hasil.config(
        text="Prodi Pilihan Anda:\nTeknologi Informasi",
        fg="green"
    )

# Tombol prediksi
tombol = tk.Button(
    root,
    text="Hasil Prediksi",
    command=hasil_prediksi,
    font=("Times New Roman", 12, "bold"),
    bg="#1976D2",
    fg="white",
    padx=15,
    pady=8
)
tombol.pack(pady=20)

# Label hasil
hasil = tk.Label(
    root,
    text="Hasil prediksi akan muncul di sini",
    font=("Times New Roman", 12),
    wraplength=400
)
hasil.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()
