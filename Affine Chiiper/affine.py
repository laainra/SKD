# Extended Euclidean Algorithm untuk mencari inversi modulo
def egcd(a, b):  # Fungsi egcd dengan parameter a dan b
    x, y, u, v = 0, 1, 1, 0  # Inisialisasi variabel x, y, u, v
    while a != 0:  # Selama a tidak sama dengan 0
        q, r = b // a, b % a  # Menghitung hasil bagi q dan sisa r dari b dibagi a
        m, n = x - u * q, y - v * q  # Menghitung nilai m dan n
        b, a, x, y, u, v = a, r, u, v, m, n  # Memperbarui nilai variabel
    gcd = b  # Nilai terakhir dari b adalah gcd (Greatest Common Divisor, Faktor Persekutuan Terbesar)
    return gcd, x, y  # Mengembalikan gcd dan nilai x, y yang merupakan koefisien invers modulo


def modinv(a, m):
    gcd, x, y = egcd(a, m)  # Menggunakan fungsi egcd yang telah didefinisikan sebelumnya
    if gcd != 1:  # Jika gcd (Faktor Persekutuan Terbesar) tidak sama dengan 1, maka inversi modulo tidak ada
        return None # inversi modulo tidak ada
    else:
        return x % m  # Mengembalikan hasil inversi modulo dari `a` terhadap `m`


# Fungsi enkripsi cipher Affine
def affine_encrypt(text, key):
    # Formula enkripsi Affine: C = (a*P + b) % 26

    # Pertama, teks diubah menjadi huruf kapital dan spasi dihapus
    text = text.upper().replace(' ', '')

    # Kemudian, setiap karakter dalam teks dienkripsi sesuai rumus Affine
    encrypted_characters = [(key[0] * (ord(char) - ord('A')) + key[1]) % 26 + ord('A') for char in text]

    # Hasil enkripsi digabungkan menjadi string
    encrypted_text = ''.join([chr(char) for char in encrypted_characters])

    return encrypted_text


# Fungsi dekripsi cipher Affine
def affine_decrypt(cipher, key):
    # Formula dekripsi Affine: P = (a^-1 * (C - b)) % 26

    # Setiap karakter dalam teks terenkripsi dienkripsi kembali menjadi teks asli
    decrypted_characters = [(modinv(key[0], 26) * (ord(char) - ord('A') - key[1])) % 26 + ord('A') for char in cipher]

    # Hasil dekripsi digabungkan menjadi string
    decrypted_text = ''.join([chr(char) for char in decrypted_characters])

    return decrypted_text

# Program Utama
def main():
    # Input teks dan kunci dari pengguna
    text = input("Masukkan teks yang akan dienkripsi: ")  # Meminta pengguna untuk memasukkan teks yang akan dienkripsi.
    a = int(input("Masukkan nilai a (integer yang relatif prima dengan 26): "))  # Meminta pengguna untuk memasukkan nilai a dari kunci Affine.
    b = int(input("Masukkan nilai b (integer): "))  # Meminta pengguna untuk memasukkan nilai b dari kunci Affine.

    # Periksa apakah a adalah relatif prima dengan 26
    if modinv(a, 26) is None:  # Memeriksa apakah a adalah relatif prima dengan 26 dengan menggunakan fungsi modinv.
        print("Nilai a harus relatif prima dengan 26.")  # Pesan kesalahan jika a bukan relatif prima dengan 26.
        return

    key = [a, b]

    # Enkripsi teks input
    teks_terenkripsi = affine_encrypt(text, key)  # Memanggil fungsi affine_encrypt untuk mengenkripsi teks input.
    print("Teks Terenkripsi: {}".format(teks_terenkripsi))  # Menampilkan teks terenkripsi ke layar.

    # Dekripsi teks terenkripsi
    teks_terdekripsi = affine_decrypt(teks_terenkripsi, key)  # Memanggil fungsi affine_decrypt untuk mendekripsi teks terenkripsi.
    print("Teks Terdekripsi: {}".format(teks_terdekripsi))  # Menampilkan teks terdekripsi ke layar.

if __name__ == '__main__':
    main()

