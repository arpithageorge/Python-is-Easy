
myUniqueList = []
myLeftovers = []

def addTomyUniqueListList(item):
    if item in myUniqueList:
        addTomyLeftovers(item)
        return False
    else:
        myUniqueList.append(item)
        return True

def addTomyLeftovers(item):
 	myLeftovers.append(item)

print(myUniqueList)
print(addTomyUniqueListList("Apple"))
print(myLeftovers)
print(myUniqueList)
print(addTomyUniqueListList("Apple"))
print(myUniqueList)
print(myLeftovers)
print(addTomyUniqueListList("Orange"))
print(myUniqueList)
print(myLeftovers)