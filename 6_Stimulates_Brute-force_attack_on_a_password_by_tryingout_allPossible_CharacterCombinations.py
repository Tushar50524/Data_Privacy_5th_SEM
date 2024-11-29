import itertools
import time
import string

# Function to perform the brute-force attack
def brute_force_attack(password_length, charset, target_password):
    # Start a timer to measure how long the attack takes
    start_time = time.time()
    
    # Generate combinations of characters of the specified length
    for attempt in itertools.product(charset, repeat=password_length):
        guess = ''.join(attempt)  # Convert tuple to string
        
        # Check if the generated guess matches the target password
        if guess == target_password:
            end_time = time.time()
            print(f"Password found: {guess}")
            print(f"Brute-force attack took {end_time - start_time:.2f} seconds.")
            return guess  # Return the password when found
    
    # If the loop finishes, no match is found
    print("Password not found.")
    return None

# Main function to get user input
def main():
    # Ask the user for the target password
    target_password = input("Enter the target password to brute-force: ")

    # Ensure the target password is not empty
    if not target_password:
        print("Password cannot be empty!")
        return
    
    # Ask the user for the password length to brute-force
    password_length = int(input(f"Enter the length of the password to crack (must be {len(target_password)}): "))
    
    # Ensure that the specified length is valid
    if password_length != len(target_password):
        print(f"Invalid length! Please provide the exact length of the target password ({len(target_password)}).")
        return
    
    # Define the character set to be used in the brute-force attack
    # This includes lowercase, uppercase, digits, and some common special characters
    charset = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    
    # Run the brute-force attack with the user-provided password length
    brute_force_attack(password_length, charset, target_password)

# Run the program
if __name__ == "__main__":
    main()
