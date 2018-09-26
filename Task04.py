#Part 1
def part1(fileName):
	time=0
	with open(fileName,encoding="utf-8") as file:
		for line in file:
			myList = line.split()
			time=time+int(myList[1])
	return time

#Part 2
#incomplete, not working, neds complete rewrite, see Task04cheat
time=0
myList=list()
completed=set()
pending=set()
myDict={}
prerequisites={}
totalTime=0

def update(aList):
	taskToBeUpdated=aList[0]
	total=int(aList[1])
	print("initial value:",total)
	for c in range(2, len(aList)):
		total = total + (myDict[aList[c]])
	print("new total:",total)
	return total

def getLowest():
	anotherList=list()
	for k in myDict:
		print(myDict[k])
		anotherList.append(myDict[k])
	anotherList.sort()
	print(anotherList)

def part2(fileName):

	with open(fileName,encoding="utf-8") as file:
		for line in file:
			splitLine=line.split()
			myList.append(splitLine)
			myDict[splitLine[0]]=int(splitLine[1])

	print(myList)
	for x in myList:
		if len(x)<3:
			completed.add(x[0])
		else:
			for y in range(2,len(x)):
				pending.add(x[y])



	print("initial sort")
	print("completed ", completed)
	print("pending ", pending)
	print()
	cnt=0
	while len(pending)>0 and cnt<len(pending):
		cnt=cnt+1
		pendingCopy=set(pending)
		for x in pendingCopy:
			if x in completed:
				pending.remove(x)

	print("second type sort")
	print("completed ", completed)
	print("pending ", pending)
	cnt=0
	while len(pending) > 0 and cnt < len(pending):
		cnt=cnt+1
		for z in myList:
			subList=list()
			if (z[0] in pending):
				for b in range(2, len(z)):
					subList.append(z[b])
				if(set(subList).issubset(completed)):
					pending.remove(z[0])
					completed.add(z[0])
					print(cnt," modding: ",z[0])
					myDict[z[0]]=update(z)

	print("third sort")
	print("completed ",completed)
	print("pending ",pending)
	print(myDict)
	getLowest()















#print(part1("04-preparation.txt"))
#print(part1("test.txt"))
part2("test.txt")
#part2("04-preparation.txt")