# Function to encrypt the plaintext using Rail Fence Cipher
def encryptRailFence(text, key):
    # Create a 2D list to store the characters in the zigzag pattern
    rail = [['\n' for i in range(len(text))] for j in range(key)]
    
    # Determine the direction and place the characters in the zigzag pattern
    dir_down = False
    row, col = 0, 0
    
    for i in range(len(text)):
        # Check if the direction needs to be changed (top or bottom rail reached)
        if row == 0 or row == key - 1:
            dir_down = not dir_down
        
        # Place the character in the matrix
        rail[row][col] = text[i]
        col += 1
        
        # Move in the appropriate direction
        row += 1 if dir_down else -1
    
    # Read the characters row-wise to get the ciphertext
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    
    return "".join(result)

# Function to decrypt the ciphertext using Rail Fence Cipher
def decryptRailFence(cipher, key):
    # Create a 2D list to mark the positions in the zigzag pattern
    rail = [['\n' for i in range(len(cipher))] for j in range(key)]
    
    dir_down = None
    row, col = 0, 0
    
    # Mark the positions in the rail matrix
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        
        # Place a marker to indicate where characters would have been placed
        rail[row][col] = '*'
        col += 1
        
        # Move in the appropriate direction
        row += 1 if dir_down else -1
    
    # Now fill the markers with the ciphertext characters
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1
    
    # Read the characters in a zigzag pattern to retrieve the plaintext
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        
        # Read characters as per the zigzag movement
        if rail[row][col] != '\n':
            result.append(rail[row][col])
            col += 1
        
        row += 1 if dir_down else -1
    
    return "".join(result)

# Main function to test the Rail Fence Cipher
if __name__ == "__main__":
    text = input("Enter the text to encrypt: ")
    key = int(input("Enter the key (number of rails): "))

    # Encrypt the text
    cipher = encryptRailFence(text, key)
    print("Encrypted text:", cipher)

    # Decrypt the text
    decrypted_text = decryptRailFence(cipher, key)
    print("Decrypted text:", decrypted_text)
