("-----------------------------------------{SELAMAT DATANG DI PEMESANAN PIZZALAALA}-----------------------------------------")
pizza = input("Masukan Namamu : ")

# Memeriksa pilihan untuk melanjutkan atau berhenti
if pizzahut5 == 1:
    pizzahut1 = int(input("Mau makan Pizza apa hari ini?\nketik 1 untuk melihat menu Pizza hari ini\n: "))
elif pizzahut5 == 2:
    print("see you... :) ")
    exit()
else:
    print("Maaf nomor atau keyword yang kamu masukan salah, silahkan ulangi dari awal")
    exit()

# Daftar harga pizza
Frankfurter = 45000
MeatMonsta = 50000
SuperSupreme = 60000
SuperSupremeChiken = 65000

# Menampilkan menu pizza
if pizzahut1 == 1:
    print("Daftar Harga Menu:")
    print(f"1. Frankfurter          : Rp {Frankfurter}")
    print(f"2. Meat Monsta          : Rp {MeatMonsta}")
    print(f"3. Super Supreme        : Rp {SuperSupreme}")
    print(f"4. Super Supreme Chicken: Rp {SuperSupremeChiken}")
    
    pizzahut3 = int(input("Masukan Pilihanmu : "))

    # Memilih pizza
    if pizzahut3 == 1:
        harga_pizza = Frankfurter
        print(f"Frankfurter          : Rp {harga_pizza}")
    elif pizzahut3 == 2:
        harga_pizza = MeatMonsta
        print(f"Meat Monsta          : Rp {harga_pizza}")
    elif pizzahut3 == 3:
        harga_pizza = SuperSupreme
        print(f"Super Supreme        : Rp {harga_pizza}")
    elif pizzahut3 == 4:
        harga_pizza = SuperSupremeChiken
        print(f"Super Supreme Chicken: Rp {harga_pizza}")
    else:
        print("Maaf, list yang kamu masukan tidak ada dalam menu kami kali ini. Silahkan ulangi pesananmu.")
        exit()

# Melanjutkan pesanan dengan memilih topping
pizza1 = int(input("ketik 1 untuk melanjutkan pesananmu : "))
original = 0
StuffedCrustCheese = 18000
StuffedCrustSausage = 15000
CheesyBites = 12000
EkstraKeju = 15000

if pizza1 == 1:
    print("Daftar Tambahan Topping:")
    print(f"1. Original             : Rp {original}")
    print(f"2. Stuffed Crust Cheese : Rp {StuffedCrustCheese}")
    print(f"3. Stuffed Crust Sausage: Rp {StuffedCrustSausage}")
    print(f"4. Cheesy Bites         : Rp {CheesyBites}")
    print(f"5. Ekstra Keju          : Rp {EkstraKeju}")
    
    pizzahut4 = int(input("Masukan Pilihan Toppingmu : "))

    # Memilih topping
    if pizzahut4 == 1:
        harga_topping = original
        print(f"Original             : Rp {harga_topping}")
    elif pizzahut4 == 2:
        harga_topping = StuffedCrustCheese
        print(f"Stuffed Crust Cheese : Rp {harga_topping}")
    elif pizzahut4 == 3:
        harga_topping = StuffedCrustSausage
        print(f"Stuffed Crust Sausage: Rp {harga_topping}")
    elif pizzahut4 == 4:
        harga_topping = CheesyBites
        print(f"Cheesy Bites         : Rp {harga_topping}")
    elif pizzahut4 == 5:
        harga_topping = EkstraKeju
        print(f"Ekstra Keju          : Rp {harga_topping}")
    else:
        print("Maaf, list yang kamu masukan tidak ada dalam menu kami kali ini")
        exit()
else:
    print("Maaf, keyword yang kamu masukan salah.")
    exit()

# Menambah ukuran pizza
pizzahut2 = int(input("ketik 1 untuk menambah ukuran, ketik 4 untuk tidak : "))
Kecil = 8000
Sedang = 18000
Besar = 28000

if pizzahut2 == 1:
    print(f"1. Kecil  Rp: {Kecil}")
    print(f"2. Sedang Rp: {Sedang}")
    print(f"3. Besar  Rp: {Besar}")
    
    pizzahut2 = int(input("Masukan Ukuran Pizzamu : "))

    # Memilih ukuran
    if pizzahut2 == 1:
        harga_ukuran = Kecil
        print(f"Kecil  : Rp {harga_ukuran}")
    elif pizzahut2 == 2:
        harga_ukuran = Sedang
        print(f"Sedang : Rp {harga_ukuran}")
    elif pizzahut2 == 3:
        harga_ukuran = Besar
        print(f"Besar  : Rp {harga_ukuran}")
    else:
        print("Maaf, ukuran tidak tersedia.")
        exit()
else:
    harga_ukuran = 0

# Penjumlahan total
total_harga = harga_pizza + harga_topping + harga_ukuran
print(f"Terima kasih sudah memesan, Total harga pesananmu adalah: Rp {total_harga}")
