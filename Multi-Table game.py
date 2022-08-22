import random


def times_table_guess():
    score = 0
    while True:
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        solution = x * y
        print("what is {} * {}?\n".format(x, y))
        guess = int(input("What is the solution?: "))
        if guess == solution:
            print("""
____________________
    correct
____________________""")
            score += 1
        else:
            print("""
____________________
    incorrect
____________________, the answer is {}\n""".format(solution))
        print("your score is {}\n".format(score))
        if score == 20:
            print("""
____ ____ _  _ ____ ____ ____ ___ _  _ _    ____ ___ _ ____ _  _ ____ |
|    |  | |\ | | __ |__/ |__|  |  |  | |    |__|  |  | |  | |\ | [__  |
|___ |__| | \| |__] |  \ |  |  |  |__| |___ |  |  |  | |__| | \| ___] .
_   _ ____ _  _ . ____ ____    ____ _    _       ___  ____ _  _ ____
 \_/  |  | |  | ' |__/ |___    |__| |    |       |  \ |  | |\ | |___
  |   |__| |__|   |  \ |___    |  | |___ |___    |__/ |__| | \| |___
""")
            break


times_table_guess()
