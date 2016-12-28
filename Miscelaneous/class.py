import numpy as np

def create_pop(n):
    # A
    distrib = 1000 * np.random.random_sample((n))
    #returns an array with the population
    return distrib

population_size = int(raw_input("Enter a population size:"))
population = create_pop(population_size)
std_pop= np.std(population)

print "In order to have a fixed number of degrees of freedom later, we will use sample size 10"
sample_size = 10

#Way 1 of getting standard error
SE1=std_pop/(sample_size**.5)
print "Standard Error for sampling distribution of sample size 10: ",SE1

#Using population stdev
count1=0
for x in range(0,100000):
    sample = np.random.choice(population, (sample_size))
    #Here I use z score for 95% confidence.
    if np.mean(population) >= np.mean(sample)-1.96*SE1 and np.mean(population) <= np.mean(sample)+1.96*SE1:
        count1+=1
print count1/100000.0

#Challenge
#Using sample stdev
count2=0
for x in range(0,100000):
    sample = np.random.choice(population, (sample_size))

   #I got errors trying to get the sample standard deviation directly, so I will just multiply by N and divide by N-1
    SampleSTD= np.std(population)*population_size/(population_size-1)
    SE2 = SampleSTD/(sample_size**.5)

        #Here I use t score for 9 degrees of freedom, 95% confidence
    if np.mean(population) >= np.mean(sample)-2.262*SE2 and np.mean(population) <= np.mean(sample)+2.262*SE2:
        count2+=1
print count2/100000.0



