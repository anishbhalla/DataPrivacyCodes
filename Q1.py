# Ceaser Cipher (substitution cipher) Encryption and Decryption.

def encrypt_ceaser_cipher(text,shift) :
    result = ""
    for char in text :
        if char.isalpha() :
            if char.isupper() :
                new_char = chr((ord(char)-ord('A')+shift)%26 + ord('A')) # Normalizing for capital letters.
            else :
                new_char = chr((ord(char)-ord('a')+shift)%26 + ord('a')) # Normalizing for small letters.
            result +=new_char
        else : 
            result +=char
    return result

def decrypt_ceaser_cipher(text,shift) :
    return encrypt_ceaser_cipher(text,-shift) # Decrypt by shifting in the opposite direction.



# Example usage
msg = input("Enter the string to be encrypted : ")
shft = int(input("Enter the shift value : "))
encrypted = encrypt_ceaser_cipher(msg,shft)
decrypted = decrypt_ceaser_cipher(encrypted,shft)

print('Encrypted :',encrypted)
print('Decrypted ',decrypted)
