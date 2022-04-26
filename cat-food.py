import random
import requests

your_name = input('What is your name?')

names = ['Emma', 'Anza', 'Jess']
computer_name = random.choice(names)

def player_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()
    player = {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
    }
    return player
player1= player_pokemon();

def computer_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()
    computer = {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
    }
    return computer
player2=computer_pokemon();

def game():
    print(your_name, 'picked {}'.format(player1['name']))
    print("Pokemon id=", player1['id'])
    print("Height=", player1['height'])
    print("Weight=", player1['weight'])
    stat_choice = input('Which stat do you want to use? (id, height, weight) ')

    print("Your opponent", computer_name, "chose {}".format(player2['name']))
    print(stat_choice, "=", player2[stat_choice])

    my_stat = player1[stat_choice]
    opponent_stat = player2[stat_choice]

    if player1[stat_choice] > player2[stat_choice] :
        print('You win')
    elif player1[stat_choice] < player2[stat_choice]:
        print('Better luck next time!')
    else:
        print("It's a draw!")


game()






















