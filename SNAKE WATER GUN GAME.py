import random
com_point=0
human_point=0
tie_rounds=0
print("welcome to snake water game\n")
for i in range(1,6): 
    your_choice=str(input("what do you want to choose--\n 1 snake \n  2 water \n 3 gun \n :-------")).lower()
    lst=("snake","water","gun")
    choice=random.choice(lst)
    print(choice) 
    if your_choice=="snake" and choice=="water":
        human_point=human_point+1
        print("you win computer choses water")
    elif your_choice=="snake" and choice=="gun":
        print("you loose computer chooses gun")
        com_point=com_point+1
    elif your_choice=="snake" and choice=="snake":
        print("it is a tie computer also chose a snake")
        tie_rounds=tie_rounds+1
    elif your_choice=="water" and choice=="water":
        print("it is a tie")
        tie_rounds=tie_rounds+1
    elif your_choice=="water" and choice=="gun":
        print("you win")
        human_point=human_point+1
    elif your_choice=="water" and choice=="snake":
        print("you loose")
        com_point=com_point+1
    elif your_choice=="gun" and choice=="water":
        print("you loose")
        com_point=com_point+1
    elif your_choice=="gun" and choice=="gun":
        print("it is a tie")
        tie_rounds=tie_rounds+1
    elif your_choice=="gun" and choice=="snake":
        print("you win")
        human_point=human_point+1
    else:
        print("error")
print(f"game ended your score was {human_point} and the cpu score was {com_point} and the total tie rounds were {tie_rounds}")
if human_point > com_point:
    print(f"you  win by {human_point - com_point} ")
else:
    print(f"you loose by {com_point - human_point}")
print(f"the total no of tie rounds were {tie_rounds}")
print("Re run to play")
   
        
        