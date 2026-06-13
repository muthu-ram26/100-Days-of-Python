print("WELCOME TO THE PIZZA DELIVERIES!")
size=input("What size pizza do want? S,M,or,L")
pepperoni=input("Do you want pepperoni on your pizza? yes or no")
extra_cheese=input("Do you want extra cheese? yes or no")
bill=0
if size =="s":
    bill += 15
elif size =="l":
    bill+=25
elif size =="m":
    bill +=20
else:
    print("your type the wrong output")
if pepperoni =="yes":
    if size =="s":
        bill+=2
    else:
        bill+=3
if extra_cheese=="yes":
    bill+=1
print(f"your final bill: {bill}.")    



    
