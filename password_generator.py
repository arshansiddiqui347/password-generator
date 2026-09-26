import random
import string

def generate_password(length):
    # Combine letters, digits, and punctuation
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly select characters
    password_list = [random.choice(all_characters) for _ in range(length)]
    
    # Join them into a single string
    password = "".join(password_list)
    
    return password

if __name__ == "__main__":
    print("--- Python Password Generator ---")
    try:
        user_length = int(input("Enter desired password length (e.g., 12): "))
        if user_length <= 0:
            print("Please enter a number greater than 0.")
        else:
            new_password = generate_password(user_length)
            print(f"\nYour generated password is: {new_password}")
    except ValueError:
        print("Error: Please enter a valid whole number.")
