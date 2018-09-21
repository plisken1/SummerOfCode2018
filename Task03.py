
#Task 3 part 1
def part1(fileName):

    cd="N" #Starting Direction, if it matters LOL
    x=0
    y=0
    cutting = False
    patches=0
    init=0
    max = 50
    grid = [[init for a in range(max)] for b in range(max)]
 
    l=0
    for line in (open(fileName, encoding="utf-8")):
        if (not("#" in line)) and len(line)>0:
            instruction=(line.rstrip('\n')) #just in case
            l=l+1
            print("Instruction - ",instruction)
            if ("D" in instruction):
                cutting=True
                if(grid[x][y]==0):
                    patches=patches+1
                    grid[x][y]=1

            if ("U" in instruction):
                cutting=False
                print(l, " UUUU", cutting)
            if ("A" in instruction): # Direction Change
                if (cd=="N"):
                    cd="W"
                elif (cd=="W"):
                    cd="S"
                elif (cd=="S"):
                    cd="E"
                elif (cd=="E"):
                    cd="N"
            if ("C" in instruction): # Direction Change
                if (cd=="N"):
                    cd="E"
                elif (cd=="W"):
                    cd="N"
                elif (cd=="S"):
                    cd="W"
                elif (cd=="E"):
                    cd="S"
            if ("F" in instruction):
                print("xxxxxx")
                move=int((instruction[1:])) #get amount to move
                if (cutting):
                    for moves in range(move-1):
                        if (cd=="N"):
                            y=y+1                            
                        if (cd=="E"):
                            x=x+1
                        if (cd=="S"):
                            y=y-1
                        if (cd=="W"):
                            x=x-1
                        if(grid[x][y]==0):
                            patches=patches+1
                            grid[x][y]=1
                           
                        
                else:
                    if (cd=="N"):
                        y=y+move
                    if (cd=="E"):
                        x=x+move
                    if (cd=="S"):
                        y=y-move
                    if (cd=="W"):
                        x=x-move

            print(x,",",y)
    for l in range(0,max):
        print("")
        for m in range(0,max):
            #print(l,",",m," - ",grid[l][m], end='')
            print(grid[l][m], end='')

 
    return patches

    
    

#print(part1("test.txt"))
print(part1("03-graffiti.txt"))




