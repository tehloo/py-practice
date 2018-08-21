s = 'abcd efgh ijklm'
print (s)

# 공백을 기준으로 자르시오
t = s.split(' ')
print (t)

# 'efgh' 문자열을 추출하시오
print(t[1])

# 'ac fhikm' 문자열을 추출하시오
print(s[0:15:2])

# 'mlkji' 문자열을 추출하시오
print(s[-1:-6:-1])


# 문자열 객체 변수명이 s인 임의의 하나의 문자열이 주어진 경우, 공백 기준으로 자른뒤 맨 마지막 문자열을 추출하도록 프로그램을 작성하시오
s = 'abc def ghi'
t = s.split(' ')
print(t[len(t) - 1])

#$ = 10
_ = 20
한글 = 30

print(_, 한글)

str = "abcdefg"
print( str[2:3])
