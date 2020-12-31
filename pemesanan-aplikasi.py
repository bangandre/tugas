import os
from time import sleep

perbaris = 5000
perhalaman = 50000
plusdatabase = 200000
sort1, sort2, data1, data2 = [], [], [], []

def query(a, b, c, d, e):
	print(f'''
Nama                : {a}
Jumlah Baris        : {b}
Jumlah Halaman      : {c}
Menggunakan Database: {d}
Total Biaya         : Rp {e}\n\n''')

def sorting():
	for x in data1:
		sort1.append(x[4])
	sortc = sort1.copy()
	sort1.sort()
	for x in sort1:
		sort2.append(sortc.index(x))
	for x in sort2:
		data2.append(data1[x])

def output():
	menu = input('\n>>>')
	if menu == '1':
		for x in data1:
			query(x[0], x[1], x[2], x[3], x[4])
	elif menu == '2':
		for x in data2:
			query(x[0], x[1], x[2], x[3], x[4])
	elif menu == '3':
		print('Total Biaya Pesanan Terkecil:')
		query(data2[0][0], data2[0][1], data2[0][2], data2[0][3], data2[0][4])
		print('Total Biaya Pesanan Terbesar:')
		query(data2[-1][0], data2[-1][1], data2[-1][2], data2[-1][3], data2[-1][4])
	elif menu == '4':
		try:
			cari = int(input('[•] Masukan Total Biaya Yang Ingin Anda Cari: '))
			cari = sort1.index(cari)
			query(data2[cari][0], data2[cari][1], data2[cari][2], data2[cari][3], data2[cari][4])
		except:
			print('\n\n[!] Maaf Total Biaya Yang Anda Cari Tidak Ditemukan!')
	elif menu == '5':
		exit()
	else:
		print('\n\n[!] Maaf Pilihan Tidak Terdaftar Pada Menu!')
	output()

def tamp_output():
	os.system('clear')
	print(f'''{"="*54}
Menu:
1. Tampilkan Semua Pesanan (Data Belum Urut)
2. Tampilkan Semua Pesanan (Data Sudah Urut)
3. Tampilkan Total Biaya Pesanan Terkecil dan Terbesar
4. Pencarian Data Terhadap Total Biaya
5. Keluar Program
{"="*54}''')
	sorting()
	output()
	
def proses(nama, baris, halaman, database):
	tarifbaris = baris*perbaris
	tarifhalaman = halaman*perhalaman
	if database.lower() == 'y':
		tarifdatabase = plusdatabase
		database = 'Ya'
	else:
		tarifdatabase = 0
		database = 'Tidak'
	tariftotal = tarifbaris + tarifhalaman + tarifdatabase
	newdata = [nama, baris, halaman, database, tariftotal]
	data1.append(newdata)
	tambah = input('\n\n[•] Apakah Anda Akan Melakukan Pemesanan Lagi [y/t]: ')
	if tambah.lower() == 'y':
		inputt()
	else:
		tamp_output()

def inputt():
	os.system('clear')
	print('[!] Silahkan Isi Formulir Untuk Melakukan Pemesanan\n')
	nama = input('[•] Nama Pelanggan: ')
	baris = int(input('[•] Jumlah Baris  : '))
	halaman = int(input('[•] Jumlah Halaman: '))
	database = input('[•] Menggunakan Database [y/t]: ')
	if nama and baris and halaman and database != '':
		proses(nama, baris, halaman, database)
	else:
		print('\n\n[!] Pastikan Anda Mengisi FormulirDengan Benar!')
		sleep(2)
		inputt()
	
if __name__=='__main__':
	inputt()
