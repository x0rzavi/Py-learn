n = int(input('Enter number of players: '))
cricket = {}

for i in range(n):
    name = input('Enter player name: ').capitalize()
    runs = int(input('Enter runs scored: '))
    cricket[name] = runs
    print()

while(True):
    name = input('Enter player name to retrive runs: ').capitalize()
    if name in cricket:
        print(cricket[name])
    else:
        print(-1)
    print()
