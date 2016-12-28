import random
import matplotlib.pyplot as plt

StoresR = []
ResultsR = []
ResultsU = []
StoresU = []
countWeek = []


#number of weeks to run the simulation
Weeks = int(raw_input("Enter the number of weeks:"))

for i in range(0,Weeks):
    countWeek.append(i+1)


def runRandom(Weeks):
    for x in range(0,499):
        StoresR.append((random.randint(0,499)))
    #number of stores that sell GMOs first
    S = random.randint(0,500)
    ResultsR.append(S)

    for i in range(1,Weeks):
        S2=0
        for x in StoresR:
            if S>=x: S2+=1

        ResultsR.append(S2)
        S=S2
    plt.scatter(countWeek,ResultsR,color = "maroon", linewidth=3)
    plt.xlim([0,Weeks+1])
    plt.ylim([-5,505])
    plt.ylabel('stores selling')
    plt.title('stores with random thresholds selling GMOs')
    plt.xlabel('week number')
    plt.show()

def runUniform(Weeks):
    t = int(raw_input("Threshold of stores:"))
    #number of stores that sell GMOs first
    for x in range(0,500):
        StoresU.append(t)
    S = random.randint(0,500)
    ResultsU.append(S)

    for i in range(1,Weeks):
        S2=0
        for x in StoresU:
            if S>=x: S2+=1

        ResultsU.append(S2)
        S=S2
    plt.scatter(countWeek,ResultsU,color = "maroon", linewidth=3)
    plt.xlim([0,Weeks+1])
    plt.ylim([-5,505])
    plt.title('stores with uniform thresholds selling GMOs')
    plt.ylabel('stores selling')
    plt.xlabel('week number')
    plt.show()

print "Running with random thresholds"
runRandom(Weeks)

print "Running with uniform threshold"
runUniform(Weeks)