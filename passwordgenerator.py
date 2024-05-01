import random
import string

def generate_password(password_length):
    # Define characters 
    allowed_characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password by randomly selecting characters from the defined set
    generated_password = ''.join(random.choice(allowed_characters) for _ in range(password_length))
    
    return generated_password

def main():
    print("Welcome to Password Generator!")
    desired_length = int(input("Enter the desired length of the password: "))

    if desired_length <= 0:
        print("Invalid length! Please enter a positive number.")
        return

    password = generate_password(desired_length)
    print("Your generated password is:", password)

if __name__ == "__main__":
    main()

