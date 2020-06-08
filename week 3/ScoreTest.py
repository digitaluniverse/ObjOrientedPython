import Score

list1 = [99,25,36,52,1,13,6,17]
list2 = [123,54,6,19,44,2,39,1]

score1 = Score.Score(list1)
score2 = Score.Score(list2)

print (" Score 1:\n Mean: {} \n Standard Deviation: {}\n Highest Score: {}\n Lowest Score: {}".format(score1.mean(),score1.standardDeviation(), score1.highestScore(),score1.lowestScore()))

print ("\n Score 2:\n Mean: {} \n Standard Deviation: {}\n Highest Score: {}\n Lowest Score: {}".format(score2.mean(),score2.standardDeviation(), score2.highestScore(),score2.lowestScore()))
