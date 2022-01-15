plaintext = input()
ciphertext = input()
ciphertext2 = input()

cipher_to_plain = {}

for i in range(len(plaintext)):
    cipher_to_plain[ciphertext[i]] = plaintext[i]

plaintext2 = ''

for char in ciphertext2:
    if char in cipher_to_plain:
        plaintext2 = plaintext2 + cipher_to_plain[char]
    else:
        plaintext2 = plaintext2 + '.'

print(plaintext2)
