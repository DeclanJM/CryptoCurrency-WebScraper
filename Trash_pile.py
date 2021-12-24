"""
                            NONE OF THIS WORKS  ;)
                            ERRORS DO NOT MATTER IN HERE
"""


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
        
"""

file = "dict_test_dict.csv"


def read_csv(file):
    lst = []
    dct = {}
    with open(file, "r") as f:
        csv_reader = csv.reader(f)
        for line in csv_reader:
            if len(line) > 1:
                lst.append(line)
        for line in lst:
            dct[line[0]] = line[1]
    return dct
    return lst

d_file = read_csv(file)
#for val in dct.values():
    #print(val)
print(d_file[0])
#print(dct["Bitcoin"])
"""