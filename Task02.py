#!/usr/bin/env python3
#part 2
def part1and2(fileName):
    total=0
    with open(fileName) as f:
        for cnt, line in enumerate (f):
            line=line.rstrip('\n')
            if (line!="9999"):
                total=total+int(line)
            else:
                break
    return cnt," ",round(total/cnt)
    
    

print(part1and2("02-rainfall.txt"))
