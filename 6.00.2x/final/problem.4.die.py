import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    # TODO
    pylab.hist (values, numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title==None:
        pass
    else:
        pylab.title(title)
    pylab.show()
    
                    
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    # TODO
    long_run_sum = 0
    long_die_list = []
    for trial in range(numTrials):
        
        roll_list = []
        
        for roll in range(numRolls):
            roll_list.append(die.roll())
        
        longest_run = 1
        longest_rll = roll_list[0]
        run = 1
        rll = roll_list[0]
        
        for roll in range(len(roll_list)):
            if roll==len(roll_list)-1:
                break
            else:                
                if roll_list[roll+1]==roll_list[roll]:
                    run+=1
                    if run>longest_run:
                        longest_run=run
                        longest_rll=rll
                else:
                    run=1
                    rll=roll_list[roll+1]
        
        long_run_sum+=longest_run
        long_die_list.append(longest_rll)
     
    makeHistogram(long_die_list, 10, "longest roll", "number of occurances")        
    return long_run_sum/numTrials
# One test case

print (getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000))
#print (getAverage(Die([1]), 10, 1000))
#print (getAverage(Die([1,1]), 10, 1000))