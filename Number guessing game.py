# import random library to using it in choise random number
import random
while True:
    try:
        # input range from usres
        start=int(input('enter a range of numbers from:'))
        end=int(input('to:'))
        # cheack if the range of numbers positive or not
        if start<0 or end <0 :
           print('error please enter only positive numbers')
           continue
        #  the end should be > start
        if start >end :
            print('error start should be < end ')
            continue
        break
    except ValueError:
        print('error please enter only positive numbers')
guess=True
trails=0
ch=random.choice(range(start,end))

while guess:
    cho=int(input('enter number from your choosing'))
    if cho==ch:
        print('sucsses , end game')
        guess=False
    elif cho>ch:
        print('error , the number > the guess, try agian')
    else:
        print('error , the number < the guess, try agian')
    trails+=1
print(trails)


