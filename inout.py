

import sys

try:
    n = float(input("How many years from now do you expect to retire? Enter an integer: "))
except ValueError:
    print("Sorry, your response was not an integer. Let's assume 30 years")
    n = 30

try:
    m = float(input("How many years do you expect to live after retiring? Enter an integer: "))
except ValueError:
    print("Sorry, your response was not an integer. Let's assume 20 years")
    m = 20

try:
    w = float(input("How much money per year will you need to live in retirement? Enter a number (no symbols): "))
except ValueError:
    print("Sorry, your response was not numerical. Let's assume $80,000")
    w = 80000

try:
    r = float(input("What annualized rate of return do you expect to earn on your retirement savings? Anything under 10 (0% - 10%) is reasonable . "))/100
except ValueError:
    print("Sorry, your response was not numerical. Let's assume 8%")
    r = 0.08

try:
    s = float(input("How much money have you saved so far towards retirement? Enter a number (no symbols): "))
except ValueError:
    print("Sorry, your response was not numerical. Let's assume $50,000")
    s = 50000

"""
try:
    pmt = float(input("How much money/year do you plan to save towards retirement going forward? Enter a number (no symbols): "))
except ValueError:
    print("Sorry, your response was not numerical. Let's assume $18,000")
    pmt = 18000
"""
PV = 0
count = 0
while (count<m):
    PV += w /(1+r)**count
    count += 1

"""

FV=0
FV=s*(1+r)**n
counter = n
while (counter>0):
    FV += pmt*(1+r)**counter
    counter -= 1
"""

payment = (-s*r*(1+r)**n/((1+r)**n-1)+r/((1+r)**n-1)*PV)/(1+r)
    
    
    
print("\n\n\nResults:")
print("\nYou have $",s," in your retirement savings, expect to work for ",n," more years , live for ",m," years in retirement after, and expect a ",r*100,"% average annualized rate of return on your savings.", sep="")

print("\n\n\nAssuming annual compounding, you need to save $",round(payment,2), " each year starting now through retirement. \n\n",sep="")

sys.exit(0)


