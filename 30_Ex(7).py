# Default arguments...

import time

def count(start, end):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)                                  # So this will print 1 to 10 1 by 1 for every second.
print("DONE!")

count(0, 10)


# If we add a default argument, then it should be after/followed by non-default arguments.
# for example, 

import time

def count(end, start=0):                                # Here if we write def count(start, end):, it won't work.
    for x in range(start, end+1):
        print(x)
        time.sleep(1)                                  
print("DONE!")

count(10)
# count(30, 15)                                           # We begin on 15 and end on 30