# SHA-256 Hashing of a Password

import hashlib

def hash_password(password):
    sha256_hash = hashlib.sha256(password.encode())
    return sha256_hash.hexdigest()

# Example usage
password = "securepassword123"
hashed_password = hash_password(password)
print("SHA-256 Hashed Password:", hashed_password)
