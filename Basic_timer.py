import datetime
import time

x = 0
now = time.time()
TIME_TO_END = 10
timer = True


while timer:
    print(x)
    time.sleep(1)
    if time.time() - now > TIME_TO_END:
        x += 1
        print(x)
        print("Times Up!!")
        timer = False
    else:
        x += 1
        continue
