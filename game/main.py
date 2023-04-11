import random

# voy a crear una dupla 
option = ('piedra', 'papel', 'tijera') # opcion como tanto para el usuario como para la computadora

computer_wins = 0
user_wins = 0
rounds = 1

while True:

    print('*' * 10) # multiplica los asteriscos (*) por 10 (********)
    print('ROUND', rounds)
    print('*' * 10)

    print('computer_wins', computer_wins) # nos lleva el conteo de las partidas
    print('user_wins', user_wins)

    user_option = input('piedra, papel, tijera => ') # opcipon del usuario
    user_option = user_option.lower() # para que quede en minuscula o mayuscula y no ayan errores si se digita en minuscula o mayuscula

    rounds += 1    

    if not user_option in option:
        print('esa opcion no es valida')
        continue

    computer_option = random.choice(option) # randon.choice esto nos sirve para que se escoja de modo aleatoria

    print('User option => ', user_option)
    print('Computer option => ', computer_option)

    if user_option == computer_option:
        print('Empate')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('piedra gana a tijera')
            print('user gano')
            user_wins += 1
        else:
            print('papel gana a piedra')
            print('computer gano')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('papel gana a piedra')
            print('user gano')
            user_wins += 1
        else:
            print('tijera gana a papel')
            print('computer gano!')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('tijera gana a papel')
            print('user gano!')
            user_wins += 1
        else:
            print('piedra gana a tijera ')
            print('computer gano!')
            computer_wins += 1

    if computer_wins == 2:
        print('El ganador es la computadora')
        break            

    if user_wins == 2:
        print('El ganador es el usuario')
        break 
