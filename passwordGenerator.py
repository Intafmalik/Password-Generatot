from random import randint
import os

# Input from the user
u_pswd = input("Enter a password: ")

# List of possible characters for guessing
pswd = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
        'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z',
        'x', 'c', 'v', 'b', 'n', 'm', '1', '2', '3', '4',
        '5', '6', '7', '8', '9', '0']

password = ""  # Initialize guessed password

while password != u_pswd:
    password = ""  
    for _ in range(len(u_pswd)): 
        guess_char = pswd[randint(0, len(pswd) - 1)]
        
        password += guess_char

    print(password) 
    print("Cracking Password...Please")

    os.system("cls")

print("Your Password is:", password)
