import random
def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    # Your code here
    balls_list = [0,0,0,0,1,1,1,1]
    draws_list = []
    for i in range(numTrials):
        draws_list.append(random.sample(balls_list, 3))

    for draw in draws_list[:]:
        if all(x==0 for x in draw):
            pass
        elif all(y==1 for y in draw):
            pass
        else:
            draws_list.remove(draw)

    return len(draws_list)/numTrials

print(drawing_without_replacement_sim(100))
        