__author__ = 'raymundogonzalez'

import csv
import matplotlib.pyplot as plt
import random

data_file = open('knn_data.csv')
reader = csv.reader(data_file)
my_DataList = []

#Create datalist from file
for row in reader:
    my_DataList.append(row)

#Create lists for x and y values and the labels (going to need this for the scatter plot)
x=[]
y=[]
labels=[]

for point in my_DataList:
    x.append(point[0])
    y.append(point[1])
    labels.append(point[2])

#Receives a list of points and a refernce point as input
#Gives me a list of tuples with distances from the nth point and the labels of those points
def my_distance(Points,n):
    dist_list = []
    tuple_list =[]
    count=0
    ref_point= (Points[n])
    for i in Points:
        distanceX = (float(i[0])-float(ref_point[0]))**2
        distanceY = (float(i[1])-float(ref_point[1]))**2
        distance = (distanceX+distanceY)**0.5
        dist_list.append(distance)

        #Make tuple list with distances and labels
    for x in dist_list:
        tuple_list.append((x, Points[count][2]))
        count+=1
    return tuple_list

#Need to define this because I'll use it on P_label
def getKey(item):
     return item[0]

#Input: list of points (Datalist), reference point, k value
#Gets most frequent label for k nearest points to a point n (Predicted label)
def P_label(Points,n,k):
    MagicList= my_distance(Points,n)
    MagicList.sort(key=getKey)
    #Makes sublist with the distances to the k nearest points to n and their neighbors
    NewList = MagicList[1:k+1]
    count0=0
    count1=0
    #looks for the most frequent label in the neighbors and returns it
    for x in NewList:
        if x[1]=='0':
            count0+=1
        else:
            count1+=1
    if count1<count0:
        return 0
    elif count0<count1:
        return 1
    #If there is a tie, lets consider one less neighboor, and repeat
    else:
         NewList = MagicList[1:k]
         for x in NewList:
            if x[1]=='0':
                count0+=1
            else:
                count1+=1
         if count1<count0:
            return 0
         else:
            return 1


#Creates the scatterplot given the points and labels (I can give it either predicted labels or real labels)
def DoPlot(x,y,labels):
    plt.scatter(x,y,c=labels,s=100)
    plt.show()

#Input: K value, and a boolean to say either if I want a plot or not.
#Gives me a list of predicted labels and actual labels, calculates percentage of accuracy
#If plot=true, gives me a plot of the points and their predicted labels.
def Magic(k,plot):
    Result_list=[]
    #variable for number/percentage of right predictions
    count=0
    labels=[]

    for c in range(0,len(my_DataList)):
        l=P_label(my_DataList,c,k)
        labels.append(l)
        Result_list.append((l,int(my_DataList[c][2])))
    for a in Result_list:
        if a[0]==a[1]:
            count+=1
    if plot==True:
        DoPlot(x,y,labels)
    return count/600.0*100

#Gives the best k using brute force
def BruteForce():
    Klist=[]
    Score=0
    BestK=0
    #gets a list with the values of k and the number of correct results
    #Assumption: No need to look for k values bigger than 300 (half the total number of points)
    for k in range(1,300):
        Klist.append((k,Magic(k,False)))
    #OPTIMIZATION: I don't need to sort the whole list, I just need to find the greatest score.
    #This takes more lines of code than just sorting, but lest computational power
    for a in Klist:
        if Score<a[1]:
            Score=a[1]
            BestK=a[0]
    print BestK
    #Create plot with predicted labels
    Magic(BestK,True)
    print Score
    #print Klist




#Greedy algorithm for getting the best k. What I am doing is simulated annealing
def Greedy():
    #Generate 2 random neighboring solutions and check for scores
    #No need to check for values of k higher than 300
    k1=int(random.uniform(1,300))
    count=0
    score1=0
    #Greedy way to get at least 90% accuracy
    while (score1<90 and count<50) :
        score1=Magic(k1,False)
        k2=int(random.uniform(k1-20,k1+20))
        score2=Magic(k2,False)
        count+=1
        #If second solution better than first one, move there
        if score2>score1:
             k1=k2
        #sometimes move to a worse solution
        #But I don't want to move to a worse solution if I am about to finish
        elif (random.random()>.90):
            k1=k2
    print "k=",k1
    #I am doing this in order to show the plot of predicted labels
    print "accuracy:" ,Magic(k1,True)


#Get plot with real labels
DoPlot(x,y,labels)

Greedy()
BruteForce()
