from typing import NamedTuple
from bs4 import BeautifulSoup
import requests
import csv
import datetime
import time
#_____________________________________________________________________        CSV Functions

file = "data.csv"
def read_csv(file):
    lst = []
    with open(file, "r") as f:
        csv_reader = csv.reader(f)
        for line in csv_reader:
            lst.append(line)
    lst.pop(0)
    return lst

def append_list_as_row(file, list):         ###
    
    #print(list)         ###TESTING to see if the elements are properly being uploaded to the file   (Not as None)
    with open(file, 'a+', newline='\n') as write_obj:   # Opens file in append mode
        # Create a writer object from csv module
        csv_writer = csv.writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list)

#_________________________________________________________________________________________________________          #####Finds top 100 coins and appends it to a dictionary
#def data_reader_uploader(file):  
url = "https://coinmarketcap.com/"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")
#print(doc.prettify())



#print(trs[0].next_sibling)      ###Moves down the tree
#print(trs[1].previous_sibling)    ###Moves up the tree
#print(list(trs[0].next_siblings))
#print(list(trs[0].content))     ##Also works with .children or .descendant

prices = {}
tbody = doc.tbody
trs = tbody.contents

for tr in trs[:10]:
    name, price = tr.contents[2:4]
    t10_name = (name.p.string)
    t10_price = (price.a.string)
    t10_price = t10_price.strip("\"")
    prices[t10_name] = t10_price
#print(prices)           #### Prints the top 10 crypto prices

for tr in trs[10:]:
    name, price = tr.contents[2:4]
    name = name.a.text
    #print(name)
    price = price.span.text
    prices[name] = price



dict = prices.items()
items = dict
date = datetime.datetime.now()
#print(items)
append_list_as_row(file, [])
append_list_as_row(file, [])
append_list_as_row(file, [date.strftime("%c")])             ####Appends the file with the time stamp and has additional spacing for readability
append_list_as_row(file, [])
append_list_as_row(file, [])

for val in items:
    name = val[0]
    price = val[1]
    print("{name}\n\tPrice:  {price}\n".format(name = name, price = price))
    append_list_as_row(file, [name, price])
#______________________________________________________________________________________________________________________________

file = "timer_file.csv"
data = read_csv(file)

#_________________________________________
def timer(data, doc):
    now = time.time()
    NEW_UPLOAD = 5
    timer = True
    while timer:
        if time.time() - now > NEW_UPLOAD:
            timer()
        else:
            continue

#timer(data, doc)