#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
import math

number = 600851475143
odds = []
factors = []

for i in range(3,10001): #lucky start. If 6857 was not the correct answer, I would increase this accordingly within my CPU's power.
    if i % 2 == 1:
        odds.append(i)

for k in odds:
    if number % k == 0:
        factors.append(k)

print(max(factors))