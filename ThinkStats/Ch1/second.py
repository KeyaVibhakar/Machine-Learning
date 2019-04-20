import survey

table = survey.Pregnancies()

table.ReadRecords()

liveBirth = int(0);

for rec in table.records:
       
   if rec.outcome==1 :
      liveBirth += 1
    
print( 'Total liveBirth = ' , liveBirth)
       
""" Documentation of total livebirth - for verification
https://www.icpsr.umich.edu/nsfg6/Controller?displayPage=labelDetails&fileCode=PREG&section=&subSec=8016&srtLabel=611932"""