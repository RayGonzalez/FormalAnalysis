
#Code use to test for statistically significant difference in frequency of sausage eating between those who prefer Halal and those who don't

from openpyxl import load_workbook
import numpy as np
from scipy import stats

xl = load_workbook(filename='Results.xlsx', read_only=True)
ws = xl['1'] # ws is now an IterableWorksheet

def Significance(set1,set2):
    SE = ( (np.std(set1)**2/len(set1))+ (np.std(set2)**2/len(set2)) )
    T = (  (np.mean(set1)-np.mean(set2))-0)/SE

    if len(set1)> len(set2): F=len(set2)-1
    else: F= len(set1)-1

    return stats.t.sf(T,df=F)

Halal=[]
NoHalal=[]

for row in ws.rows:
   if(row[6].value)== "I prefer halal over regular meat" or (row[6].value)== "I only eat halal meats" :
       if(row[1].value)=="Multiple times per week":Halal.append(4)
       elif(row[1].value)=="About once a week":Halal.append(3)
       elif(row[1].value)=="About once a month":Halal.append(2)
       elif(row[1].value)=="Less than once a month":Halal.append(1)
       elif(row[1].value)=="Never":Halal.append(0)

   else:
       if(row[1].value)=="Multiple times per week":NoHalal.append(4)
       elif(row[1].value)=="About once a week":NoHalal.append(3)
       elif(row[1].value)=="About once a month":NoHalal.append(2)
       elif(row[1].value)=="Less than once a month":NoHalal.append(1)
       elif(row[1].value)=="Never":NoHalal.append(0)

print "p value=", Significance(NoHalal,Halal)

