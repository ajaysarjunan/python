import random
generated_number=random.randrange(1,10)
user_number=int(input("guess a number between 1 and 9 including them"))
if user_number==generated_number:
    print("Great!! You guessed it right")
elif user_number>generated_number:
    print("The number is too high")
else:
    print("The number is too low")