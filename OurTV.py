import json
import os

Users_Data = "users.json"
watched_stack = []
Watched_Queue = []

def ambil_genre_unik(films):
	genres = []
	for film in films:
		genre = film["genre"]
		if genre not in genres:
			genres.append(genre) 
	return genres

#Fungsi Ambil Genre Unik ini untuk menglist ada Genre apa saja Contohnya: kalau ada genre baru maka ia akan append di list genresnya

def quick_sort(daftar):
	if len(daftar) <= 1:
		return daftar
	titik_Acuan = daftar[0]
	lebih_kecil = []
	lebih_besar_atw_sama = []

	for nilai in daftar[1:]:
		if nilai < titik_Acuan:
			lebih_kecil.append(nilai)
		else:
			lebih_besar_atw_sama.append(nilai)

	return quick_sort(lebih_kecil) + [titik_Acuan] + quick_sort(lebih_besar_atw_sama)

	#Fungsi untuk Sorting genre agar terurut

def tampil_genre(genres):
	os.system("cls")
	print("------Daftar Genre------")
	nomor = 1
	for genre in genres:
		print(nomor, ".", genre)
		nomor += 1
	print()
	try:
		pilihan = int(input("Pilih genre yang ingin Anda lihat (1-%d) : " %(nomor-1)))
	except ValueError:
		print("Inputnya harus Angka.")
		return
	if pilihan>=1 and pilihan <= len(genres):
		pilih_genre = genres[pilihan-1]
		tampil_film_yang_dipilih(pilih_genre)
	else:
		print("Pilihan Tidak Sesuai, Silahkan Coba Lagi")
	print("Tekan 'ENTER' untuk Kembali")
	a = input()


def tampil_film_yang_dipilih(genre):
	os.system("cls")
	print("----------Daftar film dengan Genre: %s-----------"%(genre))
	nomor = 0
	for film in FILMS:
		if film["genre"] == genre:
			nomor += 1
			print(nomor, ".", film["title"])
	if nomor == 0:
		print("Tidak ada Film di genre ini")
		input()


def Cek_Data_User():
	if os.path.exists(Users_Data) == False:		
		return {}
	
	file = open(Users_Data, "r")   
	data = json.load(file)  
	file.close()  	
	return data
    #Untuk ngecek dan mengubah data yang ada di file bertipe json jadi file yang dapat di akses di python / dictionary

def save_data_user(users):
	file = open(Users_Data, "w")
	json.dump(users, file,indent = 2)

def sign_up(users):
	os.system("cls")
	print("--- Daftar (Sign Up) ---")

	while True:
		username = input("Masukkan username: ")
		if len(username) == 0:
			print("Username tidak boleh kosong.")
		elif username in users:
			print("Username sudah terdaftar, coba lagi.")
		else:
			break

	while True:
		password = input("Masukkan password: ")
		if len(password) == 0:
			print("Password tidak boleh kosong.")
		else:
			break

	users[username] = {"password": password, "watching_list": []}
	save_data_user(users)
	print("User '" , username , "' berhasil didaftarkan!")
	username = sign_in(users)
	return username

def sign_in(users):
	os.system("cls")
	print("\n--- Sign In ---")
	username = input("Masukkan username: ")
	if username not in users:
		print("Username tidak ditemukan.")
		return None
	password = input("Masukkan password: ")
	if users[username]["password"] != password:	
		print("Password salah.")
		return None
	print("Welcome,", username,"!\n")
	return username

def Linear_Search_Film():
	os.system("cls")
	search_item = input("Film apa yang Anda cari: ").lower()
	finded_item = []
	for film in FILMS:
		if search_item in film["title"].lower():
			finded_item.append(film)
	if len(finded_item)== 0:
		print("Film Tidak Ditemukan")
		return []

	print("Hasil Pencarian Anda : ")
	nomor = 1
	for film in finded_item:
		print(nomor, ".", film["title"], ", Genre : ", film["genre"])
		nomor += 1
	input()
	return finded_item

