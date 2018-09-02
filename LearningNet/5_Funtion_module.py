# 함수 작성/ 모듈 만들기/ 패키지 만들기

# 함수 다루기
def hello():
    print('hello')
    print('fn')


hello()
hello()


def fn1():
    return 10, 20, 30

a, b, c = fn1()
print(a, b, c)

# 명시적 인자 호출

def fn2(a, c):
    print(a, b)

fn2(100, 200)
fn2(c=2000, a=200)

n = 10
m = 20
print(n, m, sep='/')

print('hello', end='\t')
print('hi')

# 디폴트 인자

def fn3(a=10, b=20, c=30):
    print(a, b, c)

fn3()
fn3(b=100)

# 가변 인자 & 정의되지 않은 인자

def fn4(*args):
    for x in args:
        print (x, end='/')

fn4(10, 30, 40)


def fn5(**args):
    print(args)

fn5(a=1,b=2,c=3)



# 메모리 구조와 LGB규칙

g = 10

def fn(a):
    global g
    g = 100
    print('local g=', g)

fn(g)
print( 'g=', g)

