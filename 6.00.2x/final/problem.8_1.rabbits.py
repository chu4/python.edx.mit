import random
import pylab

random.seed(100)

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30
def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP
    current_rabbit = CURRENTRABBITPOP
    
    for rabbit in range(CURRENTRABBITPOP):
        if random.random()<=(1-CURRENTRABBITPOP/MAXRABBITPOP):
            current_rabbit+=1
    
    CURRENTRABBITPOP = current_rabbit
    # TO DO
    #pass
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    
    current_rabbit = CURRENTRABBITPOP
    current_fox = CURRENTFOXPOP
    for fox in range(CURRENTFOXPOP):
        if current_rabbit>10:
            if random.random()<=(CURRENTRABBITPOP/MAXRABBITPOP):
                current_rabbit-=1
                if random.random()<=1/3:
                    current_fox+=1
            else:
                if random.random()<=9/10:
                    current_fox-=1

    
    CURRENTRABBITPOP = current_rabbit
    CURRENTFOXPOP = current_fox
    # TO DO
    pass
    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    list_rabbit = []
    list_fox = []
    for i in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        list_rabbit.append(CURRENTRABBITPOP)
        list_fox.append(CURRENTFOXPOP)
    return (list_rabbit, list_fox)
    # TO DO
    #pass

tup=runSimulation(200)
pylab.plot(tup[0], label="rabbit")
pylab.plot(tup[1], label="fox")
pylab.legend(loc = 'upper left')
pylab.show()

coeff1 = pylab.polyfit(range(len(tup[0])), tup[0], 2)
pylab.plot(pylab.polyval(coeff1, range(len(tup[0]))))

coeff2 = pylab.polyfit(range(len(tup[1])), tup[1], 2)
pylab.plot(pylab.polyval(coeff2, range(len(tup[1]))))