# Mengimpor modul DES dari pustaka Crypto
from Crypto.Cipher import DES

# Mengimpor fungsi pad dan unpad dari modul Crypto.Util.Padding
from Crypto.Util.Padding import pad, unpad

# Mengimpor fungsi get_random_bytes dari modul Crypto.Random
from Crypto.Random import get_random_bytes

# Memasukkan kunci DES 8 byte sebagai karakter ASCII
key_input = input("Masukkan kunci DES 8 byte (karakter ASCII): ")

# Jika panjang kunci kurang dari 8, lakukan padding dengan spasi
if len(key_input) < 8:
    print("Kunci kurang dari 8 karakter. Melakukan padding dengan spasi.")
    key_input = key_input.ljust(8)

# Jika panjang kunci lebih dari 8, trunikasi menjadi 8 karakter
if len(key_input) > 8:
    print("Kunci lebih dari 8 karakter. Mentrunkasi menjadi 8 karakter.")
    key_input = key_input[:8]

# Mengubah kunci menjadi format byte
key = key_input.encode()

# Ukuran blok DES diatur ke 8 byte
BLOCK_SIZE = 8

# Membuat objek kriptografi DES untuk enkripsi
des = DES.new(key, DES.MODE_ECB)

# Memasukkan pesan
message = input("Masukkan pesan: ")

# Mengonversi pesan menjadi byte dan melakukan padding
message_bytes = message.encode()
padded_message = pad(message_bytes, BLOCK_SIZE)

# Melakukan enkripsi pesan
encrypted_message = des.encrypt(padded_message)

# Menampilkan pesan asli dan pesan terenkripsi
print("Pesan Asli: ", message)
print("Pesan Terenkripsi: ", encrypted_message)

# Mendeskripsi pesan menggunakan kunci yang sama
des = DES.new(key, DES.MODE_ECB)
decrypted_message = des.decrypt(encrypted_message)

# Menghilangkan padding dari pesan terdekripsi dan mengonversi kembali ke string
unpadded_message = unpad(decrypted_message, BLOCK_SIZE)
decrypted_text = unpadded_message.decode()

# Menampilkan pesan terdekripsi
print("Pesan Terdekripsi: ", decrypted_text)
