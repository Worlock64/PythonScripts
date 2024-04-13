StrRates = "5.0,100,5.5,101,6.0,102,:L10;5.0,99,5.5,100,6.0,101,:L20"
rateSets = StrRates.split(";") 
wholeSet = []
lockedList =[" "]


print(rateSets)

for n in rateSets:
    setBreaK = n.split(",")
    wholeSet.append(setBreaK)
    lockedList.append(setBreaK.pop())
    print(setBreaK)
    print(lockedList)
 
print(wholeSet)


#def create_matrix(string, rows, cols):
