"""
june 22 homework - Extra credit

Create a graph paper based on input from user. Close graph paper on all ends

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
            cw = columnWidth
            while cw > 0:
                print("-",end="")
                cw -= 1
            c -= 1
        print(end = "\n")
            
        rw = rowWidth
        while rw > 0:
            c = columns
            while c > 0:
                print("|",end="")
                cw = columnWidth
                while cw > 0:
                    print(" ",end="")
                    cw -= 1
                c -= 1
            rw -=1
            print(end = "\n")
        r -= 1
    return;

def printGraphWithEdges(rows, columns, rowWidth, columnWidth):
    r = rows
    while r > 0:
        c = columns
        while c > 0:
            print("+",end="")
            cw = columnWidth
            while cw > 0:
                print("-",end="")
                cw -= 1
            c -= 1
        print("+", end="")
        print(end = "\n")
            
        rw = rowWidth
        while rw > 0:
            c = columns
            while c > 0:
                print("|",end="")
                cw = columnWidth
                while cw > 0:
                    print(" ",end="")
                    cw -= 1
                c -= 1
            rw -=1
            print("|", end="")
            print(end = "\n")
        r -= 1
    #print bottom most edge
    c = columns
    while c > 0:
        print("+",end="")
        cw = columnWidth
        while cw > 0:
            print("-",end="")
            cw -= 1
        c -= 1
    print("+",end="")
    print(end = "\n")

    return;


print("\nThis is what your graph paper looks like:")
printGraph(rows, columns, rowWidth, columnWidth)
print("\n")

    
print("\nThis is what your graph paper looks like with edges:")
printGraphWithEdges(rows, columns, rowWidth, columnWidth)
print("\n")

sys.exit(0)


"""
Testing how to print on new line
print(rows)
print(columns)
print(rows,end="")
print(end="\n")
print(columns)
"""
        
        
        



sys.exit(0)
