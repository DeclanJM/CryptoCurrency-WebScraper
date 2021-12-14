from typing import NamedTuple
from bs4 import BeautifulSoup
import requests
import csv
import datetime
import time
#_____________________________________________________________________        CSV Functions

file = "data.csv"
def read_csv(file):                 ####We know how to do this...    (But just in case ;)
    lst = []                        ##Create empty list
    with open(file, "r") as f:         ##Open the file in "r"ead mode (means no editing) as the value f
        csv_reader = csv.reader(f)      ##create a reader object with the CSV module and store the file as such
        for line in csv_reader:         ##Iterates through the file
            lst.append(line)        ##Adds each line to the empty list
    lst.pop(0)              ##Removes the first object (Usually the name of the data)
    return lst      ##Returns the list which contains the contents of the file

def append_list_as_row(file, list):         ###
    
    #print(list)         ###TESTING to see if the elements are properly being uploaded to the file   (Not as None)
    with open(file, 'a+', newline='\n') as write_obj:   # Opens file in append mode
        # Create a writer object from csv module
        csv_writer = csv.writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list)

#_________________________________________________________________________________________________________          #####Finds top 100 coins and appends it to a dictionary
def data_reader_uploader():  
    #file = read_csv("timer_file.csv")
    url = "https://coinmarketcap.com/"      ##Website we will be scraping
    result = requests.get(url).text         #Tests the https:// connection and returns the source
    doc = BeautifulSoup(result, "html.parser")      ##bs4 module creates a readble form of the source code in html format
         
    tbody = doc.tbody
    trs = tbody.contents
                                    ###______Uploads each value from the html into a dictionary with {Name : Dollar}
    prices = {}
    for tr in trs[:10]:                     ##Retrieves the first 10 obj (gets wonky after 10 for some reason)
        name, price = tr.contents[2:4]
        t10_name = (name.p.string)
        t10_price = (price.a.string)
        t10_price = t10_price.strip("\"")
        prices[t10_name] = t10_price
    #print(prices)           #### Prints the top 10 crypto prices

    for tr in trs[10:]:                     ###Retrieves 11-100
        name, price = tr.contents[2:4]
        name = name.a.text
        #print(name)
        price = price.span.text
        prices[name] = price

    dict = prices.items()
    items = dict
    date = datetime.datetime.now()      ##Returns the time in (Wkday, Mon, Day, 24:00:00, Year) format
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


#_________________________________________
def timer_func():
    data_reader_uploader()
    x = 1
    now = time.time()
    NEW_UPLOAD = 600
    timer = True
    while timer:
        print(x)
        if time.time() - now > NEW_UPLOAD:
            timer_func()
        else:
            time.sleep(1)
            x += 1
            continue

file = "timer_file.csv"
data = read_csv(file)
timer_func()