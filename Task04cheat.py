def addFood(index, value):
    itemTimes[index] = int(value)

# sub-function change food titles to numbers where can
def changeFoodToValue():
    for i in range(0,len(foods)):
        for j in range(2, len(foods[i])):
            for food in itemTimes:
                if foods[i][j] == food:
                    foods[i][j] = itemTimes[food]

# sub-function to find items with only times and add to dictionary
def findKnownTimes():
    i = 0
    while i < len(foods):
        allKnown = True
        for j in range(2, len(foods[i])):
            if isinstance(foods[i][j], int) == False:
                allKnown = False
        if allKnown == True:
            maxTime = int(foods[i][1]) + max(foods[i][2:])
            addFood(foods[i][0], maxTime)
            del foods[i]
        i += 1

# open table
file = open('04-preparation.txt', 'r', errors='ignore')
table1 = []
for row in file:
    table1.append(row.strip('\n'))

# create sub-lists from space separated table
foods = []
for item in table1:
    x = item.split()
    foods.append(x)
print("There are", len(foods),"foods to prepare.")

# adds up total cooking time
totalTime = 0
for item in foods:
    totalTime = totalTime + int(item[1])
print("To complete all tasks it takes", totalTime, "minutes.")

# creates a list for cooking finish times and removes known times from foods
itemTimes = {}
for turn in range(0,2): # do twice because list moves
    for item in foods:
        if len(item) == 2:
            addFood(item[0], item[1])
            foods.remove(item)

# find items that have no foods left in list
while len(foods)>0: # do until list empty
    changeFoodToValue()
    findKnownTimes()

# give longest time (and the food for it)
longestFood = max(itemTimes, key=itemTimes.get)
print('longest:',longestFood,'at',itemTimes[longestFood])





tasks={}
tasksTimes={}

def getTaskTime(task):
    dTime=0
    if task in tasksTimes:
        return tasksTimes[task]
    tasksTimes[task]=int(tasks[task][0])
    for dependsOn in tasks[task][1:]:
        dependsOnTime=getTaskTime(dependsOn)
        if dependsOnTime>dTime: dTime=dependsOnTime
    tasksTimes[task]+=dTime
    return  tasksTimes[task]

for l in open("04-preparation.txt"):
    taskAsList=l.strip().split()
    tasks[taskAsList[0]]=taskAsList[1:]

for task in tasks.keys():
    getTaskTime(task)

print(max(tasksTimes.values()))