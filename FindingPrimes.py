primes = [2]
print ("This program will find all of the prime factors inbetween 0 and to what ever number you input")
n = int(input())
x = 3
prime = True
while x <= n:
    for eachNumber in primes:
        temp = x/eachNumber
        if temp%1 == 0:
            prime = False
            break
        else:
            prime = True
    if prime is True:
        primes.append(x)
    x += 2
primes.insert(0,1)
print(primes)
