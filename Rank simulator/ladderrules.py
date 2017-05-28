# Class for initializing ladder rules
class LadderRules():
    # Initialization
    def __init__(self, rankStars, no_rankDown, no_starDown, starsMax, rankMax, streakLimit, streakRange):
        self.rankNumber = len(rankStars)        # Number of ranks, ranges from 0 to rankNumber - 1
        self.rankStars = rankStars              # Array of star requirment for ranks. Length - rankNumber. rankStars[i] - number of stars you can maximum have at rank[i].
        self.no_rankDown = no_rankDown          # Array of ranks, at which you can't derank.
        self.no_starDown = no_starDown          # Array of ranks, at which you can't lose stars. You can't derank, if you can't lose stars at your rank.
        self.starsMax = starsMax                # Maximum amount of stars one player can get. Usually it's the amount of stars you need to get to rank 0.
        self.rankMax = rankMax                  # Maximum rank you can get (the lower the rank - the better). Equals rankNumber - 1.
        self.streakLimit = streakLimit          # Rank, at which you  can't get bonus stars for winstreaks.
        self.streakRange = streakRange          # Number of wins in a row required to earn bonus star.

    # Number of ranks getter
    def getrankNumber(self):
        return self.rankNumber

    # Number of stars getter
    def getrankStars(self):
        return self.rankStars

    # "Can't derank" ranks getter
    def getno_rankDown(self):
        return self.no_rankDown

    # "Can't lose stars" ranks getter
    def getno_starDown(self):
        return self.no_starDown

    # Maximum stars getter
    def getstarsMax(self):
        return self.starsMax

    # Maximum rank getter
    def getrankMax(self):
        return self.rankMax

    # Winstreak limit getter
    def getstreakLimit(self):
        return self.streakLimit

    # Wins in a row for winstreak getter
    def getstreakRange(self):
        return self.streakRange