import csv
import itertools

colors = []
dates = []
with open('example.txt') as textfile:
    readCSV = csv.reader(textfile, delimiter=',')
    for row in readCSV:
        colors.append(row[3])
        dates.append(row[0])
        print row
        print row[0]
        print row[0],row[1],row[2],

print colors
print dates

dict = dict(zip(dates,colors))

print dict


#Getting What To Write To File

points = int(100)

#Actually Writing It
saveFile = open("boh.txt", "a")
newline = "tonno," + str(points)
saveFile.write(newline)
saveFile.close()
