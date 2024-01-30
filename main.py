import random
while True:
    try:
        nDice = int(input("How many dice do you want to roll? "))
    except ValueError:  # ValueError is the exception when the user doesn't input an int
        print("Invalid value, try again")
    number = [random.randint(1, 6) for _ in range(nDice)]  # with for _ in range we can avoid for loop
    print(number)
    choice = input("Do you want to roll dice? y/n ")
    if choice.lower() in ['y', 'yes']:  # continue only if the input is y or yes, in all the other cases exit
        continue
    else:
        print("Invalid choice or opted to exit")
        break
print(number)
