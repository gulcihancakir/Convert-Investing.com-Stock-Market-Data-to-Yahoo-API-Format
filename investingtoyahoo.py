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
        
        if row[5].endswith('K'):
            x=row[5].split('K')
            y=float(x[0].replace(',','.'))
            row[5]=int(y)*10**3

        elif row[5].endswith('M'):
            x=row[5].split('M')
            y=float(x[0].replace(',','.'))
            row[5]=int(y)*10**6

        elif row[5].endswith('B'):
            x=row[5].split('B')
            y=float(x[0].replace(',','.'))
            row[5]=int(y)*10**9

        elif row[5].endswith('-'):
            row[5]=0
       
        d = [Date,
        row[2].replace('.','').replace(',','.'),
        row[3].replace('.','').replace(',','.'),
        row[4].replace('.','').replace(',','.'),
        row[1].replace('.','').replace(',','.'),
        row[5]]
            
        liste.append(d)
    liste.reverse()
    
    name = filename.split('.')
    name.insert(1,'-converted.')
    filename = ''.join(name)
    print(filename)
    header = ['Date','Open','High','Low','Close','Volume']
    with open(filename,'w',newline='') as csvfile:
            
        writer = csv.writer(csvfile)
        writer.writerow(header)
        
        for i in liste:

            writer.writerow(i)
       
            
                