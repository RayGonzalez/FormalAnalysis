#import library
import matplotlib.pyplot as plt

# openning lists for the variables x,y and label

x = []
y = []
label = []

#returns the Euclenean distance between two points
def distance(x1, x2, y1, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    
    

#open the file with the data
f = open('knn_data.csv')

#read the file (line by line)
for line in f:
	#splitting the data
	a = line.split(',')
	#take the xs out and pack them in another list
	x.append(float(a[0]))
	y.append(float(a[1]))
	label.append(int(a[2]))
		
f.close()

#list of the list of distance - all the possible distances between any two points in the data (599*600 = 359400)
overall_array = []
#analysing each dot and comparing them with all the other dots
for i in xrange(len(x)):
    #list of the distance between each data point to all the other data points (599)
    di_array = []
    for j in xrange(len(x)):
        if i != j:
            di = distance(x[i], x[j], y[i], y[j])
            #relate the distance to each point j, through a new list
            di_array.append([di, label[j]])
    #sort it in increasing order
    di_array.sort()
    
    #counters
    white_count = 0
    black_count = 0

    #list with all the truth values for k
    truth_value=[]

    for k in xrange(1, len(x)):
        if di_array[k-1][1] == 0:
            white_count += 1
        else:
            black_count += 1
        if (label[i] == 0 and white_count > black_count) or (label[i] == 1 and white_count <= black_count):
            truth_value.append(True)
        else:
            truth_value.append(False)
    overall_array.append(truth_value)

success_k = []
best_rate = 0
best_k = 0
for k in xrange(1, len(x)):
    count = 0
    for i in xrange(len(x)):
        if overall_array[i][k - 1]:
            count += 1
    success_rate = count / float(len(x))
    if success_rate > best_rate:
        best_rate = success_rate
        best_k = k
    success_k.append(success_rate)

print('The best k is ' + str(best_k))

plt.plot(xrange(1, len(x)), success_k)

#plot the data - each x and y value are colored according to their classification in label (1 or 0)
#plt.scatter(x, y, c=label, cmap='summer')
plt.show()
