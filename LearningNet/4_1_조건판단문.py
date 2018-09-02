#   흐름제어

a = 3

if a == 3 :
    print('3임...')
elif a == 0 :
    print('0이네')
elif a < 0 :
    print('작다')
else :
    print('나머지')

print('hello')

#n = int(input('정수 입력:'))
n = 2

print( '짝수' if (n % 2 == 0) else "홀수")

if (n % 2 == 0) :
    print ('짝수네')
else :
    print('홀수다')


# 4.2 반복문
i = 10

while i < 100 :
    print ('i = ', i)
    i += 10
    if (i == 30) :
        break
else:   # loop가 종료 될때만 실행됨.
    print ('else...?')


n = 1
sum = 0
while n <= 10:
    sum += n
    print (n, sum)
    n += 1



# for loop
s = 'abcdefg'
for x in s:
    print (x)

myList = [10, 20, 30, 40, 50]
myT = (10, 200, 400)
myS = {1, 3, 5, 6}
myD = {10:'aa', 20:'bb', 30:'cc'}
for k, v in myD.items() :  # 키와 값의 튜플로 전달.
    print (k, " = ", v)

stdData = [
    {'name': '홍길동', 'age' : 20},
    {'name': '고길동', 'age' : 50},
    {'name': '황길동', 'age' : 30}
]

for n in stdData :
    print ('이름 : %(name)s / 나이 : %(age)d' % n)

# range(초기값, 끝값, 증가치)

r = range(0, 10, 1)
print (list(r))

r = range(5)
print (list(r))

r = range(1, 10, 2)
print (list(r))

sum = 0
for n in range(1,11):
    sum += n
    if n == 3:
        continue
    print (n, " - ", sum)



# 축약 문법  - 내장 리스트

my = [ n % 2 for n in range(1, 6)]
print (my)

salary = [1000, 2000, 4000, 5000, 6000]
acutal = [n - n * 0.033 for n in salary]

print (acutal)

data = [n for n in range(1, 11) if n % 2 == 0]
print (data)

# 이름 나이 데이터를 n 할때까지 입력 받아 입력받은 데이터를 출력하는 프로그램을 작성하시요.
'''
record = []
cAnswer = ''
while cAnswer != 'n':
    name = input("이름:")
    age = int(input("나이:"))
    record.append({'name':name, 'age':age})
    cAnswer = input("계속 입력하시겠습니까?")

print('------------------------')
print('\t이름\t나이')
print('------------------------')

print (record)

for item in record:
    print("%(name)s \t %(age)d" % item)

'''

f = 10 // 3
print (f)