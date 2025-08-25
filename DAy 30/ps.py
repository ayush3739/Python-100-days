#Password Generator Project
import random

def easy():
    pass1=""
    pass2="" 
    pass3=""
    for i in range(0,nr_letters):
        pass1=pass1+random.choice(letters)
    for i in range(0,nr_symbols):
        pass2=pass2+random.choice(symbols)
    for i in range(0,nr_numbers):
        pass3=pass3+random.choice(numbers)

    print(f"your EASY password should be this: {pass1+pass2+pass3}")

def strong ():
    pass1=[]
    for i in range(0,nr_letters):
        pass1.append(random.choice(letters))
    for i in range(0,nr_symbols):
        pass1.append(random.choice(symbols))
    for i in range(0,nr_numbers):
        pass1.append(random.choice(numbers))
        
    random.shuffle(pass1)
    finalpass = ''.join(pass1)
    print(f"your Strong password should be this: {finalpass}")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
while True:
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    choice=input("Choose password type - Easy or Strong (E/S):").lower()
    if choice=='e':
        easy()
    elif choice=='s':
        strong()
    else:
        print("❌ Invalid choice. Please choose 'E' for Easy or 'S' for Strong.")

    con=input("Continue or Exit (C/E):").lower()
    if con=='c':
        continue
    else:
        print("👋 Exiting Password Generator. Stay safe!")
        break