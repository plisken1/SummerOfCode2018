#Part 1
def part1(fileName):
	cnt=0
	for line in (open(fileName)):
		if (not("#" in line)) and len(line)>0:
			cnt = cnt + 1
	return cnt


#Part 2
def part2(fileName,startFacing):
    cd=startFacing #current direction.
    x=0
    y=0
    for line in (open(fileName)):
        if (not("#" in line)) and len(line)>0:
            instruction=(line.rstrip('\n')) #just in case
            if ("A" in instruction): # Direction Change
                if (cd=="N"):
                    cd="W"
                elif (cd=="W"):
                    cd="S"
                elif (cd=="S"):
                    cd="E"
                elif (cd=="E"):
                    cd="N"
            elif ("C" in instruction): # Direction Change
                if (cd=="N"):
                    cd="E"
                elif (cd=="W"):
                    cd="N"
                elif (cd=="S"):
                    cd="W"
                elif (cd=="E"):
                    cd="S"
            elif ("F" in instruction):                
                move=int((instruction[1:])) #get amount to move
                if (cd=="N"):
                    y=y+move
                if (cd=="E"):
                    x=x+move
                if (cd=="S"):
                    y=y-move
                if (cd=="W"):
                    x=x-move
    #print("current Direction =",cd," x =",x," y =",y) # Current State
    #Calculate distance to return
    if (x<0):
        x=(x*-1)
    if (y<0):
        y=(y*-1)
    return (x+y)
    





#print("starting Direction -",startingDirection)
#print("current Direction -",currentDirection)
print(part1("01-mowmaster.txt"))
print(part2("01-mowmaster.txt","E"))
