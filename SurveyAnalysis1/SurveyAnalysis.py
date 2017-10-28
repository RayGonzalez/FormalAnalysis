
from openpyxl import load_workbook
import numpy as np
from scipy import stats

xl = load_workbook(filename='answers2.xlsx', read_only=True)
ws = xl['Form Responses 1'] # ws is now an IterableWorksheet

def Significance(set1,set2):
    SE = ( (np.std(set1)**2/len(set1))+ (np.std(set2)**2/len(set2)) )
    T = (  (np.mean(set1)-np.mean(set2))-0)/SE

    if len(set1)> len(set2): F=len(set2)-1
    else: F= len(set1)-1

    return stats.t.sf(T,df=F)


#lists for vegetarians/vegans
VMem= []
VHapp= []
VBodyConfidence= []
VFit=[]
VStress=[]
VSick=[]

#lists for male meat eaters
VMMem= []
VMHapp= []
VMBodyConfidence= []
VMFit=[]
VMStress=[]
VMSick=[]

#lists for female meat eaters
VFMem= []
VFHapp= []
VFBodyConfidence= []
VFFit=[]
VFStress=[]
VFSick=[]


#lists for meat eaters
MMem= []
MHapp= []
MBodyConfidence= []
MFit=[]
MStress=[]
MSick=[]

#lists for male meat eaters
MMMem= []
MMHapp= []
MMBodyConfidence= []
MMFit=[]
MMStress=[]
MMSick=[]

#lists for female meat eaters
MFMem= []
MFHapp= []
MFBodyConfidence= []
MFFit=[]
MFStress=[]
MFSick=[]

