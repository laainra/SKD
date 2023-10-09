import string # import module string yang akan digunakan

def encrypt(input): # membuat function encrypt dengan parameter inpput dan key
    res =  "" # mendeklarasikan varibael dengan value awal string kosong 
    key = 24 # mendeklarasikan variabel key utnuk pergeseran sebanyak nomer absen (24)
    for x in range(len(input)): # membuat loop for yang mengulang sebanyak panjang karkater yang diinputkan
        char = input[x] # mendeklarasikan variabel yang berisikan karakter pada indeks ke - x

        if char.isalpha():  # mmebuat pengkondisian untuk memeriksa apakah karakter adalah huruf/alfabet
            if char.isupper():  # membuat pengkondisian untuk memeriksa apakah karakter adalah huruf kapital
                hasil = string.ascii_uppercase.index(char) + key  # mendeklarasikan variabel hasil untuk menemukan indeks huruf di alfabet kapital dengan cara menjumlahkan dengan nilai key 
                hasil = hasil % 26  # Menggunakan modulus 26 agar tidak melebihi jumlah huruf
                res += string.ascii_uppercase[hasil]  # menggunakan operator assignment untuk menambahkan huruf kapital yang sudah dienkripsi ke dalam variabel res
            else: # jika karakter huruf kecil maka akan menjalankan kondisi berikut
                hasil = string.ascii_lowercase.index(char) + key   # mendeklarasikan variabel hasil untuk menemukan indeks huruf di alfabet kapital dengan cara menjumlahkan dengan nilai key 
                hasil = hasil % 26  # Menggunakan modulus 26 agar tidak melebihi jumlah huruf
                res += string.ascii_lowercase[hasil]  # menggunakan operator assignment untuk menambahkan huruf kecil yang sudah dienkripsi ke dalam variabel res
        else: # jika bukan huruf alfabet / berupa karakter simbol maka akan menjalanakn kondisi berikut:
            
            ascii_code = ord(char) + key  # mengubah karakter ke dalam kode ASCII karakter dan menambahkannya dengan key
            if ascii_code > 127: # jika kode ascii lebih dari 127 maka akan menjalanakan kondisi berikut
                ascii_code = ascii_code - 127 + 32  # Menggunakan modulus 127 dan menjumlahkan dengan 32 jika melebihi 127 (karena kode ascii 0-31 bukanlan printable karakter)
            res += chr(ascii_code)  # Menambahkan karakter yang sudah dienkripsi ke dalam variabel res

    return res # mengembalikan nilai result

def decrypt(input): # membuat function encrypt dengan parameter inpput dan key
    res = "" # mendeklarasikan varibael dengan value awal string kosong 
    key = 24 # mendeklarasikan variabel key utnuk pergeseran sebanyak nomer absen (24)
    for x in range(len(input)): # membuat loop for yang mengulang sebanyak panjang karkater yang diinputkan
        char = input[x] # mendeklarasikan variabel yang berisikan karakter pada indeks ke - x

        if char.isalpha():  # membuat pengkondisian untuk memeriksa apakah karakter adalah huruf kapital
            if char.isupper():  # Memeriksa apakah karakter adalah huruf kapital
                hasil = string.ascii_uppercase.index(char) - key  # mendeklarasikan variabel hasil untuk menemukan indeks huruf di alfabet kapital dengan cara mengurangi dengan nilai key 
                hasil = hasil % 26  # Menggunakan modulus 26 agar tidak melebihi jumlah huruf
                res += string.ascii_uppercase[hasil]  # menggunakan operator assignment untuk menambahkan huruf kapital yang sudah dienkripsi ke dalam variabel res
            else: # jika karakter huruf kecil maka akan menjalankan kondisi berikut
                hasil = string.ascii_lowercase.index(char) - key  # mendeklarasikan variabel hasil untuk menemukan indeks huruf di alfabet kapital dengan cara mengurangi dengan nilai key 
                hasil = hasil % 26  # Menggunakan modulus 26 agar tidak melebihi jumlah huruf
                res += string.ascii_lowercase[hasil]  # menggunakan operator assignment untuk menambahkan huruf kecil yang sudah dienkripsi ke dalam variabel res
        else: # jika bukan huruf alfabet / berupa karakter simbol maka akan menjalanakn kondisi berikut:
            ascii_code = ord(char) - key  # mengubah karakter ke dalam kode ASCII karakter dan mengurangkan dengan key
            if ascii_code < 32: # jika kode ascii lebih dari 127 maka akan menjalanakan kondisi berikut
                ascii_code = ascii_code + 127 - 32  # Menggunakan modulus 127 dan mengurngkan dengan 32 jika melebihi 127 (karena kode ascii 0-31 bukanlan printable karakter)
            res += chr(ascii_code)  # Menambahkan karakter yang sudah didekripsi ke dalam variabel res

    return res # mengembalikan nilai result

while True: # ketika kondisi benar maka akan mennjalankan kode berikut:
    print("Pilih operasi:") # membuat pilihan input user untuk memilih enkripsi atau dekripsi
    print("1. Enkripsi")
    print("2. Dekripsi")
    print("3. Keluar")

    choice = input("Masukkan pilihan (1/2/3): ") # membuat variabel choice yang menyimpan inputan user

    if choice == '1': # jika inputan user bernilai 1 maka akan menjalanakan fungsi enkripsi
        plaintext = input("Masukkan teks yang akan dienkripsi: ") # mendeklarasikan variabel plainteks untuk menyimpan teks yang diinput user untuk di enkripsi

        encrypted_text = encrypt(plaintext) # mendeklarasikan variabel encrypted_text untuk menyimpan nilai dari fungsi encrypt
        print("Teks terenkripsi:", encrypted_text) # menammpilkan hasil enkripsi
    elif choice == '2':  # jika inputan user bernilai 2 maka akan menjalanakan fungsi dekripsi
        encrypted_text = input("Masukkan teks yang akan didekripsi: ")  # mendeklarasikan variabel encrypted_text untuk menyimpan teks yang diinput user untuk di dekripsi 
        decrypted_text = decrypt(encrypted_text) # mendeklarasikan variabel decrypted_text untuk menyimpan nilai dari fungsi decrypt
        print("Teks terdekripsi:", decrypted_text) # menammpilkan hasil dekripsi
    elif choice == '3':  # jika inputan user bernilai 2 maka program  akan berhenti
        break
    else: # jika inputan user bernilai selain 1 2 3 maka akan muncul pesan kesalahan
        print("Pilihan tidak valid.")
