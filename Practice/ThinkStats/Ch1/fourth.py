import survey

table = survey.Pregnancies()

table.ReadRecords()

firstChild = int(0)
fPregLength = int(0)

otherChildren = int(0)
oPregLength = int(0)

for rec in table.records:
       
   if rec.outcome==1 :
      if rec.birthord == 1:
          firstChild += 1
          fPregLength += rec.prglength
          
      else:
          otherChildren += 1
          oPregLength += rec.prglength
          
fAvgPregLen = fPregLength / firstChild

oAvgPregLen = oPregLength / otherChildren
      
print( 'Average pregnancy length for first child = ' , fAvgPregLen)

print( 'Average pregnancy length for subsequent childred = ' , oAvgPregLen )


       
""" Documentation of total livebirth - for verification
https://www.icpsr.umich.edu/nsfg6/Controller?displayPage=labelDetails&fileCode=PREG&section=&subSec=8016&srtLabel=611933
"""

