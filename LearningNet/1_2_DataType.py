# 5강 sequence data type

# 순서있는 데이터 타입 (index, slicing) - list, tuple, character array, byte
# 순서없는 데이터 타입 (index, slicing X) - Set, Dictionary
# 변경 가능(mutable) 데이터 타입 - List, dictionary, set
# 변경 불가(immutable) 데이터 타입 - Tuple, character array, byte

# myList = [10, 3.14, True, "abc"]
# print(myList)
# print(type(myList))
#
# print(myList[0:3:1])
# print(myList[1:3:2])


myList = [10,20,30,40]
myList.append(50)

myList[0] = 100
print(myList)

myList.append(50)
print(myList)

myList = myList + [1,2,3]
print(myList)

myList = myList * 2
print(myList)

myList.remove(30)
print(myList)

myList.pop()
print(myList)

myList.pop(3)
print(myList)

del( myList[0])
print(myList)

n = myList.index(50)
print(n)

c = myList.count(50)
print(c)

length = len(myList)
print(length)

# 튜플 타입

myT = (10, 20, 30, 40)
print (myT)
print(type(myT))
print(myT[0])
#myT[0] = 100


# Packing, unpacking
a, b, c = 10, 20, 30
print(a, b, c)

a, b, c = (100,200,300) #ubpacking
print(a, b, c)

a = 100, 200, 300 #packing
print(a)


#   Dictionary type
myD = {10:"aa", 20:"bb", 30:"cc"}
print(myD)
print(type(myD))
print(myD[20])
print(myD.get(30, "default"))
print(myD.get(40, "default"))

myD = {10:"aa", 20:"bb", 30:"cc", 20:"BB"}
print(myD)

myD[10] = "AA"
myD[40] = 'dd'
print(myD)

myD.pop(30)
print(myD)

print(myD.keys())
print(myD.values())
print(myD.items())

test = [10, (20, 'aa')]
print (test[1])
print (test[1][1])

### Set type

#중복 없는 데이터, 순서 없고, 변경 가능함

mySet = {10, 20, 30, 20, 10}    # 중복 허용 안됨
#print(mySet[0])
mySet.add(1000)
print(mySet)

mySet2 = {20,100,500}

print (mySet & mySet2)  #교집합
print (mySet | mySet2)  #합집합
print(mySet - mySet2)   #차집합
print(mySet ^ mySet2)   #대상 차집합