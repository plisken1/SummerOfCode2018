#Part 1
def part1(fileName):
	seperator=", "
	mostFriends=0;
	#with open(fileName) as file:
	for line in open(fileName):
		myList = line.split(seperator)
		if (len(myList)>mostFriends):
			mostFriends=len(myList)
	return mostFriends

#Part 2
def part2(fileName):
	seperator=", "
	myList=[]
	specialList=[]
	with open(fileName) as file:
		for line in file:
			myList = myList +line.rstrip('\n').split(seperator) # Create big list
	for outer in range(0,len(myList)): #outer loop
		for inner in range(outer+1,len(myList)): #inner loop
			if (myList[outer]==myList[inner]): #We have a match
				if (not(myList[inner] in specialList)): #Is it already counted for?
					specialList.append(myList[inner]) #Add it if new
				break #Stop searching now, we got a match...
	return(len(specialList))

#part 2 refined
def part2a(fileName):
	seperator=", "
	myList=[]
	specialist=set()
	for line in open(fileName):
		myList=myList+line.rstrip('\n').split(seperator)
	for cnt, name in enumerate(myList):
		if (name in myList[cnt+1:]):
			specialist.add(myList[cnt])
	return (len(specialist))




print(part1("00-invites.txt"))
print(part2("00-invites.txt"))
print(part2a("00-invites.txt"))