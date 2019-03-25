import random

randomInt = random.randint(1000, 9999)
masterCode = str(randomInt)
check = False


def game():
    user_input = input('Enter the 4 digit code : ')
    i = 0
    global check

    if len(user_input) == 4:
        if not check:
            print('Your code was :' + user_input)
            for num in user_input:

                i += 1
                if user_input == masterCode:
                    print('Winner')
                    check = True
                    return check
                elif user_input[i - 1] == masterCode[i - 1]:
                    print('C')
                elif num in masterCode:
                    print('I')
                else:
                    print('N')

            print("""
C = right number in the right place
I = right number but not in the right place
N = not in the code
            """)
    else:
        print('Enter a 4 digit code')


while not check:
    game()