def tampil_watching_list(user_data):
	os.system("cls")
	print("------------Watching List--------------")
	Watching_List =  user_data.get("watching_list",[])
	if len(Watching_List) == 0 :
		print("Watching List kosong")
		print("-------------------------------------------")
	else:
		nomor = 1
		for film in Watching_List:
			print(nomor, ".", film)
			nomor += 1
		print("-------------------------------------------")

def tambah_watching_list(user_data, users):
	os.system("cls")
	print("Tambah Film ke dalam Watching List")
	hasil_yang_dicari = Linear_Search_Film()
	if len(hasil_yang_dicari)== 0:
		return

	while True:
		try:
			pilihan = int(input("Pilih film yang ingin Anda tambahakan (1-%d) : " %(len(hasil_yang_dicari))))
		except ValueError:
			print("Inputnya harus Angka.")
			continue
		if pilihan>=1 and pilihan <= len(hasil_yang_dicari):
			judul_watching_list = hasil_yang_dicari[pilihan-1]["title"]
			if judul_watching_list in user_data["watching_list"]:
				print("film sudah pernah terdaftar di watching list")
				input()
				return
			else:
				user_data["watching_list"].append(judul_watching_list)
				print("Film", judul_watching_list, "ditambahkan ke watching list")
				print("---------------------------------------------------------")
				input()
				save_data_user(users)
				return
		else:
			print("Pilihan Tidak Sesuai, Silahkan Coba Lagi")

def hapus_watching_list(user_data, users):
	os.system("cls")
	tampil_watching_list(user_data)
	print("Hapus Film dari Watching List")
	Watching_List = user_data.get("watching_list",[])
	if len(Watching_List)== 0:
		print("Tolol kau!! Uong katek Film di watching list kau!!!!")
		# print("Tidak ada film yang anda bisa hapus")
		print("Tekan 'ENTER' untuk Kembali")
		input()
		return
	while True:
		try:
			pilihan = int(input("Pilih film yang ingin Anda hapus (1-%d) : " %(len(Watching_List))))
		except ValueError:
			print("Inputnya harus Angka.")
		if pilihan>=1 and pilihan <= len(Watching_List):
			Hapus = Watching_List.pop(pilihan-1)
			print("Film", Hapus, "telah dihapus dari Watching List")
			print("---------------------------------------------------------")
			input()
			save_data_user(users)
			return
		else:
			print("Pilihan Tidak Sesuai, Silahkan Coba Lagi")


def Fitur_Stack_Kosong():
	return len(watched_stack) == 0

def Fitur_Stack_Push():
	hasil_yang_dicari = Linear_Search_Film()
	if len(hasil_yang_dicari)== 0:
		print("Tekan 'ENTER' untuk Kembali")
		input()
		return

	while True:
		try:
			pilihan = int(input("Pilih film yang ingin Anda tambahakan (1-%d) : " %(len(hasil_yang_dicari))))
		except ValueError:
			print("Inputnya harus Angka.")
			continue
		if pilihan>=1 and pilihan <= len(hasil_yang_dicari):
			Judul_Film = hasil_yang_dicari[pilihan-1]["title"]
			watched_stack.append(Judul_Film)
			print("Film", Judul_Film, "telah ditambahkan ke History Tontonan")
			print("Tekan 'ENTER' untuk Kembali")
			input()
			break
		else:
			print("Pilihan Tidak Sesuai, Silahkan Coba Lagi")
			print("Tekan 'ENTER' untuk Kembali")
			input()

def Fitur_Stack_Hapus():
	if not Fitur_Stack_Kosong():
		hapus = watched_stack.pop()
		print("Film", hapus, "telah dihapus dari History Tontonan")
		print("Tekan 'ENTER' untuk Kembali")
		input()
		return hapus
	else:
		print("History Anda Kosong")
		print("Tekan 'ENTER' untuk Kembali")
		input()

def Fitur_Stack_Cek():
	if not Fitur_Stack_Kosong():
		list_film_akhir = watched_stack[-1]
		print("Film terakhir yang ditonton : ", list_film_akhir)
		print("Tekan 'ENTER' untuk Kembali")
		input()
	else:
		print("Lu Belum Tonton apapun Cok Mau Liat apaaaaaaa!!!!!")
		print("Tekan 'ENTER' untuk Kembali")
		input()

