import hashlib

# Function to hash the input password using SHA-256
def hash_password(password):
    # Convert the password to a bytes-like object and hash it using SHA-256
    sha_signature = hashlib.sha256(password.encode()).hexdigest()
    return sha_signature

# Main function to get user input and display the hashed password
if __name__ == "__main__":
    # Input the password from the user
    password = input("Enter the password to hash: ")
    
    # Hash the password and print the SHA-256 representation
    hashed_password = hash_password(password)
    print(f"SHA-256 Hashed Password: {hashed_password}")
