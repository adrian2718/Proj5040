import sys
import numpy as np
from multiprocessing import Pool

gPrimesList = []


def calcprime(num):
    bIsPrime = True
    for prime in gPrimesList:
        if np.power(int(prime), 2) > cnt:
            break
        if num % prime == 0:
            bIsPrime = False
            break
        else:
            break
    if bIsPrime:
        gPrimesList += [str(num)]


numthreads = int(sys.argv[2])
p = Pool(numthreads)
maxint = int(sys.argv[1])
for cnt in range(2, maxint, numthreads):
    lnums = [x for x in range(cnt, np.min((cnt + numthreads, maxint + 1)))]
    while len(lnums) > 0:
        if len(gPrimesList) > 0:
            maxprime = gPrimesList[len(gPrimesList) - 1]
            largs = []
            while not lnums[i] > np.power(maxprime, 2):
                largs += [lnums[i]]
                del(lnums[i])
        else:
            largs = [lnums[0]]
            del(lnums[0])
        p.map(calcprime, largs)

print('\n'.join(gPrimesList))
