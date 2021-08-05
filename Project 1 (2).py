import csv
import sys
import statistics
import matplotlib.pyplot as plt

print('Please enter a filename!')
filename = input()
try :
    file = open(filename)
except FileNotFoundError :
    print(filename, 'does not exist!')
    sys.exit()

reader = csv.reader(file)
header_row = next(reader)

counter = 0
counter1 = 0
add = 0
add1 = 0
counter2 = 0
counter3 = 0
var = []
name = []
list = []
appearance = []
year = []
dic = {}
good = 0
bad = 0
neutral = 0


for row in reader :
    # women
    if row[7] == 'Female Characters' :
        counter += 1
    if row[7] != 'Female Characters' :
        counter1 += 1
    totalcounter = counter + counter1
    # Appearances
    if row[7] == 'Female Characters' :
        try :
            add += int(row[10])
        except ValueError :
            add += 0
    if row[7] != 'Female Characters' :
        try :
            add1 += int(row[10])
        except ValueError :
            add1 += 0
    totaladd = add + add1
    # GSM
    if row[8] != '' :
        counter2 += 1
    if row[0] != '' :
        counter3 += 1
    # Oldest
    if row[12] != '' :
        var.append(int(row[12]))
    var.sort()
    if row[12] != '' :
        if var[-1] == int(row[12]) :
            name.append(row[1])
    # Most Appearances
    if row[10] != '' :
        list.append(int(row[10]))
    list.sort()
    if row[10] != '' :
        if list[-1] == int(row[10]) :
            appearance.append(row[1])
    # Statistics
    mean = statistics.mean(list)
    median = statistics.median(list)
    mode = statistics.mode(list)
    sd = statistics.pstdev(list)
    #Graph1
    if row[12] != '' :
        year.append(int(row[12]))
    year.sort()
    #Graph2
    if row[4] == 'Good Characters' :
        good += 1
    if row[4] == 'Bad Characters' :
        bad += 1
    if row[4] == 'Neutral Characters' :
        neutral += 1

    
for x in year :
    if x in dic.keys() :
        dic[x] = dic[x] + 1
    if x not in dic.keys() :
        dic.setdefault(x, 1)
            
labels = 'Good', 'Bad', 'Neutral'
sizes = [good, bad, neutral]
colors = ['red', 'green', 'orange']
explode = (0.1, 0, 0)
            
            
    

    
        
#Print      
    
print('There are', counter, 'Female Characters!')
print(counter / totalcounter * 100, 'percent of all characters are Female!')
print('There are', add, 'appearances by Female Characters!')
print(add / add1 *100, 'percent of all appearances are by Female Characters!')
print('There are', counter2, 'characters that are a gender or sexual minority!')
print(counter2 / counter3 *100, 'of all characters are a gender or sexual minority!')
print('The oldest character(s) is(are) : ', ', '.join(name))
print('The character(s) with the most appearances is(are): ', ', '.join(appearance))
print('The mean number of appearances of all characters is', mean)
print('The median number of appearances of all characters is', median)
print('The mode number of appearances of all characters is', mode)
print('The standard deviation of the number of appearances of all characters is', sd)

plt.plot(dic.keys(), dic.values())
plt.title('Graph of First-Appeared Characters', fontsize = 25)
plt.xlabel('Year')
plt.ylabel('# of characters')
plt.show()

plt.pie(sizes, explode=explode, labels= labels, colors = colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.show()
