
import random
# This program generates a random password based on user input for length and character types.
# It includes letters, numbers, and symbols.
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']
password_length=int(input("Enter the length of the password: "))
letters_length=int(input("Enter the number of letters: "))
numbers_length=int(input("Enter the number of numbers: "))  
symbols_length=int(input("Enter the number of symbols: "))
password_list=[]
password =""
for i in range(0, len(letters)):
    password_list.append(random.choice(letters))
for i in range(0, len(numbers)):
    password_list.append(random.choice(numbers))
for i in range(0, len(symbols)):
    password_list.append(random.choice(symbols))
for i in range (0,password_length):
    password += random.choice(password_list)
print("Your password is: " + password)