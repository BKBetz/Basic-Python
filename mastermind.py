import random

randomInt = random.randint(1000,9999)
masterCode = str(randomInt)

def game() :
    userInput = input('Enter the 4 digit code : ')
    i = 0
    correct = False

    if len(userInput) == 4 :
        for num in userInput :
            
            i += 1
            print(userInput)
            print(masterCode)
            if userInput == masterCode :
                correct = True
                print('Winner')
                print(correct)
                return (correct)
            elif num == masterCode[i -1] :
                print('C')
                correct = False
            elif num in masterCode :
                print('I')
                correct = False
            else :
                print('N')
                correct = False

        else :
            print('Enter a 4 digit code')

game()

# import random
# randomInt = random.randint(1, 100)

# def checker() :
# 	userInput = int(input('Enter a number between 1 and 100 '))
# 	correct = False
# 	while not correct :
# 		print(randomInt)

# 		if userInput == randomInt :
# 			print('You guessed right...congrats -,-')
# 			correct = True
# 			print(userInput)

# 		elif userInput > randomInt :
# 			correct = False
# 			userInput = int(input('Your number is to big..try again '))
# 			print(userInput)
		
# 		elif userInput < randomInt :
# 			correct = False
# 			userInput = int(input('Your number is to small..try again '))
# 			print(userInput)

# checker()
