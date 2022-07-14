#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
pw = ""



#Easy Password Generator
for i in range(nr_letters):
    pw += letters[random.randint(1,52)]
for i in range(nr_symbols):
    pw += symbols[random.randint(1,len(symbols)-1)]
for i in range(nr_numbers):
    pw += numbers[random.randint(1,len(numbers)-1)]
print(pw)

'''
Output:
Welcome to the PyPassword Generator!
How many letters would you like in your password?
3
How many symbols would you like?
3
How many numbers would you like?
3
udk)$)575
'''

