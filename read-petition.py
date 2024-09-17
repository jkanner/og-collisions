import csv

fn = 'collision-data.csv'
i = 0

#outfile = open('petition-list.txt', 'w')

outfile = open('og-only.csv', 'w', newline='')
output = csv.writer(outfile)
    

with open(fn, newline='') as csvfile:
        csvreader = csv.reader(csvfile)

        for indx, row in enumerate(csvreader):

	        #-- Check if OG
                street = row[5]
                cross  = row[6]
                target = "ORANGE GROVE"
                
                if target in street or target in cross:
                        print(street, cross)
                        i+=1
                        output.writerow(row)

outfile.close()
print("Found {0} collisions".format(i))
                
		
