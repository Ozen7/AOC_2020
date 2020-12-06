input4 = open("day_4/input_4.txt","r").read()

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
    if input4[count:count+3] == "byr" and 1920 < int(input4[count+4: count +9]) < 2002:
        byr = True
    elif input4[count:count+3] == "iyr" and 2010 < int(input4[count+4: count +9]) < 2020:
        iyr = True
    elif input4[count:count+3] == "eyr" and 2020 < int(input4[count+4: count +9]) < 2030:
        eyr = True
    elif input4[count:count+3] == "hgt":
        spaceind = 0
        for let in range(count,len(input4)):
            if input4[let].isspace():
                spaceind = let
                break

        if input4[spaceind-1] == "m" and 150 < int(input4[count+4:spaceind-2]) < 193:
            hgt = True
        if input4[spaceind-1] == "n" and 59 < int(input4[count+4:spaceind-2]) < 76:
            hgt = True
    
    elif input4[count:count+3] == "hcl":
        if input4[count+4] == "#" and input4[count+11].isspace():

            for let in input4[count+5:count+11]:
                if let in ['a','b','c','d','e','f','0','1','2','3','4','5','6','7','8','9']:
                    continue
                else:
                    break
            else:
                hcl = True
    
    elif input4[count:count+3] == "ecl":
        if input4[count+4:count+7] in ['amb','blu','brn','gry','grn','hzl','oth']:
            ecl = True
    elif input4[count:count+3] == "pid":
        if input4[count+13].isspace() and input4[count+4:count+13].isnumeric():
            pid = True

    elif input4[count:count+2] == "\n\n":
        if iyr and ecl and hcl and hgt and eyr and pid and byr:
            numvalid += 1
            byr = False
            iyr = False
            eyr = False
            hgt = False
            hcl = False
            ecl = False
            pid = False
        else:
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
