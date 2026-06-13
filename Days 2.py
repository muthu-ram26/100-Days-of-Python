print("Welcome to the tip calculator")
bill=int(input("what is your bill\n"))
tip = int(input("how much want give tip 10,12,15,20?\n"))
people=int(input("how many people to split the bill?\n"))
calculate=(tip+bill)/people
print(f"Each person should pay :",calculate)
