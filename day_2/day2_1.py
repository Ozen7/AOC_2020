listput = []
with open("day_2\day2_input.txt","r") as input:
    for x in input:
        listput.append(x.strip())
print(listput)
count = 0
for x in listput:
    split2 = x.split(" ")
    lett = split2[1][0]
    numsplit = split2[2].count(lett)
    indexdash = x.index("-")
    num1 = int(split2[0][0:indexdash])
    num2 = int(split2[0][indexdash+1:])
    if numsplit >= num1 and numsplit <= num2:
        count+=1
print(count)
