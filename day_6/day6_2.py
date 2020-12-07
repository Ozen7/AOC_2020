input6 =  open("day_6/input_6.txt","r")
splitput = input6.read().split("\n\n")
total = 0
for x in splitput:
    y = x.split("\n")
    y = list(map(set, y))
    totalset = []
    for sett in y:
        totalset += sett
    totalset = set(totalset)
    for oneset in y:
        totalset = totalset.intersection(oneset)
    total+= len(totalset)
print(total)