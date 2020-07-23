# This is a LEAP YEAR program written in python programming language. 
def is_leap(year):
    leap = False

    if(year%100 == 0):
        y = year / 100
        if(y%4==0):
            leap = True

    elif(year%4 == 0):
        leap = True
    
    return leap

year = int (input())
print(is_leap(year))