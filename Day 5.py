import random
letter =['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
'o','p','q','r','s','t','u','v','w','x','z']
number=["1","2","3","4","5","6","7","8","9,"]
symbols=['!','#','$','%','(',')','*','+']
print("Welcom to the pypassword Generator!")
num_letters=int(input("How many letter would you like in your in your password?\n"))
num_symbols
=int(input(F"How many symbols would you like \n"))
num_number=int(input(f"How many number would you like\n"))
password=" "
for char in range (0, num_letters):
    password+=random.choice(letter)
    
for char in range (0,num_symbols ):
    password+=random.choice(symbols)
    
for char in range (0,num_number ):
    password+=random.choice(number)
print(password)
