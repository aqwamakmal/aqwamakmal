hitung_luas =int(input("""pilih rumus 1.hitung luas persegi 
1. Hitunglah persegi
2. Hitunglah lingkaran
3. Hitunglah segitiga
"""))

match hitung_luas :
    case 1:
        print("menghilang luas persegi")
        sisi = int(input("masukan sisi :"))
        print("luas persegi adalah :", sisi*sisi)
    case 2:
        jari_jari = float(input("masukan jari-jari lingkaran: "))
        luas =3.14 * jari_jari * jari_jari
        print("luas lingkaran:",luas)
    case 3:
        alas = float(input("masukan panjang alas segitiga"))
        tinggi = float(input("masukan tinggi segitiga: "))
        luas =0.5 * alas * tinggi
        print("luas segitiga", luas)
    case _:
        print("pilihan tidak valid")