# Meminta input jumlah baris dari pengguna
jumlah_baris = int(input("Masukkan jumlah baris: "))

# Membuat rangkaian bintang menggunakan for loop
for i in range(1, jumlah_baris + 1):
    print("*" * i)