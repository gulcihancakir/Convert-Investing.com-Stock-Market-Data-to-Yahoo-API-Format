import csv
import sys

filename=sys.argv[1]

liste=[]

with open(filename, newline='') as csvfile:
    
  
    reader = csv.reader(csvfile)
    baslik = next(reader)
   
    for row in reader:
    
        add_list=row[0].split('.')
        
        
        reverse_list = add_list[::-1]
        Date = "-".join(reverse_list)
       
        
        d = [Date,
        row[2].replace('.','').replace(',','.'),
        row[3].replace('.','').replace(',','.'),
        row[4].replace('.','').replace(',','.'),
        row[1].replace('.','').replace(',','.'),
        row[5].replace(',','').replace('K','0'*3).replace('M','0'*6).replace('B','0'*9).replace('-','0')]
        

        
        liste.append(d)
    liste.reverse()
    
    
    

    header = ['Date','Open','High','Low','Close','Volume']
    with open(filename + '-converted','w',newline='') as csvfile:
            
        writer = csv.writer(csvfile)
        writer.writerow(header)
        
        for i in liste:

            writer.writerow(i)
       
            
                