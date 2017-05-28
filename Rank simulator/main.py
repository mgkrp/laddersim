import environment as env


file_no_rankDown = open("no_rankDown.txt", "r")
file_no_starDown = open("no_starDown.txt", "r")
file_players = open("players.txt", "r")
file_rankStars = open("rankStars.txt", "r")
file_winstreak = open("winstreak.txt", "r")

no_rankDown = []
no_starDown = []
players = []
rankStars = []
streakLimit = []

for line in file_no_rankDown.readlines():
    no_rankDown.append(int(line))

for line in file_no_starDown.readlines():
    no_starDown.append(int(line))

for line in file_players.readlines():
    players.append(int(line))

for line in file_rankStars.readlines():
    rankStars.append(int(line))

streakLimit = int(file_winstreak.readline())
streakRange = int(file_winstreak.readline())

Environment = env.Environment(players, rankStars, no_rankDown, no_starDown, rankStars[0], len(rankStars) - 1, streakLimit, streakRange)

iterations = 25 # Number of iterations


for iter in range(iterations):
    Environment.startIteration()
    print('Current iteration:', iter+1)

Environment.parseHistory()
Environment.ladderRanking()
Environment.getStats()