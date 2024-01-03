# import modules
import random

# main function
def guess_number (max_limit):
    # explaining the game
    print('=============================')
    print('    ¡Bienvenida al juego!    ')
    print('=============================')
    print('Debes adivinar el número dado por el computador')
    
    # number to find
    random_number = random.randint(1, max_limit)
    # define user number
    user_number = 0

    while user_number != random_number:
        # user number
        user_number = int(input(f'Adivina un número entre 1 y {max_limit}: '))

        # check if there is 
        if (user_number < random_number) :
            print('Intenta otra vez. El número es muy pequeño')
        elif(user_number > random_number) :{
            print('Intenta otra vez. El número es muy grande')
        }

    print(f'¡Los números son iguales! user: {user_number} | random number: {random_number}')


guess_number(6)