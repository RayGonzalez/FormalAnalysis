import random

def PlayGame():
    shots=0
    streakCount=0
    streak5 = False
    #we stop when we make 20 shots
    while (shots<=20):
        if random.random()>.5:
            streakCount+=1
            shots+=1
        else : streakCount=0
        if streakCount==5: streak5 = True

    return streak5



wins=0
#play many times
for x in range(0,1000000):
    if PlayGame()==True:
        wins+=1
print wins
print "P= ", wins/1000000.0

