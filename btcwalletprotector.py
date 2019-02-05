import sys
import subprocess
from encryptdecrypt import encrypt, decrypt

if __name__ == "__main__":
	args = sys.argv[2:]
	arguments = {}

	i=0
	while i in range(len(args)):
		if i % 2 == 0:
			if args[i][0] == '-':
				arguments[args[i]] = args[i + 1]
		i += 1

	# print(arguments)

	### getting arguments - done.

	if sys.argv[1] == 'encrypt':
		
		wallet_file = open(arguments['-w'], mode='rb')
		password = arguments['-p']
		
		key = encrypt(wallet_file.read())
		key = key.decode('cp1252') #Windows-1252 or CP-1252 is a single-byte character encoding of the Latin alphabet, used by default in the legacy components of Microsoft Windows in English and some other Western languages
		print("Key: ", key)

		key_file = open("key.txt", mode="w+")
		key_file.write(key)

		wallet_file.close()
		key_file.close()

		print(subprocess.check_output(['steghide', 'embed', '-ef', 'key.txt', '-cf', 'wide_geralt.jpg', '-sf', 'definitely_not_a_key.jpg', '-p', password]))

		print("\n\nDone.")
		print("\nYou can now store encrypted_wallet.bin and definitely_not_a_key.jpg anywhere you want. You can even keep the encrypted wallet and protected key in Google Drive because the only way anyone could decrypt this wallet is with the password you entered. Make sure the password was long enough to be secure. I suggest it should atleast be 12 characters long to be considered secure and not be in use somewhere else.")
		
	elif sys.argv[1] == 'decrypt':
		
		wallet_file = open(arguments['-w'], mode='rb')
		password = arguments['-p']

		print(subprocess.check_output(['steghide', 'extract', '-sf', 'definitely_not_a_key.jpg', '-xf', 'key_decrypted.txt', '-p', password]))
		print("\n---> key decrypted.")

		key_file = open("key_decrypted.txt", "rb")
		key = key_file.read()
		# print(key)
		# key = key.encode()
		# print(key)
		print("lenght of key:", len(key))
		decrypt(wallet_file, key)

		print("\n\nwallet decrypted: ./plain_decrypted_wallet.txt")
		
		wallet_file.close()
		key_file.close()		

	elif sys.argv[1] == '-h':
		print("Keep you wallet file (preferably in txt) with you and run this command to encrypt your wallet:")
		print("btcwalletprotector encrypt -w wallet.txt -p YourVeryLongAndHardPassword")
		print("\nThis will create centain files. You need to take care of encrypted_wallet.bin and definitely_not_a_key.jpg which your key hidden in password protected image form. You can now keep those 2 files in somewhere convenient like Google Drive. All you need to remember is the password.")
		print("\nMake sure your password is long enough to be secure. It should atleast be 12 characters long. Think of them as passphrases. You can make your passphrase long like \"margretthatcherisa100%sexy\".")

		print("\n\nTo decrypt your wallet, run this command:")
		print("btcwalletprotector decrypt -w encrypted_wallet.bin -p YourVeryLongAndHardPassword")
		print("\nMake sure you test everything.")
	else:
		print("No command: " + sys.argv[1])