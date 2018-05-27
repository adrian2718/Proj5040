import textwrap
output = "This program will find all the prime prime factors that makes up the number of the numbers between 0 and what ever number you input"
print (textwrap.fill(output,120))
n = int(input())
def primes_func(num):
    tempList = [2]
    x = 3
    prime = True
    while x <= num:
        for eachNum in tempList:
            if (x/eachNum)%1 == 0:
                prime = False
                break
            else:
                prime = True
        if prime is True:
            tempList.append(x)
        prime = False
        x += 2
    return tempList

primes = primes_func(n)
output2 = ""
primeFactors = []
x = 2
while x <= n:
    tempVar = x
    for eachNum in primes:
        power = 0
        while True:
            tempVar /= eachNum
            if tempVar%1 == 0:
                power += 1
            else:
                tempVar *= eachNum
                if power != 0:
                    output2 += str("(%s^%s)"%(eachNum,power))
                break
            print("Echo")
        if tempVar == 1:
            break
    primeFactors.append("[%s|%s]"%(output2,x))
    output2 = ""
    x += 1
primeFactors.insert(0,"(Anything but 0)^0 |1")
primeFactors.insert(0,"0^(Anything but 0)|0")
print(primes)
print(textwrap.fill(str(primeFactors),120))
