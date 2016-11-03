msg = raw_input ('What would you like to encrypt/decrypt today?')
key = int(raw_input ('What is your key for your caesar cipher?'))
mode =  raw_input('Would you like to decrypt or encrypt your message?')
mode = mode.lower()
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = ''
# capital type string in msg
msg = msg.upper()

print(msg)

# run the encryption/decryption code on each symbol in the msg string
for symbol in msg:
    if symbol in ALPHABET:
        # get the encrypted (or decrfypted) number for this symbol
        num = ALPHABET.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
# handlde the wrap-around if num is larger than the length of
#ALPHABET or less than 0 
        if num >= len (ALPHABET):
            num = num - len(ALPHABET)
        elif num < 0:
            num = num + len(ALPHABET)


        # add encrypted/decrypted number's symbol at the end of the result
        result = result + ALPHABET[num]
    else:
    # just add the symbol without decrypting/encrypting
        result = result + symbol
# print tyhe encrypted/decrypted string to the string
print(result)