def Cek_Seluruh_History():
	if Fitur_Stack_Kosong():
		print("Ga Capek Bang Cek History Mulu, Nonton dlu lah Baru Cek History")
		print("Tekan 'ENTER' untuk Kembali")
		input()
	else:
		print("---------------Seluruh History Tontonan---------------------")
		i = 1
		for film in watched_stack:
			print(i,".", film)
			i += 1
		print("Tekan 'ENTER' untuk Kembali")
		input()

def Fitur_Tambah_Queue(user_data, username, users):
	os.system("cls")
	data_user = users[username]
	Watching_List = user_data.get("watching_list", [])
	if len(Watching_List)== 0:
		print("Tolol kau!! Uong katek Film di watching list kau!!!!")
		# print("Tidak ada film yang anda bisa hapus")
		print("Tekan 'ENTER' untuk Kembali")
		input()
		return
	while True:
		tampil_watching_list(data_user)
		try:
			pilihan = int(input("Pilih film yang ingin Anda Tonton (1-%d) : " %(len(Watching_List))))
		except ValueError:
			print("Inputnya harus Angka.")
			continue
		if pilihan>=1 and pilihan <= len(Watching_List):
			Queue_Film = Watching_List[pilihan-1]
			Watched_Queue.append(Queue_Film)
			# watched_stack.append(Queue_Film)
			print("Film", Queue_Film, "telah masuk ke Antrian")
			print("Tekan 'ENTER' untuk Kembali")
			input()

			return
		else:
			print("Pilihan Tidak Sesuai, Silahkan Coba Lagi")

def tampil_Queue():
	os.system("cls")
	if len(Watched_Queue) == 0:
		print("Kau Tolol, Belum lah kau masukken ke Antrian tuh Film, Pergi Sana Masukkan Dlu")
		print("Tekan 'ENTER' untuk Kembali")
		input()
	else:
		print("-------------------------------Queue Tontonan---------------------")
		nomor = 1
		for film in Watched_Queue:
			print(nomor, ".", film)
			nomor += 1
		x = 1
		print("Anda Sedang Menonton :")
		print(x, ".", Watched_Queue[0])
		print("Tekan 'ENTER' untuk Kembali")
		input()

def Fitur_Kurang_Queue():
	if len(Watched_Queue) == 0:
		print("Kau Tolol, Belum ada Antrian, Nak kau apus, Hadueh!!!!!!!!!")
	else:
		film_terhapus = Watched_Queue.pop(0)
		watched_stack.append(film_terhapus)
		print("Film", film_terhapus, "telah terhapus dari Queue")
	print("Tekan 'ENTER' untuk Kembali")
	input()




def Menu_History():
	while True:
		os.system("cls")
		print("----------------History Tontonan---------------------")
		print("1. Cek History Terakhir")
		print("2. Cek Seluruh History")
		print("3. Hapus History Terakhir")
		print("4. Back")
		pilihan = input("Masukkan Opsi Anda: ")
		if pilihan == "1":
			Fitur_Stack_Cek()
		elif pilihan == "2":
			Cek_Seluruh_History()
		elif pilihan == "3":
			Fitur_Stack_Hapus()
		elif pilihan == "4":
			break
		else:
			print("Pilihan Tidak Sesuai, Silahkan Coba Lagi")
			print("Tekan 'ENTER' untuk Kembali")
			input()

def Pilihan_Queue():
	while True:
		os.system("cls")
		print("--------------------Menu Tontonan---------------------")
		print("1. Lihat Yang anda sedang Tonton")
		print("2. Hapus yang anda Tonton")
		print("3. Keluar")
		pilihan = input("Masukkan Opsi Anda: ")
		if pilihan == "1":
			tampil_Queue()
		elif pilihan == "2":
			Fitur_Kurang_Queue()
		elif pilihan == "3":
			return
		else:
			print("Pilihan Tidak Sesuai, Silahkan Coba Lagi")
			print("Tekan 'ENTER' untuk Kembali")
			input()





