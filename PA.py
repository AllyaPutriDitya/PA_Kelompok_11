import csv
import pwinput
from prettytable import PrettyTable

admin = {'name': 'pa1', 'password': 'susah'}
users = []

def simpan_users_ke_csv():
    with open('users.csv', mode='w', newline='') as file:
        fieldnames = ['nama', 'password', 'saldo']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for user in users:
            writer.writerow({'nama': user.nama, 'password': user.password, 'saldo': user.saldo})

def load_users_dari_csv():
    try:
        with open('users.csv', mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                users.append(User(row['nama'], row['password'], float(row['saldo'])))
    except FileNotFoundError:
        pass

class User:
    def __init__(self, nama, password, saldo=0):
        self.nama = nama
        self.password = password
        self.saldo = saldo
        self.invoices = []

def tambah_saldo(self, jumlah):
        self.saldo += jumlah

class Invoice:
    def __init__(self, user, code, quantity, total_biaya):
        self.user = user
        self.code = code
        self.quantity = quantity
        self.total_biaya = total_biaya



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
    with open('List_AlatBerat.csv', 'w', newline='') as new_file:
        fieldNames = ["Code", "Jenis Alat", "Merk", "Biaya Rental", "stok Alat"]
        csv_writer = csv.DictWriter(
            new_file, delimiter=',', fieldnames=fieldNames)
        csv_writer.writeheader()
        for AlatBerat in List_AlatBerat:
            csv_writer.writerow(AlatBerat)
dataList_AlatBerat()

# Nama file CSV yang akan digunakan
file_name = 'List_AlatBerat.csv'

# Fungsi untuk membaca semua data dari file CSV
def baca_List_AlatBerat():
    data = []
    with open(file_name, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# Fungsi untuk menambahkan data baru ke file CSV
def tambah_List_AlatBerat(Code, Jenis_Alat, Merk, Biaya_Rental, stok_Alat):
    with open(file_name, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    if any(row['Code'] == Code for row in data):
        print("Code sudah ada di Data")

    else:
        if stok_Alat.isdigit() and int(stok_Alat) >= 0:
            with open(file_name, mode='a', newline='') as file:
                fieldnames = ["Code", "Jenis Alat", "Merk", "Biaya Rental", "stok Alat"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)

                writer.writerow({
                    'Code': Code,
                    'Jenis Alat': Jenis_Alat,
                    'Merk': Merk,
                    'Biaya Rental': Biaya_Rental,
                    'stok Alat': stok_Alat
                })
            print("\nData Alat Berat berhasil ditambahkan.\n")
        else:
            print("\ninputan tidak valid\n")

# Fungsi untuk memperbarui data dalam file CSV
def perbarui_List_AlatBerat():
    data = baca_List_AlatBerat()
    code_update = input("Masukkan Code yang ingin diperbarui: ")
    code_exists = any(row['Code'] == code_update for row in data)

    if code_exists:
        new_Jenis_Alat = input("Masukkan Jenis Alat yang baru: ")
        new_Merk = input("Masukkan Merk yang baru: ")
        new_Biaya_Rental = input("Masukkan Biaya yang baru: ")
        new_stok_Alat = input("Masukkan Stok Alat yang baru: ")

        for row in data:
            if row['Code'] == code_update:
                row['Jenis Alat'] = new_Jenis_Alat
                row['Merk'] = new_Merk
                row['Biaya Rental'] = new_Biaya_Rental
                row['stok Alat'] = new_stok_Alat

        with open(file_name, mode='w', newline='') as file:
            fieldnames = ["Code", "Jenis Alat", "Merk", "Biaya Rental", "stok Alat"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print("\nData Alat Berat berhasil diperbarui.\n")
    else:
        print("Code tidak ditemukan.\n")


# Fungsi untuk menghapus data dari file CSV
def hapus_List_AlatBerat(Code):
        data = baca_List_AlatBerat()
        with open('List_AlatBerat.csv', mode='w', newline='') as file:
            fieldnames = ["Code", "Jenis Alat", "Merk", "Biaya Rental", "stok Alat"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for row in data:
                if row['Code'] != Code:
                    writer.writerow(row)

# Login sebagai admin
def loginAdmin():
    while True: 
        logUser = input("\nMasukkan Username : ")
        logPW = pwinput.pwinput("Password : ", mask='*')

        if logUser == "admin" and logPW == "123":
            while True:
                print("\n================================Menu Utama================================")
                print("1. Tambah Data")
                print("2. Lihat Data")
                print("3. Perbarui Data")
                print("4. Hapus Data")
                print("5. Kembali")
                pilihan = input("Pilih menu (1/2/3/4/5): ")

                if pilihan == '1':
                    Code = input("\nMasukkan Code: ")
                    Jenis_Alat = input("Masukkan Jenis Alat: ")
                    Merk = input("Masukkan Merk: ")
                    Biaya_Rental = input("Masukkan Biaya Rental: ")
                    stok_Alat = (input("Masukkan Stok Alat: "))
                    data = baca_List_AlatBerat()
                    code_exists = False

                    for row in data:
                        if row['Code'] == Code:
                            code_exists = True
                            break
                    if stok_Alat.isnumeric():
                        if int(stok_Alat) < 0:
                            print("Inputan tidak valid")


                    tambah_List_AlatBerat(Code, Jenis_Alat, Merk, Biaya_Rental, stok_Alat)

                elif pilihan == '2':
                    data = baca_List_AlatBerat()
                    tabel = PrettyTable(["Code", "Jenis Alat", "Merk", "Biaya Rental", "stok Alat"])
                    for row in data:
                        tabel.add_row([row['Code'], row['Jenis Alat'], row['Merk'], row['Biaya Rental'], row['stok Alat']])
                    print(tabel)


                elif pilihan == '3':
                    perbarui_List_AlatBerat()

                elif pilihan == '4':
                    Code = input("Masukkan Code yang ingin dihapus: ")
                    data = baca_List_AlatBerat()
                    code_exists = False

                    for row in data:
                        if row['Code'] == Code:
                            code_exists = True
                            break

                    if code_exists:
                        hapus_List_AlatBerat(Code)
                        print(f"Data dengan Code {Code} berhasil dihapus.")
                    else:
                        print(f"Data dengan Code {Code} tidak ditemukan.")

                elif pilihan == '5':
                    return

                else:
                    print("Pilihan tidak valid. Silakan pilih lagi.")
        else:
            print("Username atau Password anda salah, coba lagi\n")
            return

# Menu program 
def cek_username(nama):
    with open('users.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['nama'] == nama:
                return True
        return False

def registrasi_user():
    nama = input("Masukkan username anda: ")
    password = pwinput.pwinput("Masukkan password anda: ", mask='*')
    new_user = User(nama, password)
    users.append(new_user)

    if not cek_username(nama):
        with open('users.csv', 'a', newline='') as file:
            fieldnames = ['username', 'password']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            writer.writerow({'username': nama, 'password': password})
        print(f"Akun dengan username '{nama}' telah berhasil terdaftar.")
        print("Registrasi Berhasil.")
        simpan_users_ke_csv()
    else:
        print(f"Maaf, username '{nama}' sudah digunakan. Silakan pilih username lain.\n")

load_users_dari_csv()
def login_user():
    while True:
        nama = input("Masukkan username anda: ")
        password = pwinput.pwinput("Masukkan password anda: ", mask='*')
        user = next((u for u in users if u.nama == nama and u.password == password), None)
        if user:
            print("\n======================Login berhasil======================\n")
            return user
        else:
            print("\nUsername dan password salah. Coba lagi.\n")
            return

def melakukan_transaksi(user):
    data = baca_List_AlatBerat()
    tabel = PrettyTable(["Code", "Jenis Alat", "Merk", "Biaya Rental", "stok Alat"])
    for row in data:
        tabel.add_row([row['Code'], row['Jenis Alat'], row['Merk'], row['Biaya Rental'], row['stok Alat']])
    print(tabel)
    print("\n==========================Melakukan Transaksi==========================\n")
    code = input("\nMasukkan Code alat yang ingin disewa: ")
    Alat = next((item for item in List_AlatBerat if item["Code"] == code), None)

    if Alat:
        quantity = (input("Masukkan jumlah jam yang ingin disewa: "))
        if quantity.isnumeric():
            if int(quantity) > 0:  # Periksa apakah jumlah valid
                total_biaya = int(Alat['Biaya Rental'].replace("Rp. ", "").replace("/Jam", "")) * int(quantity)
                if user.saldo >= total_biaya and Alat['stok Alat'] >= int(quantity):
                    user.saldo -= total_biaya
                    invoice = Invoice(user, code, quantity, total_biaya)
                    user.invoices.append(invoice)
                    Alat['stok Alat'] -= int(quantity)
                    simpan_users_ke_csv()
                    dataList_AlatBerat()
                    print(f"\nTransaksi berhasil.\n")
                elif user.saldo < total_biaya:
                    print("Saldo tidak mencukupi.'\n")
                else:
                    print("Stok Alat tidak mencukupi.\n")
            else:
                print("Jumlah harus lebih besar dari 0.\n")
        else:
            print("Inputan tidak Valid\n")
    else:
        print("Alat tidak ditemukan.\n")



def tampilkan_invoices(user):
    print("============================Lihat Struk============================")
    if not user.invoices:
        print("\nStruk tidak ditemukan.\n")
        ("=" * 30)
    else:
        print("\nStruk Anda:\n")
        for invoice in user.invoices:
            equipment = next((item for item in List_AlatBerat if item["Code"] == invoice.code), None)
            if equipment:
                print("=" * 30)
                print(f"\nAlat: {equipment['Jenis Alat']} - {equipment['Merk']}")
                print(f"\nQuantity: {invoice.quantity}")
                print(f"\nTotal Biaya: Rp. {invoice.total_biaya}")
                print("=" * 30)

def tambah_saldo(user):
    print("===============================Tambah Saldo===============================")
    try:
        jumlah_saldo = float(input("Masukkan jumlah saldo yang ingin ditambahkan: "))
        if jumlah_saldo >0:
            user.saldo += jumlah_saldo
            simpan_users_ke_csv()
            print(f"Saldo berhasil ditambahkan. Saldo sekarang: Rp. {user.saldo}\n")
        elif jumlah_saldo <0:
            print("Inputan tidak valid\n")
    except:
        print("Inputan tidak valid\n")


def pilihan_user(user):
    while True:
        print("=" * 30)
        print("Selamat Datang!\n")
        print("1. Mulai Transaksi")
        print("2. Lihat Struk")
        print("3. Tambah Saldo")
        print("4. Lihat Saldo")
        print("5. Kembali")
        pilih = input("Pilih (1/2/3/4/5): ")

        if pilih == "1":
            melakukan_transaksi(user)
        elif pilih == "2":
            tampilkan_invoices(user)
        elif pilih == "3":
            tambah_saldo(user)
        elif pilih == "4":
            print(f"\nSaldo Anda saat ini: Rp. {user.saldo}")
        elif pilih == "5":
            return
        else:
            print("Pilihan tidak valid.")

# Main program
while True:
    print("=====================================Login=====================================")
    print("1. Admin")
    print("2. User")
    print("3. Keluar")
    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        print("\n=====================================Admin=====================================")
        loginAdmin()
    elif pilihan == "2":
        while True:
            print("\n=====================================User=====================================")
            print("1. Login")
            print("2. Registrasi")
            print("3. Kembali")
            pilihan_user_login = input("Pilih (1/2/3): ")

            if pilihan_user_login == "1":
                user = login_user()
                if user:
                    pilihan_user(user)
            elif pilihan_user_login == "2":
                registrasi_user()
            elif pilihan_user_login == "3":
                break
            else:
                print("Pilihan tidak valid.\n")
    elif pilihan == "3":
        break
    else:
        print("Pilihan tidak valid. Coba lagi!\n")
