#list: mutable sequence of data elements (can be of different types)
aList =["item1",12,True,"item2" ]
print(type(aList))
print('aList:')
print(aList)

#last index
print('aList[-1]:' + aList[-1])

#list slicing
print('aList[:-2]:')
print(aList[:-2])

#filtering data with lambda
filteredList=list(filter(lambda x: x > 100, [-5, 200, 300, -10, 10, 1000]))
print('filteredList:')
print(filteredList)

#data transformation with map
transformedList = list(map(lambda x: x ** 2, [11, 22, 33, 44,55]))
print('transformedList:')
print(transformedList)

listFromRange=list(range(10))
print('listFromRange:')
print(listFromRange)

oddNum = list(range(3,29,2))
print('oddNum:')
print(oddNum)

# Time complexity:
# Insert O(1)
# Delete O(n)
# Slice O(n)
# Element retrieval: O(n)
# Copy O(n)



###################################
#tuples: immutable data structure
myTuple=('1','un',False)
print('myTuple:')
print(myTuple)
print(myTuple[1:])

#time complexity
#append: O(1)
