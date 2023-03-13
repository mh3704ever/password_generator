import random
import string

def generate_password(length):
    """Generate a random password of specified length"""
    letters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(letters) for _ in range(length))

if __name__ == '__main__':
    password_length = int(input("Enter password length: "))
    password = generate_password(password_length)
    print("Your password is:", password)
