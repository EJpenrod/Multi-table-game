import random


def times_table_guess():
    score = 0
    valid = False
    while True:
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        solution = x * y
        print("what is {} * {}?\n".format(x, y))
        while not valid:  # loop until the user enters a valid int
            try:
                guess = int(input("enter the answer: "))
                valid = True  # if this point is reached, x is a valid int
            except ValueError:
                print('Please only type in a number')
        if guess == solution:
            print("""
.___________________.
|      correct      |
|___________________|\n*********************""")
            score += 1
        else:
            print("""
.___________________.
|     incorrect     |
|___________________|
 the answer is {}\n*********************""".format(solution))
        print("your score is [{}]\n*********************\n".format(score))
        valid = False
        if score == 20:
            print("""
____ ____ _  _ ____ ____ ____ ___ _  _ _    ____ ___ _ ____ _  _ ____ |
|    |  | |\ | | __ |__/ |__|  |  |  | |    |__|  |  | |  | |\ | [__  |
|___ |__| | \| |__] |  \ |  |  |  |__| |___ |  |  |  | |__| | \| ___] .
_   _ ____ _  _   ____ ____    ____ _    _       ___  ____ _  _ ____
 \_/  |  | |  | ' |__/ |___    |__| |    |       |  \ |  | |\ | |___
  |   |__| |__|   |  \ |___    |  | |___ |___    |__/ |__| | \| |___
""")
            break


times_table_guess()
