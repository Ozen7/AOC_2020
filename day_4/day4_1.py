input4 = open("day_4/input_4.txt","r").read()

print(input4)
numvalid = 0
byr = False
iyr = False
eyr = False
hgt = False
hcl = False
ecl = False
pid = False
new = 0
for count in range(0,len(input4)):
    if input4[count:count+3] == "byr":
        byr = True
    elif input4[count:count+3] == "iyr":
        iyr = True
    elif input4[count:count+3] == "eyr":
        eyr = True
    elif input4[count:count+3] == "hgt":
        hgt = True
    elif input4[count:count+3] == "hcl":
        hcl = True
    elif input4[count:count+3] == "ecl":
        ecl = True
    elif input4[count:count+3] == "pid":
        pid = True
    elif input4[count:count+2] == "\n\n":
        if iyr and ecl and hcl and hgt and eyr and pid and byr:
            numvalid += 1
            print(numvalid)
            byr = False
            iyr = False
            eyr = False
            hgt = False
            hcl = False
            ecl = False
            pid = False
        else:
            print("RESET")
            byr = False
            iyr = False
            eyr = False
            hgt = False
            hcl = False
            ecl = False
            pid = False
        new += 1
print(numvalid)
print(new)
print(len(input4.split("\n\n")))