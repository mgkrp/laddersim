# ranksim
Emulator for Hearthstone ladder player distribution with custom rules.  
Basic rules like winstreaks and rules for ranks and deranks are exactly the same like in Hearthstone.

# Rules  
Ranks go from 0 to the lowest with 0 being the best rank.  
Each player starts at the lowest rank.  
Every player has a "skill" which equals one of the ranks, skill 0 means the highest skill.   
Results are based on skill of both player, player with a higher skill has a better chance to win.  
One iteration forces everyone to play with someone, so everyone will have the exact number of games.

# Files and configuration
.py files:  
player.py - class for a single player.  
ladderrules.py - rules for ladder (ranks and stars for example).  
environment.py - environment which takes current ladder rules and players and emulates games between players.  
main.py - file to launch. Takes an environment and launches it for a certain number of iterations.    

Configuration files:  
no_rankDown.txt - at which ranks you can't derank.
no_starDown.txt - at which ranks you can't lose stars.
winstreak.txt - first line - rank at which bonus stars stop, second line - number of wins requiered for winstreak.
players.txt - number of players of each skill, starts from highest skill to lowest.  

Log files:  
stats.txt - statistics for each player.
ladderRanking - how many players there are at each rank.
history.txt - logs of every match of every iteration.


