# Task 3 part 1 & 2

cnt=0

def part2(fileName):
	cd = "N"  # Starting Direction, if it matters LOL
	x = 0
	y = 0 # NO NEED TO CHEAT WITH AN OFFSET
	cutting = False
	init = ' ' # Fill our grid with blanks
	mark='X' # Represents a bald patch
	max = 100 # max grid size
	global cnt

	def update(): # Remember where we've been and keep count
		global cnt
		if (grid[x][y] == init):
			grid[x][y] = mark
			cnt +=1

	grid = [[init for a in range(max)] for b in range(max)] # Set up our grid

	for line in (open(fileName, encoding="utf-8")):
		if (not ("#" in line)) and len(line) > 0:
			instruction = (line.rstrip('\n'))  # just in case
			print("Instruction - ", instruction, " current coord: ",x,",",y) # just for debugging
			if ("D" in instruction):
				cutting = True
				update() # Deal with a single cut

			if ("U" in instruction):
				cutting = False
			if ("A" in instruction):  # Direction Change
				if (cd == "N"):
					cd = "W"
				elif (cd == "W"):
					cd = "S"
				elif (cd == "S"):
					cd = "E"
				elif (cd == "E"):
					cd = "N"
			if ("C" in instruction):  # Direction Change
				if (cd == "N"):
					cd = "E"
				elif (cd == "W"):
					cd = "N"
				elif (cd == "S"):
					cd = "W"
				elif (cd == "E"):
					cd = "S"
			if ("F" in instruction):
				move = int((instruction[1:]))  # get amount to move
				if (cutting):
					for moves in range(move ):# NO NEED FOR -1 HERE LOL
						if (cd == "N"):
							y = y + 1
						if (cd == "E"):
							x = x + 1
						if (cd == "S"):
							y = y - 1
						if (cd == "W"):
							x = x - 1
						update() # Update on each single move
				else:
					if (cd == "N"):
						y = y + move
					if (cd == "E"):
						x = x + move
					if (cd == "S"):
						y = y - move
					if (cd == "W"):
						x = x - move
	#Print message
	for m in range(max-1,-1,-1): # A bit of fiddling was required here
		print("")
		for l in range(0, max):
			print(grid[l][m],end='')

	print()
	return cnt # For answer to part 1




#part2("test.txt")
print(part2("03-graffiti.txt"))

