from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def encrypt(wallet):

	key = get_random_bytes(16)
	# print("key:", key)
	cipher = AES.new(key, AES.MODE_EAX)

	# wallet = open("./wallet.txt", mode="rb")
	# wallet = wallet.read()
	ciphertext, tag = cipher.encrypt_and_digest(wallet)

	file_out = open("encrypted_wallet.bin", "wb")
	[ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]

	return key

def decrypt(wallet, key):
	# print(key.decode())
	# file_in = open(wallet, "rb")
	nonce, tag, ciphertext = [ wallet.read(x) for x in (16, 16, -1) ]

	cipher = AES.new(key, AES.MODE_EAX, nonce)
	data = cipher.decrypt_and_verify(ciphertext, tag)

	plain_wallet = open("plain_decrypted_wallet.txt", "wb+")

	plain_wallet.write(data)