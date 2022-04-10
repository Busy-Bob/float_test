from math import ceil
from decimal import *

getcontext().prec = 10000

f = open("./Project1/95.txt", "r")
for T in range(1, 10000):
    K = T - ceil(Decimal('0.95') * Decimal(T))
    if int(f.readline()) != K:
        print("Check failed!")
        exit()

f = open("./Project1/90.txt", "r")
for T in range(1, 10000):
    K = T - ceil(Decimal('0.90') * Decimal(T))
    if int(f.readline()) != K:
        print("Check failed!")
        exit()

print("Check Successed!")