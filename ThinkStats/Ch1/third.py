import survey

table = survey.Pregnancies()

table.ReadRecords()

firstChild = int(0)
otherChildren = int(0)

for rec in table.records:
       
   if rec.outcome==1 :
      if rec.birthord == 1:
          firstChild += 1
      else:
          otherChildren += 1
      
print( 'Total liveBirth for first child = ' , firstChild)

print( 'Total liveBirth for subsequent childred = ' , otherChildren )
       
""" Documentation of total livebirth - for verification
https://www.icpsr.umich.edu/nsfg6/Controller?displayPage=labelDetails&fileCode=PREG&section=&subSec=8016&srtLabel=611933
"""