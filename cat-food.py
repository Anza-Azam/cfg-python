import random
import requests
from termcolor import colored

your_name = input('What is your name?')
names = ['Emma', 'Anza', 'Jess']
computer_name = random.choice(names)
player_score = 0
computer_score = 0

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



def game():
    global player_score, computer_score
    player1 = player_pokemon()
    player2 = computer_pokemon()
    print(your_name, 'picked {}'.format(player1['name']))
    print("Pokemon id=", player1['id'])
    print("Height=", player1['height'])
    print("Weight=", player1['weight'])
    stat_choice = input('Which stat do you want to use? (id, height, weight) ')

    print("Your opponent", computer_name, "chose {}".format(player2['name']))
    print(stat_choice, "=", player2[stat_choice])

    my_stat = player1[stat_choice]
    opponent_stat = player2[stat_choice]

    if player1[stat_choice] > player2[stat_choice]:
        print('You win')
        player_score = player_score + 1
    elif player1[stat_choice] < player2[stat_choice]:
        print('Better luck next time!')
        computer_score = computer_score + 1
    else:
        print("It's a draw!")



no_of_games = 0

while no_of_games < 3:
    game()

    no_of_games = no_of_games + 1
    print(colored("The outcome!", attrs=['bold']))
    print("{}'s score is: {}".format(your_name, player_score))
    print("{}'s score is: {}".format(computer_name, computer_score))
    if player_score < computer_score:
        print("Oh no, {}!! You have lost!".format(computer_name, your_name))
    elif player_score > computer_score:
        print("Congratulations, {}!! You have won!".format(your_name))
    else:
        print("You have tied!")