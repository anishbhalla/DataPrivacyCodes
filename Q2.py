# Rail Fence Cipher (Transpositional Cipher) Encryption and Decryption.

def rail_fence_encrypt(text, num_rails):
    rails = [''] * num_rails
    rail = 0
    direction = 1

    for char in text:
        rails[rail] += char
        rail += direction

        if rail == 0 or rail == num_rails - 1:
            direction *= -1

    return ''.join(rails)

def rail_fence_decrypt(cipher_text, num_rails):
    matrix = [['\n' for _ in range(len(cipher_text))] for _ in range(num_rails)]
    rail = 0
    direction = 1

    for i in range(len(cipher_text)):
        matrix[rail][i] = '*'
        rail += direction
        if rail == 0 or rail == num_rails - 1:
            direction *= -1

    # Fill the matrix with characters from the cipher text
    index = 0
    for r in range(num_rails):
        for c in range(len(cipher_text)):
            if matrix[r][c] == '*' and index < len(cipher_text):
                matrix[r][c] = cipher_text[index]
                index += 1

    # Read the matrix in zigzag order to get the original text
    result = []
    rail = 0
    direction = 1
    for i in range(len(cipher_text)):
        result.append(matrix[rail][i])
        rail += direction
        if rail == 0 or rail == num_rails - 1:
            direction *= -1

    return ''.join(result)

text_to_encrypt = "HELLO, WORLD!"
num_rails = 3

encrypted_text = rail_fence_encrypt(text_to_encrypt, num_rails)
print("Encrypted:", encrypted_text)

decrypted_text = rail_fence_decrypt(encrypted_text, num_rails)
print("Decrypted:", decrypted_text)
