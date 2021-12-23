from typing import NamedTuple
from bs4 import BeautifulSoup
import requests
import csv
import datetime
import time


inp_file = input("Enter a filename (no .csv): ")

file = inp_file + ".csv"
#file = "iter_test.csv"


#_____________________________________________________________________        CSV Functions
def read_csv(file):                 ####We know how to do this...    (But just in case ;)
    name_lst = []
    name_lst.append(file)
    print(name_lst)
    with open(file, "a+", newline = "\n") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(name_lst)
        lst = []                        ##Create empty list
    with open(file, "r") as f:          ##Open the file in "r"ead mode (means no editing) as the value f
        csv_reader = csv.reader(f)      ##create a reader object with the CSV module and store the file as such
        for line in csv_reader:         ##Iterates through the file
            lst.append(line)            ##Adds each line to the empty list
        
    lst.pop(0)                          ##Removes the first object (Usually the name of the data)
    
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
        print("{name}\n\tPrice:  {price}\n".format(name = name, price = price))     #Test to make sure it is doing anything (Comment out)
        append_list_as_row(file, [name, price])
#______________________________________________________________________________________________________________________________


#_________________________________________Timer function (Backbone of whole program)
def timer_func(timer_input, iteration):
    if iteration == 0:
        print("DONE")
        return
    else:
        iter = iteration - 1
        print("NOT DONE")

    #data_reader_uploader() 
    print("\ndata")
    x = 1
    now = time.time()              ##Registers the start time
    NEW_UPLOAD = timer_input                ###Timer is set in second
    timer = True if iter > 0 else False

    if timer == False:
        #main()
        return

    elif timer == True:
        while timer:
            if time.time() - now > NEW_UPLOAD:          ###Waits until time is up and then runs again (Recursion)
                print("EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
                timer_func(NEW_UPLOAD, iter)
            else:
                if time.time() - now < NEW_UPLOAD and not iter == 0:
                    print(x)
                    time.sleep(1)           ##Waits and counts up 1  (Another visual to make sure it's working, can be commented out)
                    x += 1
                    continue
                elif iter == 0:
                    break
    #print("end")
    """
    elif iteration == 0:
        quit()      ##Same \/
        #exit()     ##Same ^
    """    

######________________________________________________________________________________________________

def timer_func2(timer_input, iteration, level):
    print("data")       #retrieve data
    level += 1
    print("LEVEL: {}".format(level))
    if iteration > 0:
        iteration -= 1
        x = 1
        now = time.time()              ##Registers the start time
        NEW_UPLOAD = timer_input
        timer = True
        while timer:
            if time.time() - now > NEW_UPLOAD:
                print("RECURSION")
                timer_func2(timer_input, iteration, level)
            else:
                print(x)
                time.sleep(1)
                x += 1
            if level == iteration + 1:
                print("NO MORE")
                break
    else:
        return
        
######________________________________________________________________________________________________          Working timer function that works with iterations

def timer_func3(timer_input):
    data_reader_uploader()          ##As soon as the program starts it will upload the crypto prices at that time
    #print("\tData")
    x = 1
    now = time.time()              ##Registers the start time
    NEW_UPLOAD = timer_input                ###Timer is set in second
    timer = True
    while timer:
        if time.time() - now > NEW_UPLOAD:          ###Waits until time is up and then runs again (Recursion)
            return
        else:
            print("\t{}".format(x))
            time.sleep(1)           ##Waits and counts up 1  (Another visual to make sure it's working, can be commented out)
            x += 1
            continue

"""
Notes for timer_func3()
    No need for recursion, much easier to run individually in a for loop for the iterations
    That way we get 0 recursion errors that hurt our brain
"""

######________________________________________________________________________________________________



                                                ### MAIN ###
data = read_csv(file)

timer_set = int(input("How long between requests (Seconds):  "))
print()
total_it = int(input("Enter total number of requests:  "))
print()
    

if __name__ == "__main__":
    for num in range(total_it):
        print("Iteration #{}".format(num + 1))
        timer_func3(timer_set)
    print("\n\nSuccessfully Completed {iter} Iterations\n\tData has been uploaded to:  '{file}'\n\tFormatted in: '{dict}'\n\n".format(iter = total_it, file = file, dict = inp_file + "_dict.csv"))
    
###______________________________________Sets the file to be read and stored as the main crypto file


read_file = file                            
file = read_csv(read_file)

"""
FILES FOR SECOND PART!!!!! ^^^
"""


newl = []
for list in file:
    if len(list) > 1:       ##Checks to make sure the val actually contains data and isn't white space
        newl.append(list)
        #print("yes")
        #print(list)
    else:
        continue


dict = {}

for val in newl:
    val[1] = val[1].replace("\'", "").replace("$", "").replace("\'", "")            ##Removes the '$     ' from the money
    dict[val[0]] = []       #Creates a list for that key's value

for val in newl:            #####appends all values inside of the keys to a list in the val slot
    dict[val[0]].append(val[1])


dict_file = inp_file + "_dict.csv"

#f = csv.writer(open(dict_file, "a+"))
f = read_csv(dict_file)
f = csv.writer(open(dict_file, "w"))       ###Sets up the file reader under the variable f
for key,vals in dict.items():                   ##iterates through each item in the dict
    for val in vals:        
        val = val.replace(",", "")              ###Removes the , from every dollar amount so that it can be float and not str
        #print("Val: {}".format(val))  
        val = float(val)
        #print("{}:{}".format(key,vals))
    f.writerow([key,vals])              ###appends the csv file with a new row under the Coin : [List of dollar amounts] format