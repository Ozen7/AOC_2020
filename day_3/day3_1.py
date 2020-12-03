with open("day_3/input3.txt","r") as input3:
    fixedinput = input3.read().split("\n")
fixedinput.remove("")
axis = 0
count = 0
print(fixedinput)
print(len(fixedinput[1]))
for x in fixedinput:
    if x[axis] == "#":
        count+=1
    axis+=3
    if axis >= 31:
        axis-=31
print(count)