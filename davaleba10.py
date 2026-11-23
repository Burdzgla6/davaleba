# Pizza order 

def make_order(customer, size, *toppings, **extras):
   prices = {'small': 10,'medium': 15,'large': 20}
   total = prices[size]
   
   for topping in toppings:
    total += 2

   if extras.get('delivery', False):
    total += 5

   print(f"Customer: {customer}")
   print(f"Size: {size}")  
   print("Toppings:")
   for topping in toppings:
     print(f"- {topping}")  

   print("Extras:")
   for key, value in extras.items():
     print(f"- {key}: {value}")

   print(f"Total: {total}")
   return total

make_order('Nino', 'large', 'cheese', 'olives', delivery=True, drink='Cola')
toppings = ['cheese', 'mushrooms', 'ham']
extras = {'delivery': False, 'note': 'No onions'}
make_order('Luka', 'medium', *toppings, **extras)


# Game Leaderboard

players = [
        {"nick": "ShadowWolf", "level": 42, "wins": 120, "losses": 30},
        {"nick": "PixelQueen", "level": 42, "wins": 95, "losses": 10},
        {"nick": "NoobMaster", "level": 7, "wins": 3, "losses": 40},
        {"nick": "DragonFly", "level": 58, "wins": 200, "losses": 100},
        {"nick": "CatLord", "level": 58, "wins": 150, "losses": 25},
    ]
result = sorted(players, key=lambda x: (x['level'], x['wins']), reverse=True)
print(result)
    
win_rate = sorted(players,key=lambda x: x['wins'] / (x['wins'] + x['losses']), reverse=True)
print(win_rate)

nicknames = sorted(players,key=lambda x: (len(x['nick']), x['nick']))
for player in nicknames:
    print(player['nick'])


# Music playlist

songs = [
    {"title": "Sunrise", "artist": "Luna", "duration": 215, "plays": 5400},
    {"title": "Midnight Drive", "artist": "Neon Pulse", "duration": 187, "plays": 12800},
    {"title": "Ocean Eyes", "artist": "Luna", "duration": 243, "plays": 9100},
    {"title": "Thunder", "artist": "Neon Pulse", "duration": 201, "plays": 7600},
    {"title": "Quiet Rain", "artist": "Mira", "duration": 156, "plays": 3200},
]

def show_playlist(name, *songs):
    print(name)

    counter = 1

    for song in songs:
        print(f"{counter}. {song['title']} - {song['artist']} ({song['duration']} წმ)")
        counter += 1


show_playlist('My Playlist', *songs)



short_songs = sorted(songs, key=lambda song: song["duration"])

show_playlist('Short First', *short_songs)



top_songs = sorted(songs, key=lambda song: song["plays"], reverse=True)

show_playlist('Top 3', *top_songs[:3])


  