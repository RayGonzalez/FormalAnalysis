import random

def PlayGame():
   #Players start with 0 points
    p1=0
    p2=0
    #I serve first
    s=True
    #Play until someone wins
    while(p1<21 and p2<21):
        if(s):
            #60% of winning
            if(random.random()>.4):
                p1+=1
            else:
                s=False
        else:
            if(random.random()<=.5):
                p2+=1
            else:
                s=True
    if (p1==21):
        return True
    if (p2==21):
        return False


#
wins=0
#play many times
for x in range(0,10000):
    if PlayGame()==True:
        wins+=1
print "P= ", wins/10000.0
