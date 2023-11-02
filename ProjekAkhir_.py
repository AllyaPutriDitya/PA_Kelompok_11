import csv
import pwinput # untuk menyembunyikan password
from prettytable import PrettyTable # untuk membuat tampilan tabel

admin = {'name': 'admin', 'password': '123'}
users = [] # list kosong untuk menyimpan objek data pengguna (User)

# Fungsi untuk menyimpan data pengguna ke dalam file CSV
def simpan_users_ke_csv():
    with open('users.csv', mode='w', newline='') as file:
        fieldnames = ['nama', 'password', 'saldo'] # untuk menulis nama kolom
        writer = csv.DictWriter(file, fieldnames=fieldnames) # objek writer
        writer.writeheader() # untuk menulis kolom header

        for user in users:  # Tulis setiap baris data pengguna ke dalam file CSV
            writer.writerow({'nama': user.nama, 'password': user.password, 'saldo': user.saldo})

# fungsi memuat daata user dari file csv
def load_users_dari_csv():
    try:
        with open('users.csv', mode='r', newline='') as file: # buka file csv
            reader = csv.DictReader(file) # membaca file csv sebagai dict
            for row in reader: # membaca atau loop setiap baris data
                users.append(User(row['nama'], row['password'], float(row['saldo'])))
    except FileNotFoundError:
        pass # Jika file CSV tidak ditemukan, lanjutkan program


class User:
    def __init__(self, nama, password, saldo=0):
        self.nama = nama # atribut nama
        self.password = password
        self.saldo = saldo
        self.invoices = [] # list buat nyimpan objek invoice

# metode menambahkan saldo
def tambah_saldo(self, jumlah):
        self.saldo += jumlah

# Definisi class Invoice yang merepresentasikan invoice untuk setiap transaksi
class Invoice:
    def __init__(self, user, code, total_jam, total_biaya):
        self.user = user
        self.code = code
        self.total_jam = total_jam
        self.total_biaya = total_biaya


# ini Data list alat berat bisa dibaca dari file CSV atau diinisialisasi di dalam kode
List_AlatBerat = [
    {"Code": "1A", "Jenis Alat": "Excavator", "Merk": "Hitachi PC 200", "Biaya Rental": "Rp. 300000/Jam", "stok Alat": 5},
    {"Code": "1B", "Jenis Alat": "Excavator", "Merk": "Hitachi PC 50", "Biaya Rental": "Rp. 100000/Jam", "stok Alat": 3},
    {"Code": "1C", "Jenis Alat": "Excavator", "Merk": "Caterpillar PC 200", "Biaya Rental": "Rp. 350000/Jam", "stok Alat": 6},
    {"Code": "2A", "Jenis Alat": "BullDozer", "Merk": "Caterpillar Crawler", "Biaya Rental": "Rp. 300000/Jam", "stok Alat": 2},
    {"Code": "2B", "Jenis Alat": "BullDozer", "Merk": "Komatsu Wheel", "Biaya Rental": "Rp. 250000/Jam", "stok Alat": 1},
    {"Code": "3A", "Jenis Alat": "Dump Truck", "Merk": "Hino Dutro 130 HD", "Biaya Rental": "Rp. 300000/Jam", "stok Alat": 4},
    {"Code": "3B", "Jenis Alat": "Dump Truck", "Merk": "Mitsubishi FE 74 HD K", "Biaya Rental": "Rp. 200000/Jam", "stok Alat": 7},
    {"Code": "3C", "Jenis Alat": "Dump Truck", "Merk": "Scania R620", "Biaya Rental": "Rp. 350000/Jam", "stok Alat": 8}   
]

# Simpan data ke dalam file CSV
def dataList_AlatBerat():

    # Membuka file CSV dan menulis data alat berat ke dalamnya
    with open('List_AlatBerat.csv', 'w', newline='') as new_file:
        fieldNames = ["Code", "Jenis Alat", "Merk", "Biaya Rental", "stok Alat"]
        csv_writer = csv.DictWriter(
            new_file, delimiter=',', fieldnames=fieldNames)
        csv_writer.writeheader() # tulis header

        # Tulis setiap baris data alat berat ke dalam file CSV
        for AlatBerat in List_AlatBerat:
            csv_writer.writerow(AlatBerat)
