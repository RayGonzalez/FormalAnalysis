
import numpy as np
from scipy import stats




def create_pop(n):
    # A
    distrib = 1000 * np.random.random_sample(n)

    return distrib

#testing without bonferroni
def testhypothesis(pop1,pop2,SE):
    sample_size = 30
    #specify significance level
    alpha = .05
    #create 2 random samples
    sample1 = np.random.choice(pop1, (sample_size))
    sample2 = np.random.choice(pop2, (sample_size))

    T = (  (np.mean(sample1) - np.mean(sample2))-(np.mean(pop1) - np.mean(pop2)))/SE
    #one tailed test
    if stats.t.sf(T,df=sample_size-1) < alpha:
        return True
    else: return False


#make comparisons with Bonferroni correction
def Bonferroni(pop1,pop2,SE,comparisons):
    alpha = .05/comparisons
    c=0
    for _ in range(comparisons):
        sample1 = np.random.choice(pop1, (30))
        sample2 = np.random.choice(pop2, (30))
        T = (  (np.mean(sample1) - np.mean(sample2)) -  (np.mean(pop1) - np.mean(pop2))  )/SE
        if stats.t.sf(T,df=29) < alpha: c+=1.0
    #If I got significance in one of my comparisons, return True
    if c!=0:
        return True
    else:return False




#I create two population distributions
n1=5000
n2=5000
pop1 = create_pop(n1)
pop2 = create_pop(n2)

SE = ( (np.std(pop1)**2/30)+ (np.std(pop2)**2/30))**.5


#check multiple comparisons with alpha = .05
count=0
comparisons = 100

for _ in range(1000):
    a=0
    for x in range(comparisons):
        if testhypothesis (pop1,pop2,SE):
            a+=1
    if a!=0:
      count+=1

print "without  Bonferroni ", count/1000.0

count = 0
for _ in range(1000):
     if Bonferroni (pop1,pop2,SE,comparisons):
        count+=1


print "with  Bonferroni ", count/1000.0



