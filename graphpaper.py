"""
june 22 homework
Create a graph paper based on input from user
"""

import sys

rows = int(input("How many rows of boxes? "))
columns = int(input("How many columns of boxes? "))
rowWidth = int(input("How many rows of spaces in each box? "))
columnWidth = int(input("How many columns of spaces in each box? "))

def printGraph(rows, columns, rowWidth, columnWidth):
    r = rows
    while r > 0:
        c = columns
        while c > 0:
            print("+",end="")
            print(columnWidth*"-",end="")
            c -= 1
        print()
            
        rw = rowWidth
        while rw > 0:
            c = columns
            while c > 0:
                print("|",end="")
                print(columnWidth*" ",end="")
                c -= 1
            rw -=1
            print()
        r -= 1

print("\nThis is what your graph paper looks like:")
printGraph(rows, columns, rowWidth, columnWidth)
print()

sys.exit(0)