dataList_AlatBerat() # Memanggil fungsi dataList_AlatBerat untuk menyimpan data alat berat ke dalam file CSV

# Nama file CSV yang akan digunakan
file_name = 'List_AlatBerat.csv'

# Fungsi untuk membaca semua data dari file CSV
def baca_List_AlatBerat():
    data = []  # Inisialisasi list untuk menampung data dari file CSV
    with open(file_name, mode='r', newline='') as file:  # Buka file CSV
        reader = csv.DictReader(file)  # Membaca file sebagai dictionary
        for row in reader:  # Loop setiap baris data dalam file CSV
            data.append(row)  # Menambahkan setiap baris data ke dalam list data
    return data  # Mengembalikan data yang telah terbaca dari file CSV

# Fungsi untuk menambahkan data alat baru ke file CSV
def tambah_List_AlatBerat(Code, Jenis_Alat, Merk, Biaya_Rental, stok_Alat):
    # baca data dari file csv
    with open(file_name, mode='r', newline='') as file: # Membuka file CSV untuk pembacaan
        reader = csv.DictReader(file) # Membaca file sebagai dictionary
        data = list(reader) # Membuat list dari data yang terbaca

        # periksa apakah kode sudah ada di data
    if any(row['Code'] == Code for row in data):
        print("Code sudah ada di Data\n")

    else:
        # memeriksa inputan
        if stok_Alat.isdigit() and int(stok_Alat) >= 0 and Biaya_Rental.replace("Rp. ", "").replace("/Jam", "").isdigit():
            # tulis data baru ke csv
            with open(file_name, mode='a', newline='') as file: # Membuka file CSV untuk menulis
                fieldnames = ["Code", "Jenis Alat", "Merk", "Biaya Rental", "stok Alat"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)

                # Menulis data alat berat baru ke dalam file CSV
                writer.writerow({
                    'Code': Code,
                    'Jenis Alat': Jenis_Alat,
                    'Merk': Merk,
                    'Biaya Rental': Biaya_Rental,
                    'stok Alat': stok_Alat
                })
            print("Data Alat Berat berhasil ditambahkan.\n")
        else:
            print("inputan tidak valid\n")

