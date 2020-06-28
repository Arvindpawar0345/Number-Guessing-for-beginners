import random
ab=0
while ab==0:
    number = random.randint(1,100)
    a=int(input('Guess the Number in between 1 to 100:\n'))
    if a==number:
        print('You Won')
        break

    else:
        print('you loss')
ab +=1
