import math
def encrypt_exponential(plaintext, base, modulus):
    # define ciphertext as an empty string
    ciphertext = ""
    
    # remove all spaces from plaintext
    plaintext = plaintext.replace(" ", "")

    # to calculate m param
    m = int(math.log10(modulus)) - 1
    
    # split plaintext into blocks of size 2m
    blocks = [plaintext[i:i+m] for i in range(0, len(plaintext), m)]
    if (len(blocks[-1]) == 1):
        blocks[-1] += 'X'

    # loop for each block in the plaintext
    for block in blocks:
        
        # empty string
        encrypted_block = ""

        # loop for each character in the block
        for char in block:
            # check if the character is an alphabet
            if char.isalpha():

                # The same with encrypt_caesar
                ascii_offset = ord('A') if char.isupper() else ord('a')

                # The formula for exponential cipher is (x^base) mod modulus
                normal_char = ord(char) - ascii_offset

                # if the encrypted_char is a single digit number, add a leading zero
                if 0 <= normal_char <= 9:
                    encrypted_block += '0' + str(normal_char)
                else:
                    encrypted_block += str(normal_char)
            
        
        encrypted_number = pow(int(encrypted_block), base, modulus)
        if(len(str(encrypted_number)) < 2*m):
            encrypted_number = "0"*(2*m - len(str(encrypted_number))) + str(encrypted_number)
        ciphertext += str(encrypted_number)
            
    return ciphertext

def decrypt_exponential(ciphertext, base, modulus):
    # define plaintext as an empty string
    plaintext = ""

    # d param
    inverse_base = pow(base, -1, modulus - 1)  

    # to calculate m param
    m = int(math.log10(modulus)) - 1

    # split plaintext into blocks of size 2m
    blocks = [ciphertext[i:i+2*m] for i in range(0, len(ciphertext), 2*m)]

    # loop for each block in the ciphertext
    for block in blocks:
        # perform decryption operation
        decrypted_number = pow(int(block), inverse_base, modulus)
        
        if(len(str(decrypted_number)) < 2*m):
            decrypted_number = "0"*(2*m - len(str(decrypted_number))) + str(decrypted_number)
        
        decrypted_number = str(decrypted_number)
        # convert the decrypted number back to characters and append them to the plaintext
        text = ''
        for i in range(0, len(decrypted_number)-1, 2):
            ascii_offset = ord('A')
            text += chr(ascii_offset + int(decrypted_number[i:i+2]))
        plaintext += text
            
    return plaintext
plain_text = "THIS IS AN EXAMPLE OF AN EXPONENTIATION CIPHER"
e = 29
n = 2633
encrypt_expo = encrypt_exponential(plain_text, e, n)
print("ENCRYPT EXPONENTIAL: ", encrypt_expo)

decrypt_expo = decrypt_exponential(encrypt_expo, e, n)
print("DECRYPT EXPONENTIAL: ", decrypt_expo)