# Fungsi untuk memperbarui data dalam file CSV
def perbarui_List_AlatBerat():
    data = baca_List_AlatBerat() # baca data
    code_update = input("Masukkan Code yang ingin diperbarui: ")
    code_exists = any(row['Code'] == code_update for row in data)

    if code_exists:
        new_Jenis_Alat = input("Masukkan Jenis Alat yang baru: ")
        new_Merk = input("Masukkan Merk yang baru: ")
        new_Biaya_Rental = input("Masukkan Biaya yang baru: ")
        new_stok_Alat = input("Masukkan Stok Alat yang baru: ")

        #periksa inputan
        if new_Biaya_Rental.isnumeric():
            if int(new_Biaya_Rental) < 0:
                print("inputan tidak valid\n")
        if new_stok_Alat.isnumeric():
            if int(new_stok_Alat) < 0:
                print("inputan tidak valid\n")

        # memperbarui data yang sesuai
        for row in data: # Loop data alat berat
            if row['Code'] == code_update: # Jika Code cocok dengan yang diinput
                # Memperbarui informasi alat berat sesuai input yang baru
                row['Jenis Alat'] = new_Jenis_Alat
                row['Merk'] = new_Merk
                row['Biaya Rental'] = new_Biaya_Rental
                row['stok Alat'] = new_stok_Alat

        # Tulis perubahan ke dalam file CSV
        if new_stok_Alat.isdigit() and int(new_stok_Alat) >= 0 and new_Biaya_Rental.replace("Rp. ", "").replace("/Jam", "").isdigit():
            with open(file_name, mode='w', newline='') as file: # Membuka file CSV untuk penulisan
                fieldnames = ["Code", "Jenis Alat", "Merk", "Biaya Rental", "stok Alat"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader() # Menulis header ke file CSV
                writer.writerows(data) # menulis semua data yang diperbarui
            print("Data Alat Berat berhasil diperbarui.\n")
        else:
            print("Inputan tidak Valid\n")
    else:
        print("Code tidak ditemukan.\n")


# Fungsi untuk menghapus data dari file CSV
def hapus_List_AlatBerat(Code):
        data = baca_List_AlatBerat()  # Memanggil fungsi untuk membaca data alat berat dari file CSV
        with open('List_AlatBerat.csv', mode='w', newline='') as file:
            fieldnames = ["Code", "Jenis Alat", "Merk", "Biaya Rental", "stok Alat"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

        # Tulis kembali data ke dalam file CSV kecuali data yang ingin dihapus
            for row in data:
                if row['Code'] != Code: # Memeriksa setiap baris data untuk Code yang tidak sama dengan yang ingin dihapus
                    writer.writerow(row) # Menulis baris data yang tidak dihapus ke dalam file CSV

# Login sebagai admin
def loginAdmin():
    while True: 
        logUser = input("\nMasukkan Username : ")
        logPW = pwinput.pwinput("Password : ", mask='*')

        # memeriksa username sama password
        if logUser == "admin" and logPW == "123":
            while True: # Jika login berhasil, tampilkan menu utama
                print("\n================================Menu Utama Admin================================\n")
                print("Selamat Datang!")
                print("1. Tambah Data")
                print("2. Lihat Data")
                print("3. Perbarui Data")
                print("4. Hapus Data")
                print("5. Kembali")
                pilihan = input("Pilih menu (1/2/3/4/5): ")

                if pilihan == '1':
                    print("\n===============================Tambah Data===============================\n")
                    Code = input("Masukkan Code: ")
                    Jenis_Alat = input("Masukkan Jenis Alat: ")
                    Merk = input("Masukkan Merk: ")
                    Biaya_Rental = input("Masukkan Biaya Rental: ")
                    stok_Alat = (input("Masukkan Stok Alat: "))
                    data = baca_List_AlatBerat()
                    code_exists = False # Inisialisasi variabel code_exists sebagai False

                    for row in data:
                        if row['Code'] == Code: # Memeriksa jika Code sudah ada di data
                            code_exists = True # Inisialisasi variabel code_exists sebagai True
                            break
                    if stok_Alat.isnumeric():
                        if int(stok_Alat) < 0:
                            print("Inputan tidak valid")

                    # Memanggil fungsi tambah_List_AlatBerat dengan input yang diberikan
                    tambah_List_AlatBerat(Code, Jenis_Alat, Merk, Biaya_Rental, stok_Alat)

                elif pilihan == '2':
                    print("\n===============================Lihat Data===============================\n")
                    data = baca_List_AlatBerat()
                    tabel = PrettyTable(["Code", "Jenis Alat", "Merk", "Biaya Rental", "stok Alat"])
                    for row in data: # Menampilkan data menggunakan PrettyTable
                        tabel.add_row([row['Code'], row['Jenis Alat'], row['Merk'], row['Biaya Rental'], row['stok Alat']])
                    print(tabel)


                elif pilihan == '3':
                    print("\n===============================Perbarui Data===============================\n")
                    perbarui_List_AlatBerat()

                elif pilihan == '4':
                    print("\n===============================Hapus Data===============================\n")
                    Code = input("Masukkan Code yang ingin dihapus: ")
                    data = baca_List_AlatBerat()
                    code_exists = False # Inisialisasi variabel code_exists sebagai False

                    for row in data:
                        if row['Code'] == Code: # Memeriksa jika Code yang ingin dihapus ada dalam data
                            code_exists = True # Jika Code ditemukan, set code_exists ke True
                            break

                    if code_exists: # Jika Code ada dalam data
                        hapus_List_AlatBerat(Code)
                        print(f"Data dengan Code {Code} berhasil dihapus.\n")
                    else:
                        print(f"Data dengan Code {Code} tidak ditemukan.\n")

                elif pilihan == '5':
                    return

                else:
                    print("Pilihan tidak valid. Silakan pilih lagi.\n")
        else:
            print("Username atau Password anda salah, coba lagi\n")

# Fungsi cek_username memeriksa keberadaan username dalam file CSV
def cek_username(nama):
    # Membuka file 'users.csv' untuk dibaca
    with open('users.csv', 'r', newline='') as file:
        reader = csv.DictReader(file) # Membaca file CSV sebagai dictionary
        for row in reader:
            if row['nama'] == nama: # Jika nama sudah ada dalam baris file CSV, mengembalikan True
                return True
        return False # Mengembalikan False jika nama tidak ditemukan dalam file CSV

# Fungsi untuk mendaftarkan pengguna baru
def registrasi_user():
    print("\n=====================================Registrasi=====================================\n")
    nama = input("Masukkan username anda: ")
    password = pwinput.pwinput("Masukkan password anda: ", mask='*')
    new_user = User(nama, password) # Membuat objek User baru dengan username dan password
    users.append(new_user) # Menambahkan user baru ke dalam list pengguna

    # Memeriksa keberadaan username menggunakan fungsi cek_username
    if not cek_username(nama): # Jika username belum ada, menulis username dan password ke file 'users.csv'
        with open('users.csv', 'a', newline='') as file:
            fieldnames = ['username', 'password']
            writer = csv.DictWriter(file, fieldnames=fieldnames) 
            writer.writerow({'username': nama, 'password': password}) # Menulis username dan password baru ke dalam file CSV
        print(f"Akun dengan username '{nama}' telah berhasil terdaftar.\n")
        print("\nRegistrasi Berhasil.\n")
        simpan_users_ke_csv() # Menyimpan perubahan ke dalam file CSV
    else:
        print(f"Maaf, username '{nama}' sudah digunakan. Silakan pilih username lain.\n")

load_users_dari_csv() # Memuat data pengguna dari file CSV saat aplikasi dijalankan

def login_user():
    while True:
        print("\n=====================================Login User=====================================\n")
        nama = input("Masukkan username anda: ")
        password = pwinput.pwinput("Masukkan password anda: ", mask='*')
        user = next((u for u in users if u.nama == nama and u.password == password), None)
        if user: # Jika pengguna ditemukan
            print("Login berhasil.\n")
            return user
        else:
            print("Username dan password salah. Coba lagi.\n")
            return

def melakukan_transaksi(user):
    data = baca_List_AlatBerat()
    tabel = PrettyTable(["Code", "Jenis Alat", "Merk", "Biaya Rental", "stok Alat"])
    for row in data:
        tabel.add_row([row['Code'], row['Jenis Alat'], row['Merk'], row['Biaya Rental'], row['stok Alat']])
    print(tabel)

    code = input("Masukkan Code alat yang ingin disewa: ")
    Alat = next((item for item in List_AlatBerat if item["Code"] == code), None) # Mencari alat dengan kode yang dimasukkan

    if Alat:  # Jika alat ditemukan
        total_jam = input("Masukkan jumlah jam yang ingin disewa: ")  # Meminta pengguna untuk memasukkan jumlah jam yang ingin disewa
        if total_jam.isdigit() and int(total_jam) > 0:  # Periksa apakah input jumlah jam merupakan angka yang positif
            total_jam = int(total_jam)  # Mengubah total_jam menjadi tipe data integer
            total_biaya = int(Alat['Biaya Rental'].replace("Rp. ", "").replace("/Jam", "")) * total_jam  # Menghitung total biaya berdasarkan harga sewa per jam dan jumlah jam
            if user.saldo >= total_biaya and Alat['stok Alat'] >= 1:  # Jika saldo pengguna mencukupi dan stok alat tersedia
                user.saldo -= total_biaya  # Mengurangi saldo pengguna sesuai dengan total biaya transaksi
                invoice = Invoice(user, code, total_jam, total_biaya)  # Membuat objek Invoice untuk transaksi
                user.invoices.append(invoice)  # Menambahkan invoice ke daftar transaksi pengguna
                Alat['stok Alat'] -= 1  # Mengurangi stok alat yang disewa sebanyak 1
                simpan_users_ke_csv()  # Menyimpan perubahan saldo pengguna ke file CSV
                dataList_AlatBerat()  # Memperbarui data stok alat ke file CSV
                print(f"Transaksi berhasil!\n")  # Memberi pesan bahwa transaksi berhasil dilakukan beserta total biaya
            elif user.saldo < total_biaya:  # Jika saldo tidak mencukupi
                print("Saldo tidak mencukupi.\n")  # Memberi pesan bahwa saldo tidak mencukupi
            else:  # Jika stok alat tidak mencukupi
                print("Stok Alat tidak mencukupi.\n")  # Memberi pesan bahwa stok alat tidak mencukupi
        else:  # Jika input jumlah jam tidak valid
            print("Jumlah jam harus berupa angka dan lebih besar dari 0.\n")  # Memberi pesan bahwa jumlah jam harus berupa angka positif
    else:  # Jika alat tidak ditemukan
        print("Alat tidak ditemukan.\n")  # Memberi pesan bahwa alat dengan kode yang dimasukkan tidak ditemukan


# Fungsi untuk menampilkan struk transaksi pengguna
def tampilkan_invoices(user):
    if not user.invoices: # Periksa apakah daftar invoices pengguna kosong
        print("Struk tidak ditemukan.\n")
    else:
        print("Struk Anda:")
        for invoice in user.invoices: # Iterasi melalui setiap invoice dalam daftar invoices pengguna

            # Cari peralatan terkait dengan kode pada invoice dalam List_AlatBerat
            equipment = next((item for item in List_AlatBerat if item["Code"] == invoice.code), None) 
            if equipment: # Jika peralatan ditemukan
                print("=" * 50)
                print(f"\nAlat: {equipment['Jenis Alat']} - {equipment['Merk']}")
                print(f"\ntotal jam: {invoice.total_jam}") # Tampilkan total jam pada invoice
                print(f"\nTotal Biaya: Rp. {invoice.total_biaya}") # Tampilkan total biaya pada invoice
                print("=" * 50)

def tambah_saldo(user):
    try:
        jumlah_saldo = float(input("Masukkan jumlah saldo yang ingin ditambahkan: "))
        if jumlah_saldo >0: # Jika jumlah saldo lebih dari nol
            user.saldo += jumlah_saldo # Tambahkan saldo ke saldo pengguna
            simpan_users_ke_csv() # Simpan perubahan saldo ke file CSV
            print(f"Saldo berhasil ditambahkan. Saldo sekarang: Rp. {user.saldo}\n")
        elif jumlah_saldo <0: # Jika jumlah saldo kurang dari nol
            print("Inputan tidak valid\n") 
    except:
        print("Inputan tidak valid\n")

# Fungsi untuk memungkinkan pengguna memilih opsi terkait transaksi atau saldo
def pilihan_user(user):
    while True:
        print("\n================================Menu Utama User================================\n")
        print("Selamat Datang!\n")
        print("1. Mulai Transaksi")
        print("2. Lihat Struk")
        print("3. Tambah Saldo")
        print("4. Lihat Saldo")
        print("5. Kembali")
        pilih = input("Pilih (1/2/3/4/5): ")

        if pilih == "1":
            print("\n==========================Melakukan Transaksi==========================\n")
            melakukan_transaksi(user)
        elif pilih == "2":
            print("\n==========================Lihat Transaksi==========================\n")
            tampilkan_invoices(user)
        elif pilih == "3":
            print("\n==========================Tambah Saldo==========================\n")
            tambah_saldo(user)
        elif pilih == "4":
            print("\n==========================Lihat Saldo==========================\n")
            print(f"Saldo Anda saat ini: Rp. {user.saldo}\n")
        elif pilih == "5":
            return
        else:
            print("Pilihan tidak valid.\n")

# Main program
while True:
    print("\n=====================================Login=====================================\n")
    print("1. Admin")
    print("2. User")
    print("3. Keluar")
    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        print("\n=====================================Admin=====================================\n")
        loginAdmin()
    elif pilihan == "2":
        print("\n=====================================User=====================================\n")
        while True:
            print("1. Login")
            print("2. Registrasi")
            print("3. Kembali")
            pilihan_user_login = input("Pilih (1/2/3): ")

            if pilihan_user_login == "1":
                user = login_user() # Jalankan fungsi login_user() untuk login
                if user:
                    pilihan_user(user) # Jika user berhasil login, jalankan fungsi untuk opsi user
            elif pilihan_user_login == "2":
                registrasi_user() # Jalankan fungsi untuk registrasi user
            elif pilihan_user_login == "3":
                break 
            else:
                print("Pilihan tidak valid.\n")
    elif pilihan == "3":
        break
    else:
        print("Pilihan tidak valid. Coba lagi!\n")