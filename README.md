# bitcoin-wallet-protector
This is a commandline tool to encrypt your bitcoin wallet (or any message) and then hide the encryption key in an image that requires password to decrypt. This can be used to keep your wallet in somewhere unsafe like Google Drive and you'll only have to remember your password.

# Usage

To encrypt your wallet
btcwalletprotector encrypt -w testwallet.txt -p password

To decrypt your wallet
btcwalletprotector decrypt -w encrypted_wallet.bin -p password

When you encrypt your wallet, it'll create certain files. You need to take care of encrypted_wallet.bin and definitely_not_a_key.jpg. The image file contains your encryption keys which are hidden in that image. To decrypt that key, you'll need that password, so keep that password long and secure. Make sure you test everything.

If you get UnicodeError, just try again. Make sure you test both encrypt and decrypt.

# Dependencies
- Python 3.x

- pycryptodome

- steghide (commandline tool)

The encryption used is AES in EAX mode.

# Tested on Linux and Windows 10.