def Pilihan_Watching_List(username, user_data, users):
	while True:
		os.system("cls")
		data_user = users[username]
		tampil_watching_list(data_user)
		print("1. Tambah Watching List")
		print("2. Hapus Watching List")
		print("3. Masukkan Film Untuk di Tonton")
		print("4. Keluar")
		pilihan = input("Masukkan Opsi Anda: ")
		if pilihan == "1":
			tambah_watching_list(user_data, users)
		elif pilihan == "2":
			hapus_watching_list(user_data, users)
		elif pilihan == "3":
			Fitur_Tambah_Queue(user_data, username, users)
		elif pilihan == "4":
			return
		else:
			print("Pilihan Tidak Sesuai, Silahkan Coba Lagi")
			print("Tekan 'ENTER' untuk Kembali")
			input()


def MainMenu(username, users):
	os.system("cls")
	data_user = users[username]
	while True:
		os.system("cls")
		print("-----------------------Selamat Datang di OurTv-------------------------")
		print("1. Lihat Daftar Genre")
		print("2. Cari Film")
		print("3. Lihat Watching List")
		print("4. Lihat Anda Sedang Menonton Apa")
		print("5. Menu History")
		print("6. Logout")
		pilihan = input("Pilih Opsi (1-6): ")
		if pilihan == "1":
			tampil_genre(genre_terurut)
		elif pilihan == "2":
			Linear_Search_Film()
		elif pilihan == "3":
			Pilihan_Watching_List(username, data_user, users)
		elif pilihan == "4":
			Pilihan_Queue()
		elif pilihan == "5":
			Menu_History()
		elif pilihan == "6":
			print(username, "Telah Logout dari Program")
			print("Tekan 'ENTER' untuk Lanjut")
			input()
			break
		else:
			print("Pilihan Tidak Sesuai, Silahkan Coba Lagi")
			print("Tekan 'ENTER' untuk Kembali")
			input()


def MenuLogin ():
	os.system("cls")
	users = Cek_Data_User()
	print("----------------------Selamat Datang di OurTv-------------------------")
	while True:
		os.system("cls")
		print("Menu Login:")
		print("1. Login")
		print("2. SignUp")
		print("3. Keluar")
		pilihan = input("Pilih Opsi (1-3): ")
		if pilihan == "1":
			username = sign_in(users)
			if username != None:
				MainMenu(username, users)
		elif pilihan == "2":
			username = sign_up(users)
			if username != None:
				MainMenu(username, users)
		elif pilihan == "3":
			print("Terima Kasih Telah Menggunakan Program Kami")
			break
		else:
			print("Pilihan Tidak Sesuai, Silahkan Coba Lagi")
			print("Tekan 'ENTER' untuk Kembali")
			input()

