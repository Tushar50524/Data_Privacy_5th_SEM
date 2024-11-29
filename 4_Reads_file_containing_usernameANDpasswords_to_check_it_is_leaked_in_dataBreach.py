# IF A PASSWORD HAS BEEN LEAKED.
import hashlib
import requests

# Function to get the SHA-1 hash of a password
def get_sha1_hash(password):
    sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    return sha1

# Function to check if a password has been leaked using HIBP API
def check_password_pwned(password):
    sha1_hash = get_sha1_hash(password)
    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]

    # API URL for k-Anonymity model
    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    # Query the HIBP API
    response = requests.get(url)

    if response.status_code != 200:
        raise RuntimeError(f"Error fetching data: {response.status_code}")

    # Check if the suffix of the hash is in the returned list
    hashes = (line.split(':') for line in response.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return int(count)  # Password found with the number of times pwned

    return 0  # Password not found

# Function to process the file and check each password
def check_passwords_from_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                username, password = line.strip().split(',')
                pwned_count = check_password_pwned(password)
                if pwned_count > 0:
                    print(f"WARNING: The password for '{username}' has been found {pwned_count} times in data breaches.")
                else:
                    print(f"The password for '{username}' is safe (not found in any breaches).")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Main function
if __name__ == "__main__":
    filename = input("Enter the file name containing usernames and passwords: ")
    check_passwords_from_file(filename)
