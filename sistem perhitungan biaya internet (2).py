#!/usr/bin/env python
# coding: utf-8

# In[1]:


def main():
    print("Selamat datang di Program Perhitungan Biaya Internet")
    # Di sini akan diisi dengan kode selanjutnya

if __name__ == "__main__":
    main()


# In[3]:


# Fungsi untuk menghitung biaya internet
def hitung_biaya(mb):
    harga_per_mb = 10  # Harga per MB
    harga_per_gb = 5000  # Harga per GB
    satuan_gb = 1000  # 1 GB = 1000 MB

    if mb < satuan_gb:
        total_biaya = mb * harga_per_mb  # Hitung biaya jika kurang dari 1 GB
    else:
        gb = mb / satuan_gb  # Konversi MB ke GB
        total_biaya = gb * harga_per_gb  # Hitung biaya jika lebih dari 1 GB

    return total_biaya

# Fungsi utama
def main():
    print("=== Program Perhitungan Biaya Internet ===")

    while True:  # Loop untuk meminta input hingga valid
        try:
            mb = float(input("Masukkan jumlah pemakaian internet (MB): "))  # Input dari pengguna
            if mb < 0:  # Cek jika input negatif
                print("Input tidak valid! Harap masukkan angka positif.")
                continue  # Kembali ke awal loop untuk meminta input lagi
            break  # Keluar dari loop jika input valid
        except ValueError:
            print("Input tidak valid! Harap masukkan angka.")

    total_biaya = hitung_biaya(mb)  # Hitung total biaya
    print(f"Total biaya internet: Rp{total_biaya:.2f}")  # Tampilkan hasil
    input("tekan enter untuk keluar...") 

# Memanggil fungsi utama
if __name__ == "__main__":
    main()



# In[ ]:




