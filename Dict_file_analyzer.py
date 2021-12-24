import csv

def read_csv(file):                 ####We know how to do this...    (But just in case ;)
    name_lst = []
    name_lst.append(file)
    print(name_lst)             ##COMMENT OUT 
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

read_file = "30s15m.csv"                            
file = read_csv(read_file)

"""
FILES FOR SECOND PART!!!!! ^^^
"""

def dict_analyzer(file):
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


    #dict_file = "30s15m_dict.csv"

    for key,vals in dict.items():                   ##iterates through each item in the dict
        for val in vals:        
            val = val.replace(",", "")              ###Removes the , from every dollar amount so that it can be float and not str
            #print("Val: {}".format(val))  
            val = float(val)

    print(dict.keys())

    filter = input("\nEnter a coin: ")
    print()

    if filter in dict.keys():
        prices = dict[filter]
        chg_lst = []
        for price in prices:
            price = price.replace(",", "")
            price = float(price)
            chg_lst.append(price)
        first = float(chg_lst[1])
        last = float(chg_lst[-1])
        p_chg = first / last * 100

        total = 0
        amt = 0
        max = -99999999
        min = 99999999
        for price in prices:
            price = price.replace(",", "")
            price = float(price)
            """if price == prices[1]:
                first = price
                print(first)
            if price == prices[-1:]:
                last = prices[-1]
                print(last)"""
            total += price
            amt += 1
            if price < min:
                min = price
            if price > max:
                max = price
        #p_chg = first/last * 100
        
        print("STATS:\n\tAverage Price:  {:.2f}\n\tMaximum Price:  {:.2f}\n\tMinimum Price:  {:.2f}\n\tPercent Change:  {:.2f}%".format(total/amt, max, min, p_chg))

    else:
        print("Error: Cannot Find Coin")
        return


dict_analyzer(file)