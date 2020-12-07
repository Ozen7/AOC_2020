input6 =  open("day_6/input_6.txt","r")
splitput = input6.read().split("\n\n")
total = 0
for x in splitput:
    y = set(x.replace("\n",""))
    total += len(y)
print(total)