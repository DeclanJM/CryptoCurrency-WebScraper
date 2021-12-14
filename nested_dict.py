import csv
from typing import DefaultDict
from collections import defaultdict
import pprint

###________________________________Reads the file and returns in a list
def read_csv(file):
    lst = []
    with open(file, "r") as f:
        #dict_reader = csv.DictReader(f)
        #for line in dict_reader:
        csv_reader = csv.reader(f)
        for line in csv_reader:
            lst.append(line)
    lst.pop(0)
    return lst

###______________________________________Sets the file to be read and stored as the main crypto file
file = "timer_file.csv"
file = read_csv(file)
#print(file)

newl = []
for list in file:
    if len(list) > 1:       ##Checks to make sure the val actually contains data and isn't white space
        newl.append(list)
        #print("yes")
        #print(list)
    else:
        continue

#print(newl)

dict = {}

for val in newl:
    val[1] = val[1].replace("\'", "").replace("$", "").replace("\'", "")            ##Removes the '$      ' from the money
    dict[val[0]] = []       #Creates a list for that key's value
    """
    
    print(str(dict[val[0]]))
    print(str(dict[val[1]]))
    dict[val[0]] = []
    dict[val[0]].append(dict[val[1]])
    """
for val in newl:            #####appends all values inside of the keys to a list in the val slot
    dict[val[0]].append(val[1])

#pprint.pprint(dict)        ##Prints in a readable way
#print(newl)

"""with open("Dict_data.csv", "w") as f:
    csv_writer = csv.writer(f)
    for key, val in dict.items():
        f.write(str([key,val]))"""

f = csv.writer(open("Dict_data.csv", "w"))          
for key,vals in dict.items():
    for val in vals:
        val = val.replace(",", "")
        #print("Val: {}".format(val))
        val = float(val)
        #print("{}:{}".format(key,vals))
    f.writerow([key,vals])

