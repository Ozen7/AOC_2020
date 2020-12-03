from day2_input import input
listput = input.split("\n")
count = 0
for x in listput:
    split2 = x.split(" ")
    lett = split2[1][0]
    indexdash = x.index("-")
    num1 = int(split2[0][0:indexdash])-1
    num2 = int(split2[0][indexdash+1:])-1
    try: 
        if ((split2[2][num1] == lett) or (split2[2][num2] == lett)) and (not(split2[2][num1] == lett) or (not(split2[2][num2] == lett))):
            count+=1
    except:
        pass
print(count)


