# PA_Kelompok_11

Tema program = Penyewaan Alat Berat

awalan progaram di buka dengan menu untuk login sebagai admin, user, atau keluar dari program

![Screenshot (89)](https://github.com/Lizzylizzz/PA_Kelompok_11/assets/144436692/fbf28eab-db7f-49b7-b91f-448f692a42a1)




1. Jika memilih login sebagai Admin
   Pengguna diminta untuk menginput nama dan password.
   jika salah inputan salah, akan di kembalikan ke menu awal

![Screenshot (91)](https://github.com/Lizzylizzz/PA_Kelompok_11/assets/144436692/f05777b3-0545-40bf-bfb2-ec8174adaf8f)


   jika berhasil, pengguna diarahkan ke menu admin

![Screenshot (92)](https://github.com/Lizzylizzz/PA_Kelompok_11/assets/144436692/2bd344b0-c222-4c03-9f89-2d9f2d84ad13)

   
   jika memilih 1, yaitu menambahkan data baru
   pengguna diminta untuk menginput code, nama alat, merk, harga, dan stok. 
   jika inputan code ada di dalam list, maka outputnya seperti ini

![Screenshot (94)](https://github.com/Lizzylizzz/PA_Kelompok_11/assets/144436692/4811df1a-2cef-4e4e-9547-6035735da51f)

   
   jika inputan stok berisi tidak lebih dari 0 dan berisi string, maka outputnya seperti ini

![Screenshot (95)](https://github.com/Lizzylizzz/PA_Kelompok_11/assets/144436692/8b7a5802-117e-48d7-a180-eecf990013f0)
   
   jika inputan sesuai program akan menyimpan data tambahan tersebut ke dalam list

![Screenshot (96)](https://github.com/Lizzylizzz/PA_Kelompok_11/assets/144436692/d6fee89c-3a7c-43d7-9ce1-22d86540d6f6)

   

   jika memilih 2, program akan menampilkan list, sesuai dengan data list yang terbaru yang disimpan dalam file dinamis, CSV

![Screenshot (97)](https://github.com/Lizzylizzz/PA_Kelompok_11/assets/144436692/24331b51-d0e9-464a-bcbc-94f08494c5e8)


   jika memilih 3 yaitu perbarui data
   pengguna diminta untuk menginput code yang ingin diubah untuk mengubah nama alat, merk, harga dan stock.
   jika inputan code tidak ada dalam list, maka outputnya seperti ini

![Screenshot (98)](https://github.com/Lizzylizzz/PA_Kelompok_11/assets/144436692/a5a422c8-a8fa-4a53-91a3-2867d0bb900a)

   
   jika inputan sesuai maka program akan menyimpan perubahan tersebut

![Screenshot (99)](https://github.com/Lizzylizzz/PA_Kelompok_11/assets/144436692/ae49d79e-446a-487a-8cf4-1e11aceec455)


   jika memilih 4 yaitu menghapus data
   penggna diminta untuk masukkan code yang ingin di hapus.
   jika code yang dimasukkan tidak ada dalam list, maka outpunya seperti ini

![Screenshot (100)](https://github.com/Lizzylizzz/PA_Kelompok_11/assets/144436692/2b1675ac-8134-4e4c-aa6d-8286b1d2790c)

   
   jika code yang dimasukkan ada dalam list, program menghapus code yang di masukkan tadi

![Screenshot (102)](https://github.com/Lizzylizzz/PA_Kelompok_11/assets/144436692/d1afc86f-d37b-4a28-9598-ea1b54855b8f)


   jika memilih 5 yaitu kembali, pengguna diarahkan ke halaman login

![Screenshot (103)](https://github.com/Lizzylizzz/PA_Kelompok_11/assets/144436692/c944627f-9a48-4e52-8b62-edd989000cfd)


   jika memilih pilihan yang diluar opsi maka outpunya seperti ini

![Screenshot (104)](https://github.com/Lizzylizzz/PA_Kelompok_11/assets/144436692/d83e1302-7c56-4ef4-aef4-e55e0f3e1490)




2. Jika memilih login sebagai User,
   pengguna diarahkan untuk memilih opsi ini

![Screenshot (104)](https://github.com/Lizzylizzz/PA_Kelompok_11/assets/144436692/0b2674eb-6745-4a5d-be91-8806a7afbb08)


   jika pengguna memilih registrasi, pengguna diminta masukkan nama dan password.
   jika inputan nama pengguna dalam registrasi sama dengan nama user yang sudah terdaftar, maka registrasi gagal dan diarahkan ke halaman opsi masuk sebagai user

![Screenshot (106)](https://github.com/Lizzylizzz/PA_Kelompok_11/assets/144436692/83a7d0ba-5fdb-4ecc-9f63-e4a53efee39c)

   
   jika inputan baru, maka registrasi berhasil dan diarahan ke halaman opsi masuk sebagai user

![Screenshot (107)](https://github.com/Lizzylizzz/PA_Kelompok_11/assets/144436692/8495b886-af08-48b9-ae7c-3a02fab576d5)

   
   jika memilih Login, pengguna diminta untuk masukan nama dan password.
   jika nama dan password salah atau tidak terdaftar, maka login gagal dan di arahkan ke halaman opsi masuk sebagi user

![Screenshot (108)](https://github.com/Lizzylizzz/PA_Kelompok_11/assets/144436692/516b180f-1054-4ab2-90c4-8cc659b07a4d)

   
   jika nama dan password benar atau terdaftar, maka program mengarahkan pengguna ke halaman user

![Screenshot (109)](https://github.com/Lizzylizzz/PA_Kelompok_11/assets/144436692/c0e3d3f0-25c0-494a-b9d8-f203e737725c)

   
   
   jika memilih 1 yaitu mulai transaksi,
   pengguna diminta untuk masukkan code alat yang ingin di sewa beserta durasi penyewaan.
   jika user memasukkan code diluar dari list, maka outputnya seperti ini

![Screenshot (110)](https://github.com/Lizzylizzz/PA_Kelompok_11/assets/144436692/9fcf9dde-791d-4818-864b-39db64db5539)

   
   jia user memasukkan durasi penyewaan selain angka dan -, maka outputnya seperti ini

![Screenshot (111)](https://github.com/Lizzylizzz/PA_Kelompok_11/assets/144436692/673c3b15-1b07-4bbd-a648-b9432585e9dd)

   
   jika user memasukkan code dan durasi yang sesuai, maka data menyimpan data penyewaan tersebut ke dalam struk

![Screenshot (112)](https://github.com/Lizzylizzz/PA_Kelompok_11/assets/144436692/76757188-3dcc-4df3-8c5f-1fd59465e529)

   
   jika memilih 2 yaitu lihat struk, program menampilkan biaya penyewaan yang sudah di pilih user sebelumnya

![Screenshot (113)](https://github.com/Lizzylizzz/PA_Kelompok_11/assets/144436692/9bd89ad6-d44d-48b4-a49d-40ad136d8735)

   
   jika pengguna belum ada memilih barang penyewaan, maka outputnya seperti ini
   
![Screenshot (114)](https://github.com/Lizzylizzz/PA_Kelompok_11/assets/144436692/80ee47ce-aa1c-4cd9-9ab1-55e73c1259df)

   jika memilih 3 yaitu tambah saldo.
   jika pengguna memasukkkan angka maka program berhasil menambahkan saldo user

![Screenshot (116)](https://github.com/Lizzylizzz/PA_Kelompok_11/assets/144436692/f2da531b-08f8-4a95-acc8-0737f44b47f7)


   jika pengguna memasukkan inputan selain angka maka outpunya seperti ini

![Screenshot (115)](https://github.com/Lizzylizzz/PA_Kelompok_11/assets/144436692/ad6c9578-a4d5-420f-aa59-68d3c4363367)


   jika memilih 4 yaitu melihat saldo pengguna, program menampilkan saldo pengguna
   
![Screenshot (117)](https://github.com/Lizzylizzz/PA_Kelompok_11/assets/144436692/03def4c1-2e9a-4f6f-8dac-db5c2a33c985)

   jika memilih 5, program mengarahkan ke halaman opsi masuk sebagai user
   
![Screenshot (118)](https://github.com/Lizzylizzz/PA_Kelompok_11/assets/144436692/6a6faaa0-8cce-4fbe-9593-adf3c9d460f3)


   jika memilih pilihan yang diluar opsi, output progran seperti ini

![Screenshot (119)](https://github.com/Lizzylizzz/PA_Kelompok_11/assets/144436692/f27dc722-6a0d-4c3d-8768-a594ff01b856)



3. jika memilih 3 yaitu keluar, program akan berhenti

![Screenshot (121)](https://github.com/Lizzylizzz/PA_Kelompok_11/assets/144436692/3ee71f2b-0ac6-46fd-b9eb-ea42a24b2df4)




4. jika memilih pilihan diluar opsi, output program seperti ini

![Screenshot (120)](https://github.com/Lizzylizzz/PA_Kelompok_11/assets/144436692/ed282cff-5073-4874-8e37-52685dc4f0b8)
