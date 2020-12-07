input5 = open("day_5/input_5.txt","r")


def take_half(inp,min1,max1,count):
    if min1+1 == max1:
        if inp[count] == "L":
            return min1
        if inp[count] == "R":
            return max1
        return min1
    if inp[count] == "F" or inp[count] == "L":
        newmax = max1
        newmax = max1 - (max1-min1)//2 - 1
        return take_half(inp,min1,newmax,count+1)
    if inp[count] == "B" or inp[count] == "R":
        newmin = min1
        newmin = min1 + (max1-min1)//2 + 1 
        return take_half(inp,newmin,max1,count+1)


highestcol = -1
highestrow = -1
for x in input5.read().split("\n"):
    rowx = take_half(x[0:7],0,127,0)
    colx = take_half(x[7:10],0,7,0)

    if rowx >= highestrow:
        if highestrow == rowx and colx > highestcol:
            highestcol = colx
        elif highestrow == rowx and colx <= highestcol:
            continue
        highestrow = rowx
        highestcol = colx
        print(rowx,colx)
            

    

print(highestrow*8+highestcol)