FILMS = [
	{"title": "Crash Landing on You", "genre": "Drama"},
	{"title": "Vincenzo", "genre": "Drama"},
	{"title": "Descendants of the Sun", "genre": "Drama"},
	{"title": "The Untamed", "genre": "Drama"},
	{"title": "Heaven Official's Blessing", "genre": "Drama"},
	{"title": "My Girlfriend is an Alien", "genre": "Comedy"},
	{"title": "Reply 1988", "genre": "Comedy"},
	{"title": "Mo Dao Zu Shi", "genre": "Donghua"},
	{"title": "Scissor Seven", "genre": "Donghua"},
	{"title": "Naruto", "genre": "Anime"},
	{"title": "One Piece", "genre": "Anime"},
	{"title": "Demon Slayer", "genre": "Anime"},
	{"title": "Attack on Titan", "genre": "Anime"},
	{"title": "Hometown Cha Cha", "genre": "Drama"},
	{"title": "Big Mouth", "genre": "Thriller"},
	{"title": "Cheer Up", "genre": "Romance"},
	{"title": "Heavenly Idol", "genre": "Fantasy"},
	{"title": "Shooting Star", "genre": "Romance"},
	{"title": "My Demon", "genre": "Fantasy"},
	{"title": "Marry My Husband", "genre": "Romance"},
	{"title": "Love In Contract", "genre": "Romance"},
	{"title": "More Than Friend", "genre": "Romance"},
	{"title": "Welcome to Samldari", "genre": "Romance"},
	{"title": "Strong Dong Bong Soon", "genre": "Action"},
	{"title": "See You in My 19th Life", "genre": "Fantasy"},
	{"title": "King The Land", "genre": "Romance"},
	{"title": "Glory", "genre": "Drama"},
	{"title": "Backstreet Rookie", "genre": "Romance"},
	{"title": "Doctor Cha", "genre": "Medical"},
	{"title": "Death Game", "genre": "Thriller"},
	{"title": "Love Next Door", "genre": "Romance"},
	{"title": "Perfect Family", "genre": "Family"},
	{"title": "My Roommate Is Gumiho", "genre": "Fantasy"},
	{"title": "The Fiery Priest", "genre": "Action"},
	{"title": "Alchemy Soul", "genre": "Fantasy"},
	{"title": "Seoul Buster", "genre": "Action"},
	{"title": "Welcome to Waikiki", "genre": "Comedy"},
	{"title": "Work later, drink now", "genre": "Comedy"},
	{"title": "Hospital Playlist", "genre": "Medical"},
	{"title": "18 Again", "genre": "Fantasy"},
	{"title": "Gaus Electronic", "genre": "Comedy"},
	{"title": "Vincenzo", "genre": "Crime"},
	{"title": "Mr Queen", "genre": "Historical"},
	{"title": "Extracurricular", "genre": "Crime"},
	{"title": "Save Me", "genre": "Thriller"},
	{"title": "Flower of Evil", "genre": "Crime"},
	{"title": "Love Song For Illustion", "genre": "Fantasy"},
	{"title": "Celebrity", "genre": "Drama"},
	{"title": "Queen Of Divorce", "genre": "Comedy"},
	{"title": "The Atypically Family", "genre": "Fantasy"},
	{"title": "Doctor Slump", "genre": "Medical"},
	{"title": "Reply 1988", "genre": "Family"},
	{"title": "Penthouse", "genre":"Drama"},
	{"title": "WitchWatch", "genre": "Anime"},
	{"title": "Jojo Bizzare Adventure", "genre": "Anime"},
	{"title": "The Apothecary Diaries", "genre": "Anime"},
	{"title": "Rising Impact", "genre": "Anime"},
	{"title": "Baki Hanma", "genre": "Anime"},
	{"title": "Rising Impact", "genre": "Anime"},
	{"title": "Rurouni Kenshin", "genre": "Anime"},
	{"title": "Classroom Of The Elite", "genre": "Anime"},
	{"title": "That Time I Get Reincarnated as a Slime", "genre": "Anime"},
	{"title": "Buddy Daddies", "genre": "Anime"},
	{"title": "Bungo Stray Dogs", "genre":"Anime"},
	{"title": "Violet Evergarden", "genre": "Anime"},
	{"title": "Kaiju No8", "genre": "Anime"},
	{"title": "Wind Breaker", "genre": "Anime"},
	{"title": "Solo Leveling", "genre": "Anime"},
	{"title": "Jujutsu Kaisen", "genre": "Anime"},
	{"title": "Tokyo Revengers", "genre": "Anime"},
	{"title": "Spy x Family", "genre": "Anime"},
	{"title": "One Punch Man", "genre": "Anime"},
	{"title": "Haikyuu!!", "genre": "Anime"},
	{"title": "Dr. Stone", "genre": "Anime"},
	{"title": "Doraemon", "genre":"Anime"},
	{"title": "Battle Through the Havens", "genre": "Mystery"},
	{"title": "Renegade Immortal", "genre": "Fantasy"},
	{"title": "Perfect World", "genre": "Fantasy"},
	{"title": "Throne of Seal", "genre": "Fantasy"},
	{"title": "Supreme God Emperor", "genre": "Advanture"},
	{"title": "Martial Master", "genre": "Reincarnation"},
	{"title": "Tales of Herding Gods", "genre": "Action"},
	{"title": "Soul Land 1", "genre": "Reincarnation"},
	{"title": "Against the Gods", "genre": "Reincarnation"},
	{"title": "Sage Ancestor", "genre": "Isekai"},
]


variant_genre = ambil_genre_unik(FILMS)
genre_terurut = quick_sort(variant_genre)
MenuLogin()