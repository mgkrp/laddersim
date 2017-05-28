# Class for emulating ladder

import player as pl
import ladderrules as ld
import math
import random

class Environment():
    # Initialization
    def __init__(self, playerSkill, rankStars, no_rankDown, no_starDown, starsMax, rankMax, streakLimit, streakRange):
        self.ladder = ld.LadderRules(rankStars, no_rankDown, no_starDown, starsMax, rankMax, streakLimit, streakRange) # Initializing ladder rules.
        self.players = [] # Array of players.
        self.playersNumber = sum(playerSkill) # Number of players.
        id = 0
        for rank, quantity in enumerate(playerSkill): # Iterating through ranks.
            for i in range(quantity):
                self.players.append(pl.Player(id, rank, self.ladder.rankMax)) # Creating a player for current rank.
                id += 1
        self.history = [] # Overall history of emulation.
        self.iterationHistory = [] # History of current iteration.

    # Sorting players based on their current ranks
    def sortByRanks(self):
        random.shuffle(self.players) # To prevent people playing with the same skill level.
        self.players.sort(key=lambda x: x.getcurrentRank(), reverse = True) # Ranks are sorted from rankMax to 0.

    # Calculating chance for playerOne to win agains playerTwo
    def calculateVictoryChance(self, playerOne, playerTwo):
        rank_playerOne = playerOne.getskillRank()
        rank_playerTwo = playerTwo.getskillRank()
        sigmoidCoeff = 2 # Coefficient for sigmoid function. The less it is, the more chance to win more skilled player will have.
        winProbability = 1 / (1 + (math.pow(math.e, (rank_playerOne - rank_playerTwo) / sigmoidCoeff))) # Sigmoid for calculating chance of victory.
        return winProbability

    # Deciding a winner based on win probability
    def decideWinner(self, playerOne, playerTwo):
        winProbability = self.calculateVictoryChance(playerOne, playerTwo)
        if winProbability >= random.random():
            playerWinner = playerOne
            playerLoser = playerTwo
        else:
            winProbability = 1 - winProbability # Since winProbability is a chance for playerOne to win a playerTwo, we need to change in if playerTwo won.
            playerWinner = playerTwo
            playerLoser = playerOne
        playerWinner.changeLuck(2 - winProbability) # Multiplying current luck attribute by 2 - winProbability. Ex: if the winProbability was 80%, luck would be luck*1.2.
        playerLoser.changeLuck(winProbability) # Multiplying current luck attribute by winProbability. Ex: if the winProbability was 80%, luck would be luck*0.8.
        self.handleResult(playerWinner, playerLoser)

    # Handling a match result
    def handleResult(self, playerWinner, playerLoser):
        playerLoser.lose() # Changing wins for loser
        playerWinner.win() # Changing wins for winner

        winnerStars = playerWinner.getstars()
        winnerRank = playerWinner.getcurrentRank()
        loserStars = playerLoser.getstars()
        loserRank = playerLoser.getcurrentRank()
        winnerWinsInARow = playerWinner.getwins_InARow()
        no_starDown = self.ladder.getno_starDown()
        no_rankDown = self.ladder.getno_rankDown()
        rankStars = self.ladder.getrankStars()
        rankMax = self.ladder.getrankMax()
        starsMax = self.ladder.getstarsMax()
        streakLimit = self.ladder.getstreakLimit()
        streakRange = self.ladder.getstreakRange()
        bonusStar = 0

        self.iterationHistory.append([playerWinner, playerLoser, winnerRank, loserRank, winnerStars, loserStars]) # Adding match to the iteration history

        if loserRank not in no_starDown and loserStars != 0 and not (loserRank in no_rankDown and rankStars[loserRank] == loserStars): # Checking, if loser can lose stars at this rank, loser has stars to lose and he isn't losing last star when he can't derank.
            playerLoser.starDown()
            if loserRank != rankMax: # Checking if rank is not maximum, to prevent overflow.
                if loserStars < rankStars[loserRank + 1] and loserRank not in no_rankDown: # Checking, if loser lost enough stars to derank and he's not in rank, where he can't derank.
                    playerLoser.rankDown()

        if winnerStars < starsMax: # Checking, if winner is not  at the maximum amount of stars.
            playerWinner.starUp()
            if winnerStars + 1 < starsMax and winnerWinsInARow >= streakRange and winnerRank > streakLimit: # Checking, if bonus star for winstreak is available.
                playerWinner.starUp()
                bonusStar = 1
            if winnerRank != 0 and winnerStars + 1 + bonusStar >= rankStars[winnerRank]: # Checking if winner has enough stars to rank up.
                playerWinner.rankUp()

    # Generate a series of matches. Every player has a match with one another player during one iteration. Could work strangely if number of players is odd.
    def matchPlayers(self):
        for i in range (math.floor(self.playersNumber/2)):
            if i*2+1 != self.playersNumber:
                self.decideWinner(self.players[i*2], self.players[i*2+1]) # Matches 2 neighbor players in ranks, starting from bottom. If number of players is odd, the best one will not have a pair.

    #  history.txt with all match results
    def parseHistory(self):
        print ("Generating history.txt")
        file = open("history.txt", "w")
        for iterI, iteration in enumerate(self.history):
            file.write('================================= Iteration: {0} =================================\n'.format(iterI+1))
            for iterM, match in enumerate(iteration):
                playerWinner = match[0]
                playerLoser = match[1]
                winnerRank = match[2]
                loserRank = match[3]
                winnerStars = match[4]
                loserStars = match[5]
                winProbability = self.calculateVictoryChance(playerWinner, playerLoser)
                file.write("Match #{0}: ID {1} (rank: {2}, stars: {8}, skill: {3}) won against ID {4} (rank: {5}, stars: {9}, skill: {6}) with a chance of {7}\n".format(iterM+1, playerWinner.getid(), winnerRank, playerWinner.getskillRank(), playerLoser.getid(), loserRank, playerLoser.getskillRank(), winProbability, winnerStars, loserStars))

    # Start a single iteration
    def startIteration(self):
        self.sortByRanks()
        self.matchPlayers()
        self.history.append(self.iterationHistory)
        self.iterationHistory = []

    # Generate ladderRanking.txt with info of all players.
    def ladderRanking(self):
        self.sortByRanks()
        print ("Generating ladderRanking.txt")
        file = open("ladderRanking.txt", "w")
        for player in self.players:
            file.write("Player ID: {0}, rank: {1}, skill: {2}, winrate: {3}, luck: {4}\n".format(player.getid(), player.getcurrentRank(), player.getskillRank(), player.getwinrate(), player.getluck()))

    # Generating stats on ladder
    def getStats(self):
        ranks = []
        for i in range(self.ladder.getrankNumber()):
            ranks.append(0)
        print ("Generating stats.txt")
        file = open("stats.txt", "w")
        for player in self.players:
            ranks[player.getcurrentRank()] += 1
        for iter, rank in enumerate(ranks):
            file.write("Rank: {0}, players: {1}\n".format(iter, rank))