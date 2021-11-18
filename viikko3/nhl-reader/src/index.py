import requests
from player import Player

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

#    print("JSON-muotoinen vastaus:")
#    print(response)

    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'],
            player_dict['goals'],
            player_dict['assists']
        )

        if player_dict['nationality'] == 'FIN':
            players.append(player)
    
    players = sorted(players, key=lambda p: p.points, reverse=True)
    print("Oliot:")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()

