import random

times = []
for i in range(1000000):
    b = 0           ## tells us if we're done with the while loop
    n = 0           ## initialize number of flips
    a = ['','','']  ## initialize last three results of flips
    while(b == 0):  ## repeat until sequence occurs
        n += 1
        a[0] = a[1]
        a[1] = a[2]
        a[2] = random.randint(0,1)
        if a == [1,1,0]:
            b = 1
    times.append(n)
print float(sum(times))/float(len(times))
