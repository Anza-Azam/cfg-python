import random
import requests
from termcolor import colored

your_name = input('What is your name?')
names = ['Emma', 'Anza', 'Jess']
computer_name = random.choice(names)
print("You are playing {}".format(computer_name))
print()
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
    print("{} 'picks {}".format(your_name, player1['name']))
    print("Pokemon id=", player1['id'])
    print("Height=", player1['height'])
    print("Weight=", player1['weight'])
    stat_choice = input('Which stat do you want to use? (id, height, weight) ')
    print()
    print("Your opponent {} picks {}".format(computer_name, player2['name']))
    print(stat_choice, "=", player2[stat_choice])
    print()
    my_stat = player1[stat_choice]
    opponent_stat = player2[stat_choice]

    if player1[stat_choice] > player2[stat_choice]:
        print(colored("You win", 'green'))
        player_score = player_score + 1
    elif player1[stat_choice] < player2[stat_choice]:
        print(colored("You lose! Better luck next time!", 'red'))
        computer_score = computer_score + 1
    else:
        prin(colored("It's a draw!", 'blue'))



no_of_games = 0

while no_of_games < 3:
    game()
    no_of_games = no_of_games + 1
    print()
    print(colored("{}'s score is: {}".format(your_name, player_score), 'blue'))
    print(colored("{}'s score is: {}".format(computer_name, computer_score), 'blue'))
    print()
    print()

if player_score > computer_score:
    print(colored("Congratulations {}!!!, you have won!".format(your_name), 'green'))
elif player_score < computer_score:
    print(colored("Oh no {}!!! You have lost".format(your_name), 'red'))
else:
    print(colored("You have tied", 'blue'))