for row in ws.rows:
   if(row[8].value)== "Yes":    #If person is vegetarian/vegan
       #Body confidence
       if(row[2].value)=="Very comfortable":VBodyConfidence.append(3)
       elif(row[2].value)=="Moderately comfortable":VBodyConfidence.append(2)
       elif(row[2].value)=="Slightly comfortable":VBodyConfidence.append(1)
       elif(row[2].value)=="Neutral":VBodyConfidence.append(0)
       elif(row[2].value)=="Slightly uncomfortable":VBodyConfidence.append(-1)
       elif(row[2].value)=="Moderately uncomfortable":VBodyConfidence.append(-2)
       elif(row[2].value)=="Very uncomfortable":VBodyConfidence.append(-3)
            #Males
       if(row[10].value)== "Male":
          if(row[2].value)=="Very comfortable":VMBodyConfidence.append(3)
          elif(row[2].value)=="Moderately comfortable":VMBodyConfidence.append(2)
          elif(row[2].value)=="Slightly comfortable":VMBodyConfidence.append(1)
          elif(row[2].value)=="Neutral":VMBodyConfidence.append(0)
          elif(row[2].value)=="Slightly uncomfortable":VMBodyConfidence.append(-1)
          elif(row[2].value)=="Moderately uncomfortable":VMBodyConfidence.append(-2)
          elif(row[2].value)=="Very uncomfortable":VMBodyConfidence.append(-3)

       elif(row[10].value)== "Female":
          if(row[2].value)=="Very comfortable":VFBodyConfidence.append(3)
          elif(row[2].value)=="Moderately comfortable":VFBodyConfidence.append(2)
          elif(row[2].value)=="Slightly comfortable":VFBodyConfidence.append(1)
          elif(row[2].value)=="Neutral":VFBodyConfidence.append(0)
          elif(row[2].value)=="Slightly uncomfortable":VFBodyConfidence.append(-1)
          elif(row[2].value)=="Moderately uncomfortable":VFBodyConfidence.append(-2)
          elif(row[2].value)=="Very uncomfortable":VFBodyConfidence.append(-3)

       #Happiness
       if(row[3].value)=="Much higher":VHapp.append(3)
       elif(row[3].value)=="Moderately higher":VHapp.append(2)
       elif(row[3].value)=="Slightly higher":VHapp.append(1)
       elif(row[3].value)=="The same":VHapp.append(0)
       elif(row[3].value)=="Slightly lower":VHapp.append(-1)
       elif(row[3].value)=="Moderately lower":VHapp.append(-2)
       elif(row[3].value)=="Much lower":VHapp.append(-3)

              #Males
       if(row[10].value)== "Male":
            if(row[2].value)=="Very comfortable":VMHapp.append(3)
            elif(row[2].value)=="Moderately comfortable":VMHapp.append(2)
            elif(row[2].value)=="Slightly comfortable":VMHapp.append(1)
            elif(row[2].value)=="Neutral":VMHapp.append(0)
            elif(row[2].value)=="Slightly uncomfortable":VMHapp.append(-1)
            elif(row[2].value)=="Moderately uncomfortable":VMHapp.append(-2)
            elif(row[2].value)=="Very uncomfortable":VMHapp.append(-3)


       elif(row[10].value)== "Female":
            if(row[2].value)=="Very comfortable":VFHapp.append(3)
            elif(row[2].value)=="Moderately comfortable":VFHapp.append(2)
            elif(row[2].value)=="Slightly comfortable":VFHapp.append(1)
            elif(row[2].value)=="Neutral":VFHapp.append(0)
            elif(row[2].value)=="Slightly uncomfortable":VFHapp.append(-1)
            elif(row[2].value)=="Moderately uncomfortable":VFHapp.append(-2)
            elif(row[2].value)=="Very uncomfortable":VFHapp.append(-3)



       #Fitness
       if(row[4].value)=="Much higher":VFit.append(3)
       elif(row[4].value)=="Moderately higher":VFit.append(2)
       elif(row[4].value)=="Slightly higher":VFit.append(1)
       elif(row[4].value)=="The same":VFit.append(0)
       elif(row[4].value)=="Slightly lower":VFit.append(-1)
       elif(row[4].value)=="Moderately lower":VFit.append(-2)
       elif(row[4].value)=="Much lower":VFit.append(-3)

              #Males
       if(row[10].value)== "Male":
            if(row[2].value)=="Very comfortable":VMFit.append(3)
            elif(row[2].value)=="Moderately comfortable":VMFit.append(2)
            elif(row[2].value)=="Slightly comfortable":VMFit.append(1)
            elif(row[2].value)=="Neutral":VMFit.append(0)
            elif(row[2].value)=="Slightly uncomfortable":VMFit.append(-1)
            elif(row[2].value)=="Moderately uncomfortable":VMFit.append(-2)
            elif(row[2].value)=="Very uncomfortable":VMFit.append(-3)


       elif(row[10].value)== "Female":
            if(row[2].value)=="Very comfortable":VFFit.append(3)
            elif(row[2].value)=="Moderately comfortable":VFFit.append(2)
            elif(row[2].value)=="Slightly comfortable":VFFit.append(1)
            elif(row[2].value)=="Neutral":VFFit.append(0)
            elif(row[2].value)=="Slightly uncomfortable":VFFit.append(-1)
            elif(row[2].value)=="Moderately uncomfortable":VFFit.append(-2)
            elif(row[2].value)=="Very uncomfortable":VFFit.append(-3)


       #Memory
       if(row[5].value)=="Much higher":VMem.append(3)
       elif(row[5].value)=="Moderately higher":VMem.append(2)
       elif(row[5].value)=="Slightly higher":VMem.append(1)
       elif(row[5].value)=="The same":VMem.append(0)
       elif(row[5].value)=="Slightly lower":VMem.append(-1)
       elif(row[5].value)=="Moderately lower":VMem.append(-2)
       elif(row[5].value)=="Much lower":VMem.append(-3)

               #Males
       if(row[10].value)== "Male":
             if(row[2].value)=="Very comfortable":VMMem.append(3)
             elif(row[2].value)=="Moderately comfortable":VMMem.append(2)
             elif(row[2].value)=="Slightly comfortable":VMMem.append(1)
             elif(row[2].value)=="Neutral":VMMem.append(0)
             elif(row[2].value)=="Slightly uncomfortable":VMMem.append(-1)
             elif(row[2].value)=="Moderately uncomfortable":VMMem.append(-2)
             elif(row[2].value)=="Very uncomfortable":VMMem.append(-3)


       elif(row[10].value)== "Female":
             if(row[2].value)=="Very comfortable":VFMem.append(3)
             elif(row[2].value)=="Moderately comfortable":VFMem.append(2)
             elif(row[2].value)=="Slightly comfortable":VFMem.append(1)
             elif(row[2].value)=="Neutral":VFMem.append(0)
             elif(row[2].value)=="Slightly uncomfortable":VFMem.append(-1)
             elif(row[2].value)=="Moderately uncomfortable":VFMem.append(-2)
             elif(row[2].value)=="Very uncomfortable":VFMem.append(-3)


       #Stress
       if(row[6].value)=="Much more often":VStress.append(3)
       elif(row[6].value)=="Moderately more often":VStress.append(2)
       elif(row[6].value)=="Slightly more often":VStress.append(1)
       elif(row[6].value)=="The same":VStress.append(0)
       elif(row[6].value)=="Slightly less often":VStress.append(-1)
       elif(row[6].value)=="Moderately less often":VStress.append(-2)
       elif(row[6].value)=="Much lower":VStress.append(-3)


               #Males
       if(row[10].value)== "Male":
             if(row[2].value)=="Very comfortable":VMStress.append(3)
             elif(row[2].value)=="Moderately comfortable":VMStress.append(2)
             elif(row[2].value)=="Slightly comfortable":VMStress.append(1)
             elif(row[2].value)=="Neutral":VMStress.append(0)
             elif(row[2].value)=="Slightly uncomfortable":VMStress.append(-1)
             elif(row[2].value)=="Moderately uncomfortable":VMStress.append(-2)
             elif(row[2].value)=="Very uncomfortable":VMStress.append(-3)


       elif(row[10].value)== "Female":
             if(row[2].value)=="Very comfortable":VFStress.append(3)
             elif(row[2].value)=="Moderately comfortable":VFStress.append(2)
             elif(row[2].value)=="Slightly comfortable":VFStress.append(1)
             elif(row[2].value)=="Neutral":VFStress.append(0)
             elif(row[2].value)=="Slightly uncomfortable":VFStress.append(-1)
             elif(row[2].value)=="Moderately uncomfortable":VFStress.append(-2)
             elif(row[2].value)=="Very uncomfortable":VFStress.append(-3)


       #Sickness
       if(row[7].value)=="Much more often":VSick.append(3)
       elif(row[7].value)=="Moderately more often":VSick.append(2)
       elif(row[7].value)=="Slightly more often":VSick.append(1)
       elif(row[7].value)=="The same":VSick.append(0)
       elif(row[7].value)=="Slightly less often":VSick.append(-1)
       elif(row[7].value)=="Moderately less often":VSick.append(-2)
       elif(row[7].value)=="Much lower":VSick.append(-3)


               #Males
       if(row[10].value)== "Male":
             if(row[2].value)=="Very comfortable":VMSick.append(3)
             elif(row[2].value)=="Moderately comfortable":VMSick.append(2)
             elif(row[2].value)=="Slightly comfortable":VMSick.append(1)
             elif(row[2].value)=="Neutral":VMSick.append(0)
             elif(row[2].value)=="Slightly uncomfortable":VMSick.append(-1)
             elif(row[2].value)=="Moderately uncomfortable":VMSick.append(-2)
             elif(row[2].value)=="Very uncomfortable":VMSick.append(-3)


       elif(row[10].value)== "Female":
             if(row[2].value)=="Very comfortable":VFSick.append(3)
             elif(row[2].value)=="Moderately comfortable":VFSick.append(2)
             elif(row[2].value)=="Slightly comfortable":VFSick.append(1)
             elif(row[2].value)=="Neutral":VFSick.append(0)
             elif(row[2].value)=="Slightly uncomfortable":VFSick.append(-1)
             elif(row[2].value)=="Moderately uncomfortable":VFSick.append(-2)
             elif(row[2].value)=="Very uncomfortable":VFSick.append(-3)








   else:  #Meat eaters
         #Body confidence
         if(row[2].value)=="Very comfortable":MBodyConfidence.append(3)
         elif(row[2].value)=="Moderately comfortable":MBodyConfidence.append(2)
         elif(row[2].value)=="Slightly comfortable":MBodyConfidence.append(1)
         elif(row[2].value)=="Neutral":MBodyConfidence.append(0)
         elif(row[2].value)=="Slightly uncomfortable":MBodyConfidence.append(-1)
         elif(row[2].value)=="Moderately uncomfortable":MBodyConfidence.append(-2)
         elif(row[2].value)=="Very uncomfortable":MBodyConfidence.append(-3)
              #Males
         if(row[10].value)== "Male":
            if(row[2].value)=="Very comfortable":MMBodyConfidence.append(3)
            elif(row[2].value)=="Moderately comfortable":MMBodyConfidence.append(2)
            elif(row[2].value)=="Slightly comfortable":MMBodyConfidence.append(1)
            elif(row[2].value)=="Neutral":MMBodyConfidence.append(0)
            elif(row[2].value)=="Slightly uncomfortable":MMBodyConfidence.append(-1)
            elif(row[2].value)=="Moderately uncomfortable":MMBodyConfidence.append(-2)
            elif(row[2].value)=="Very uncomfortable":MMBodyConfidence.append(-3)


         elif(row[10].value)== "Female":
            if(row[2].value)=="Very comfortable":MFBodyConfidence.append(3)
            elif(row[2].value)=="Moderately comfortable":MFBodyConfidence.append(2)
            elif(row[2].value)=="Slightly comfortable":MFBodyConfidence.append(1)
            elif(row[2].value)=="Neutral":MFBodyConfidence.append(0)
            elif(row[2].value)=="Slightly uncomfortable":MFBodyConfidence.append(-1)
            elif(row[2].value)=="Moderately uncomfortable":MFBodyConfidence.append(-2)
            elif(row[2].value)=="Very uncomfortable":MFBodyConfidence.append(-3)

         #Happiness
         if(row[3].value)=="Much higher":MHapp.append(3)
         elif(row[3].value)=="Moderately higher":MHapp.append(2)
         elif(row[3].value)=="Slightly higher":MHapp.append(1)
         elif(row[3].value)=="The same":MHapp.append(0)
         elif(row[3].value)=="Slightly lower":MHapp.append(-1)
         elif(row[3].value)=="Moderately lower":MHapp.append(-2)
         elif(row[3].value)=="Much lower":MHapp.append(-3)

                #Males
         if(row[10].value)== "Male":
              if(row[2].value)=="Very comfortable":MMHapp.append(3)
              elif(row[2].value)=="Moderately comfortable":MMHapp.append(2)
              elif(row[2].value)=="Slightly comfortable":MMHapp.append(1)
              elif(row[2].value)=="Neutral":MMHapp.append(0)
              elif(row[2].value)=="Slightly uncomfortable":MMHapp.append(-1)
              elif(row[2].value)=="Moderately uncomfortable":MMHapp.append(-2)
              elif(row[2].value)=="Very uncomfortable":MMHapp.append(-3)


         elif(row[10].value)== "Female":
              if(row[2].value)=="Very comfortable":MFHapp.append(3)
              elif(row[2].value)=="Moderately comfortable":MFHapp.append(2)
              elif(row[2].value)=="Slightly comfortable":MFHapp.append(1)
              elif(row[2].value)=="Neutral":MFHapp.append(0)
              elif(row[2].value)=="Slightly uncomfortable":MFHapp.append(-1)
              elif(row[2].value)=="Moderately uncomfortable":MFHapp.append(-2)
              elif(row[2].value)=="Very uncomfortable":MFHapp.append(-3)



         #Fitness
         if(row[4].value)=="Much higher":MFit.append(3)
         elif(row[4].value)=="Moderately higher":MFit.append(2)
         elif(row[4].value)=="Slightly higher":MFit.append(1)
         elif(row[4].value)=="The same":MFit.append(0)
         elif(row[4].value)=="Slightly lower":MFit.append(-1)
         elif(row[4].value)=="Moderately lower":MFit.append(-2)
         elif(row[4].value)=="Much lower":MFit.append(-3)

                #Males
         if(row[10].value)== "Male":
              if(row[2].value)=="Very comfortable":MMFit.append(3)
              elif(row[2].value)=="Moderately comfortable":MMFit.append(2)
              elif(row[2].value)=="Slightly comfortable":MMFit.append(1)
              elif(row[2].value)=="Neutral":MMFit.append(0)
              elif(row[2].value)=="Slightly uncomfortable":MMFit.append(-1)
              elif(row[2].value)=="Moderately uncomfortable":MMFit.append(-2)
              elif(row[2].value)=="Very uncomfortable":MMFit.append(-3)


         elif(row[10].value)== "Female":
              if(row[2].value)=="Very comfortable":MFFit.append(3)
              elif(row[2].value)=="Moderately comfortable":MFFit.append(2)
              elif(row[2].value)=="Slightly comfortable":MFFit.append(1)
              elif(row[2].value)=="Neutral":MFFit.append(0)
              elif(row[2].value)=="Slightly uncomfortable":MFFit.append(-1)
              elif(row[2].value)=="Moderately uncomfortable":MFFit.append(-2)
              elif(row[2].value)=="Very uncomfortable":MFFit.append(-3)


         #Memory
         if(row[5].value)=="Much higher":MMem.append(3)
         elif(row[5].value)=="Moderately higher":MMem.append(2)
         elif(row[5].value)=="Slightly higher":MMem.append(1)
         elif(row[5].value)=="The same":MMem.append(0)
         elif(row[5].value)=="Slightly lower":MMem.append(-1)
         elif(row[5].value)=="Moderately lower":MMem.append(-2)
         elif(row[5].value)=="Much lower":MMem.append(-3)

                 #Males
         if(row[10].value)== "Male":
               if(row[2].value)=="Very comfortable":MMMem.append(3)
               elif(row[2].value)=="Moderately comfortable":MMMem.append(2)
               elif(row[2].value)=="Slightly comfortable":MMMem.append(1)
               elif(row[2].value)=="Neutral":MMMem.append(0)
               elif(row[2].value)=="Slightly uncomfortable":MMMem.append(-1)
               elif(row[2].value)=="Moderately uncomfortable":MMMem.append(-2)
               elif(row[2].value)=="Very uncomfortable":MMMem.append(-3)


         elif(row[10].value)== "Female":
               if(row[2].value)=="Very comfortable":MFMem.append(3)
               elif(row[2].value)=="Moderately comfortable":MFMem.append(2)
               elif(row[2].value)=="Slightly comfortable":MFMem.append(1)
               elif(row[2].value)=="Neutral":MFMem.append(0)
               elif(row[2].value)=="Slightly uncomfortable":MFMem.append(-1)
               elif(row[2].value)=="Moderately uncomfortable":MFMem.append(-2)
               elif(row[2].value)=="Very uncomfortable":MFMem.append(-3)


         #Stress
         if(row[6].value)=="Much more often":MStress.append(3)
         elif(row[6].value)=="Moderately more often":MStress.append(2)
         elif(row[6].value)=="Slightly more often":MStress.append(1)
         elif(row[6].value)=="The same":MStress.append(0)
         elif(row[6].value)=="Slightly less often":MStress.append(-1)
         elif(row[6].value)=="Moderately less often":MStress.append(-2)
         elif(row[6].value)=="Much lower":MStress.append(-3)


                 #Males
         if(row[10].value)== "Male":
               if(row[2].value)=="Very comfortable":MMStress.append(3)
               elif(row[2].value)=="Moderately comfortable":MMStress.append(2)
               elif(row[2].value)=="Slightly comfortable":MMStress.append(1)
               elif(row[2].value)=="Neutral":MMStress.append(0)
               elif(row[2].value)=="Slightly uncomfortable":MMStress.append(-1)
               elif(row[2].value)=="Moderately uncomfortable":MMStress.append(-2)
               elif(row[2].value)=="Very uncomfortable":MMStress.append(-3)


         elif(row[10].value)== "Female":
               if(row[2].value)=="Very comfortable":MFStress.append(3)
               elif(row[2].value)=="Moderately comfortable":MFStress.append(2)
               elif(row[2].value)=="Slightly comfortable":MFStress.append(1)
               elif(row[2].value)=="Neutral":MFStress.append(0)
               elif(row[2].value)=="Slightly uncomfortable":MFStress.append(-1)
               elif(row[2].value)=="Moderately uncomfortable":MFStress.append(-2)
               elif(row[2].value)=="Very uncomfortable":MFStress.append(-3)


         #Sickness
         if(row[7].value)=="Much more often":MSick.append(3)
         elif(row[7].value)=="Moderately more often":MSick.append(2)
         elif(row[7].value)=="Slightly more often":MSick.append(1)
         elif(row[7].value)=="The same":MSick.append(0)
         elif(row[7].value)=="Slightly less often":MSick.append(-1)
         elif(row[7].value)=="Moderately less often":MSick.append(-2)

                  #Males
         if(row[10].value)== "Male":
                if(row[2].value)=="Very comfortable":MMSick.append(3)
                elif(row[2].value)=="Moderately comfortable":MMSick.append(2)
                elif(row[2].value)=="Slightly comfortable":MMSick.append(1)
                elif(row[2].value)=="Neutral":MMSick.append(0)
                elif(row[2].value)=="Slightly uncomfortable":MMSick.append(-1)
                elif(row[2].value)=="Moderately uncomfortable":MMSick.append(-2)
                elif(row[2].value)=="Very uncomfortable":MMSick.append(-3)

         elif(row[10].value)== "Female":
                if(row[2].value)=="Very comfortable":MFSick.append(3)
                elif(row[2].value)=="Moderately comfortable":MFSick.append(2)
                elif(row[2].value)=="Slightly comfortable":MFSick.append(1)
                elif(row[2].value)=="Neutral":MFSick.append(0)
                elif(row[2].value)=="Slightly uncomfortable":MFSick.append(-1)
                elif(row[2].value)=="Moderately uncomfortable":MFSick.append(-2)
                elif(row[2].value)=="Very uncomfortable":MFSick.append(-3)

print "First result is with all individuals, second with males, third with females"
print "Body Comfort"
print Significance(VBodyConfidence,MBodyConfidence)
print Significance(VMBodyConfidence,MBodyConfidence)
print Significance(VFBodyConfidence,MFBodyConfidence)
print "Fitness"
print Significance(VFit,MFit)
print Significance(VMFit,MMFit)
print Significance(VFFit,MFFit)
print "Memory"
print Significance(VMem,MMem)
print Significance(VMMem,MMMem)
print Significance(VFMem,MFMem)
print "Sickness"
print Significance(VSick,MSick)
print Significance(VMSick,MMSick)
print Significance(VFSick,MFSick)
print "Stress"
print Significance(VStress,MStress)
print Significance(VMStress,MMStress)
print Significance(VFStress,MFStress)
print "Happiness"
print Significance(VHapp,MHapp)
print Significance(VMHapp,MMHapp)
print Significance(VFHapp,MFHapp)

print "Veggie change in memory:"
print np.mean(VMem)
print "Meat eater change in memory:"
print np.mean(MMem)

