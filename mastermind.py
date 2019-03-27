import random

master_code = ''


def start():
    createNum()
    userInput()


def createNum():
    global master_code
    random_int = random.randint(0000, 9999)
    code = '{:04}'.format(random_int)
    master_code = str(code)


def userInput():

    user_input = input('Enter a 4 digit code: ')

    if len(user_input) == 4:
        try:
            answer = int(user_input)
            answer = '{:04}'.format(answer)
            check(answer)

        except ValueError:
            print('enter a number')
            userInput()

    else:
        print('Code should be 4 digits')
        userInput()


def check(user_input):

    global master_code
    user_answer = str(user_input)
    i = 0
    if user_answer == master_code:
        print("You've won...the code was " + master_code)

    else:
        print('Your code was :' + user_answer)
        for num in user_answer:

            i += 1
            if user_answer[i - 1] == master_code[i - 1]:
                print('C')
            elif num in master_code:
                print('I')
            elif num not in master_code:
                print('N')

        print("""
        C = right number in the right place
        I = right number but not in the right place
        N = not in the code
        """)

    if user_answer != master_code:
        userInput()


start()
