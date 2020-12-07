input5 = open("day_5/input_5.txt","r")


def take_half(inp,min1,max1,count):
    if min1+1 == max1:
        if inp[count] == "L" or inp[count] == "F":
            return min1
        if inp[count] == "R" or inp[count] == "B":
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
seatlist = []
for x in input5.read().split("\n"):
    rowx = take_half(x[0:7],0,127,0)
    colx = take_half(x[7:10],0,7,0)
    seatlist.append(rowx*8+colx)
n = sorted(seatlist)

for count,x in enumerate(n):
    try:
        if x + 2 == n[count+1]:
            print(x,n[count+1])
    except:
        pass