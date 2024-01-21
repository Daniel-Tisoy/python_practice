import hashlib 
def hash_password(password: str) -> str:
    # Convert the password to bytes
    password_bytes = password.encode('utf-8')

    # Hash the password using SHA-256
    hashed_password = hashlib.sha256(password_bytes).hexdigest()

    return hashed_password
    

if __name__ == "__main__":
    print(hash_password("adminpass"))
    print(hash_password("danpass"))


