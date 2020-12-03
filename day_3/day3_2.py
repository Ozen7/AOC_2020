with open("day_3/input3.txt","r") as input3:
    fixedinput = input3.read().split("\n")
fixedinput.remove("")
axis = 0
count = 0
switch = False

for x in fixedinput:
    if switch:
        switch = False
        print("runs")
        continue
    if x[axis] == "#":
        count+=1
    print(count)
    print(x[axis])
    axis+=1
    if axis >= 31:
        axis-=31

    switch = True
print(count)
#D1,R1 = 81
#D1,R3 = 292
#D1,R5 = 89
#D1,R7 = 101
#D2,R1 = 37