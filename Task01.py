#Part 1
def part1(fileName):
	cnt=0
	for line in (open(fileName)):
		if (not("#" in line)) and len(line)>1:
			cnt = cnt + 1
			print(cnt, " ",line)
	return cnt


def part2(fileName):
	startingDirection="E"
	currentDirection=startingDirection
	x=0
	y=0


	def calculate(instruction):
		if (instruction=="A"):
			if (currentDirection=="N"):
				currentDirection="W"
			if (currentDirection=="W"):
				currentDirection="S"
			if (currentDirection=="S"):
				currentDirection="E"
			if (currentDirection=="E"):
				currentDirection="N"









print(part1("01-mowmaster.txt"))