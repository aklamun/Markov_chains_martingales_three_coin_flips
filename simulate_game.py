import random

wins = []
for i in range(1000000):
    b = 0           ## tells us if we're done with the while loop
    a = ['','','']  ## initialize last three results of flips
    while(b == 0):  ## repeat until sequence occurs
        a[0] = a[1]
        a[1] = a[2]
        a[2] = random.randint(0,1)
        if a == [1,1,0]:
            b = 1
            wins.append(1)
        if a == [1,0,1]:
            b = 1
            wins.append(0)
print float(sum(wins))/float(len(wins))
