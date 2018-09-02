#######################
# 산술연산자
a = 10 + 2
b = 10 - 2
c = 10 * 2
d = 10 / 2  # 정수 / 정수 -> 실수
e = 10 ** 2
f = 10 // 2
g = 10 % 3

print (a, b, c, d, e, f, g)

# **
# * / // %
# + /
# 결합도 : 좌 -> 우

a = 10 + 2 - 3 * 2 ** 2
print(a)

# 반지름이 5인 원의 면적을 구하세요
cir = 5**2 * 3.14
print( "원의 면적 = ", cir)
#s = int(input ("input = "))
s = 10
print(s)
print(type(s))

cir = s ** 2 * 3.14
print("입력한 반지름24", s, "인 원의 면적 = ", cir)

# 대입 연산자
a = 10
a **= 2
print(a)
# 전치/후치 연산자 지원 안함 : a++, ++a
++a
print(a)

#######################
# 관계 논리 연산자

a = -3
b = a >= 0 and a != -3
print(b)

a = 1
b = 0 < a < 10
print ("a is bigger then 0 and less then 10 ?", b)

#######################
# 비트 및 구성원 연산자 - 비트 단위 연산 수행

a = 2 & 1
print(a)

a = 2 | 1
print (a)

a = -2 & 1  # -가 붙으면 2의 보수를 취한다
print(a)

a = 2 << 1
print(a)

a = -2 >> 1
print(a)

# 구성원 연산자
s = "abcdefg hello"
print ("Is hello is in string???", "hello" in s)

myList = [10, 20, 30, 40, 50]
print (1 not in myList)

myD = {10:'aa', 20:'bb', 30:"cc"}
print ('aa' in myD)
print (20 in myD)

a = 10
b = 10
print (a is b)
print (id(a), id(b))

b = 100
print (a is b)
print (id(a), id(b))

b = 10
print (a is b)
print (id(a), id(b))

myList = [10, 20, 30, 40]
myList2 = myList

print (myList is myList2)
print (id(myList), id(myList2))

myList2 = myList.copy()
print (myList is myList2)
print (id(myList), id(myList2))

