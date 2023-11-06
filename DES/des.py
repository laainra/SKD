# from Crypto.Cipher import DES3
# from Crypto.Util.Padding import pad, unpad
# from Crypto.Random import get_random_bytes

# # Generate a random 24-byte TDES key
# key = get_random_bytes(24)

# BLOCK_SIZE = 8

# # Create a TDES cipher object for encryption
# des = DES3.new(key, DES3.MODE_ECB)

# # Input message
# message = input("Enter the message: ")

# # Convert the message to bytes and pad it
# message_bytes = message.encode()
# padded_message = pad(message_bytes, BLOCK_SIZE)

# # Encrypt the message
# encrypted_message = des.encrypt(padded_message)

# print("Original Message: ", message)
# print("Encrypted Message: ", encrypted_message)

# # Decrypt the message using the same key
# des = DES3.new(key, DES3.MODE_ECB)
# decrypted_message = des.decrypt(encrypted_message)

# # Unpad the decrypted message and convert it back to a string
# unpadded_message = unpad(decrypted_message, BLOCK_SIZE)
# decrypted_text = unpadded_message.decode()

# print("Decrypted Message: ", decrypted_text)

# from Crypto.Cipher import DES3
# from Crypto.Util.Padding import pad, unpad
# from Crypto.Random import get_random_bytes

# # Input the 24-byte TDES key as ASCII characters
# key_input = input("Enter the 24-byte TDES key (24 ASCII characters): ")
# if len(key_input) != 24:
#     print("Key must be exactly 24 characters long.")
#     exit()

# key = key_input.encode()

# BLOCK_SIZE = 8

# # Create a TDES cipher object for encryption
# des = DES3.new(key, DES3.MODE_ECB)

# # Input message
# message = input("Enter the message: ")

# # Convert the message to bytes and pad it
# message_bytes = message.encode()
# padded_message = pad(message_bytes, BLOCK_SIZE)

# # Encrypt the message
# encrypted_message = des.encrypt(padded_message)

# print("Original Message: ", message)
# print("Encrypted Message: ", encrypted_message)

# # Decrypt the message using the same key
# des = DES3.new(key, DES3.MODE_ECB)
# decrypted_message = des.decrypt(encrypted_message)

# # Unpad the decrypted message and convert it back to a string
# unpadded_message = unpad(decrypted_message, BLOCK_SIZE)
# decrypted_text = unpadded_message.decode()

# print("Decrypted Message: ", decrypted_text)
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Input the 8-byte DES key as ASCII characters
key_input = input("Enter the 8-byte DES key (ASCII characters): ")
if len(key_input) < 8:
    print("Key is less than 8 characters. Padding with spaces.")
    key_input = key_input.ljust(8)

if len(key_input) > 8:
    print("Key is longer than 8 characters. Truncating to 8 characters.")
    key_input = key_input[:8]

key = key_input.encode()

BLOCK_SIZE = 8

# Create a DES cipher object for encryption
des = DES.new(key, DES.MODE_ECB)

# Input message
message = input("Enter the message: ")

# Convert the message to bytes and pad it
message_bytes = message.encode()
padded_message = pad(message_bytes, BLOCK_SIZE)

# Encrypt the message
encrypted_message = des.encrypt(padded_message)

print("Original Message: ", message)
print("Encrypted Message: ", encrypted_message)

# Decrypt the message using the same key
des = DES.new(key, DES.MODE_ECB)
decrypted_message = des.decrypt(encrypted_message)

# Unpad the decrypted message and convert it back to a string
unpadded_message = unpad(decrypted_message, BLOCK_SIZE)
decrypted_text = unpadded_message.decode()

print("Decrypted Message: ", decrypted_text)

