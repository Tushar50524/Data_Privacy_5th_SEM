import random
import string # ForEnhancement

# Function to read words from a dictionary file
def read_dictionary(filename):
    try:
        with open(filename, 'r') as file:
            words = [line.strip() for line in file if line.strip()]
        return words
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []

# Function to generate a password using random words with added numbers and capital letters
def generate_secure_password(words, num_words=4):
    if len(words) < num_words:
        raise ValueError("Not enough words in the dictionary to generate the password.")
    
    # Randomly select words from the dictionary
    selected_words = random.sample(words, num_words)
    
    # Capitalize the first letter of each word
    selected_words = [word.capitalize() for word in selected_words]
    
    # Combine the words into a single string
    password = ''.join(selected_words)
    
    # Optionally, add a random number and special character
    # password += str(random.randint(0, 99))  # Add a random number (FOR ENHANCEMENT)
    # password += random.choice(string.punctuation)  # Add a random special character  (FOR ENHANCEMENT)
    
    return password

# Main function
if __name__ == "__main__":
    # Input dictionary file from the user
    dictionary_file = input("Enter the dictionary file path: ")
    
    # Read the words from the file
    words_list = read_dictionary(dictionary_file)
    
    if words_list:
        # Get the number of words to use for the password
        num_words = int(input("Enter the number of words to use in the password: "))
        
        # Generate and display the secure password
        secure_password = generate_secure_password(words_list, num_words)
        print(f"Generated Secure Password: {secure_password}")
