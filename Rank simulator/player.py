# Class for initializing a player
class Player():
    # Initialization
    def __init__(self, id, rank, maxrank):
        self.id = id                    # ID of player.
        self.skillRank = rank           # Skill of a player, based on ranks in the ladder, ranges from 0 to maximum ladder rank.
        self.currentRank = maxrank      # Current rank of a player, ranges from 0 to maximum ladder rank. Everyone starts at the max rank by default.
        self.stars = 0                  # Number of stars player has.
        self.games = 0                  # Number of games played.
        self.wins = 0                   # Number of wins.
        self.wins_InARow = 0            # Number of wins in a row. Used for bonus stars for winstreaks.
        self.luck = 1                   # Attribute that kinda shows, how lucky the player was. It's kinda relative to other's luck, compare it, don't take it as absolute value.

    # Player winning
    def win(self):
        self.games += 1
        self.wins += 1
        self.wins_InARow += 1

    # Player losing
    def lose(self):
        self.games += 1
        self.wins_InARow = 0

    # Luck setter
    def changeLuck(self, coef):
        self.luck *= coef

    # Rank setter
    def rankUp(self):
        self.currentRank -= 1

    # Rank setter
    def rankDown(self):
        self.currentRank += 1

    # Star setter
    def starUp(self):
        self.stars += 1

    # Star setter
    def starDown(self):
        self.stars -= 1

    # ID getter
    def getid(self):
        return self.id

    # Skill rank getter
    def getskillRank(self):
        return self.skillRank

    # Current rank getter
    def getcurrentRank(self):
        return self.currentRank

    # Stars getter
    def getstars(self):
        return self.stars

    # Number of games getter
    def getgames(self):
        return self.games

    # Number of wins getter
    def getwins(self):
        return self.wins

    # Winrate getter
    def getwinrate(self):
        return float(self.wins/self.games)

    # Wins in a row getter
    def getwins_InARow(self):
        return(self.wins_InARow)

    # Luck getter
    def getluck(self):
        return(self.luck)