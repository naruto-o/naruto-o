import random
n=20
to_be_guessed=int(n*random.random())+1
guess=0
while guess != to_be_guessed:
    guess=int(input("new number:"))
    if guess>0:
        if guess>to_be_guessed:
            print("number to large")
    elif guess<to_be_guessed:
        print("number too small")
    else:
        print("you give up,because yo are pathetic")
        break
else:
    print("congrats,you won")
