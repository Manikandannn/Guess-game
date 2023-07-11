""" Hello guys. Welcome, It is a guessing game and just try its very funny"""
import random
number=random.randint(1,20)
guess=int(input("Can you guess which number i think :"))
while number!=guess:
    if(guess>number):
        print("your guess higher than i think")
    else:
        print("your guess lower than i think")
    guess=int(input("guess again :"))
print("You won ,your guess is correct")
