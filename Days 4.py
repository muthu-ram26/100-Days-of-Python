user_choice=int(input(" What do you choose? type 0 for rock,1 for paper or for scissors.\n"))
import random
computer_choice=(random.randint(0,2))
print(f"computer chose:{computer_choice}")
if user_choice ==0 and computer_choice==2:
    print("you win!")
elif computer_choice >user_choice:
    print("you lose")
elif computer_choice == user_choice:
    print("it's a draw)
else:
    print("invaild number,you lose")
