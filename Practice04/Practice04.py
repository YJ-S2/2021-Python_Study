#04장 프로그램의 입력과 출력은 어떻게 해야 할까?

####### Practice04-1 (함수)

#파이썬 함수의 구조 
#def 함수 이름(매개변수):
#  수행할 문장 
def add (a, b):  #a, b -> 매개변수
    return a + b      #result = a + b   return result
a = 3
b = 4
c = add(a, b)  #3, 4는 인수
print(c)

#입력값이 없는 함수
def say():
    return 'hi'

print(say())

#결괏값이 없는 함수
def addPrint(a, b):
    print("%d, %d의 합은 %d 입니다." % (a , b , a + b)) #결괏값은 리턴으로만 
addPrint(3, 4)   

#입력값도 결괏값도 없는 함수
def sayPrint():
    print('hello')  #입력 인수를 받는 매개변수도 없고 return 문도 없다.

sayPrint()

#매개변수 지정해 호출
addResult = add(a = 3, b = 7)
print(addResult)

#여러개의 입력값을 받는 함수 만들기
def add_many(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

c = add_many(1, 2, 3)
print(c)

def add_mul(choice, *args):
    if choice == 'add':
        res = 0
        for i in args:
            res = res + i
    elif choice == 'mul':
        res = 1
        for i in args:
            res = res * i
    return res

print(add_mul('add', 1, 2, 3, 4, 5))
print(add_mul('mul', 1, 2, 3, 4, 5))

#키워드 파라미터
def print_kwargs(**kwargs): #매개변수 이름앞에 **을 붙이면 kwargs는 딕셔너리가 되고 모든 key = value 형태의 결괏값이 딕셔너리에 저장
    print(kwargs)

print_kwargs(a = 1)
print_kwargs(name = 'foo', age = 3)

def add_and_mul(a, b):
    return a+b, a*b  #결괏값 튜플
 
print(add_and_mul(3, 4)) 

def say_nick(nick):
    if nick == '바보':
        return #입력값으로 '바보'라는 값이 들어오면 문자열을 출력하지 않고 함수를 즉시 빠져나간다.
    print('나의 별명은 %s 입니다' %nick) 
say_nick('무야호')
say_nick('바보')

#매개변수에 초깃값 미리 설정하기
def say_myself(name, old, man=True): #man = TRUE -> 초깃값 설정  true면 남자 false면 여자
    print("나의 이름은 %s 입니다." %name)
    print("나이는 %d 살 입니다." %old)

    if man: #초기화 시키고 싶은 매개변수를 항상 뒤쪽에 놓기.
        print("남자입니다")
    else :
        print("여자입니다.")

say_myself("kyj", 11)
say_myself("kyj", 11, False)

#함수 안에서 선언한 변수의 효력 범위
#함수 안에서 선언한 매개변수는 함수 안에서만 사용될 뿐 함수 밖에서는 사용되지 않는다

#함수 안에서 함수 밖의 변수를 변경하는 방법
# 1. return 사용하기 
a = 1
def vartest1(a):
    a = a + 1
    return a
a = vartest1(a) #물론 vartest함수 안의 a 매개변수는 함수 밖의 a와는 다른것이다.
print(a)

# 2. global 명령어 사용하기
a = 1
def vartest2():
    global a  #global 명령어는 사용하지 않는것이 좋다 -> 함수는 독립적으로 존재하는 것이 좋기 때문에.
    a = a + 1
vartest2()
print(a)

#lambda
#함수를 생성할 때 사용하는 예약어로 def와 동일한 역할을 한다.
#보통 함수를 한줄로 간결하게 만들 때 사용한다. 
#lambda 매개변수1, 매개변수2,  . . .: 매개변수를 사용한 표현식
addLambda = lambda a, b: a+b
resultLambda = addLambda(3, 4)
print(resultLambda)


####### Practice04-2 (사용자 입력과 출력)
#사용자 입력 -> input
number = input("숫자를 입력하세요")

#출력 -> print
#큰따옴표로 둘러싸인 문자열은 + 연산과 동일
#문자열 띄어쓰기는 콤마
print("life", "is", "too short")

#한 줄에 결괏값 출력하기
for i in range(10):
    print(i, end = '   ')
print('')

####### Practice04-3 (파일 읽고 쓰기)

#파일 생성하기
#f = open('새 파일.txt' , 'w')
#f.close() #파일 객체 닫아주는 역할
#파일 객체 = open(파일 이름, 파일 열기 모드) 
# r -> 읽기모드 w -> 쓰기모드 a -> 추가모드 - 파일의 마지막에 새로운 내용 추가

f = open("C:/Users/Admin/Desktop/Python_Study/새파일.txt" , 'w')
for i in range(1, 11):
    data = "%d 번째 줄입니다.\n" %i
    f.write(data)
f.close()

#프로그램의 외부에 저장된 파일을 읽는 여러가지 방법
#readline 함수 사용하기
f = open("C:/Users/Admin/Desktop/Python_Study/새파일.txt", 'r')
line = f.readline() # 파일의 첫번째 줄을 읽어 출력하는 경우
print(line)
f.close()

f = open("C:/Users/Admin/Desktop/Python_Study/새파일.txt", 'r')
while True:
    line  = f.readline()
    if not line: break #만약 더이상 읽을 줄이 없으면 break수행
    print(line)
f.close()


#readlines 함수 사용하기
f = open("C:/Users/Admin/Desktop/Python_Study/새파일.txt", 'r')
lines = f.readlines() # 파일의 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트로 돌려준다.
for line in lines:
    print(line)
f.close()

#read 함수 사용하기
f = open("C:/Users/Admin/Desktop/Python_Study/새파일.txt", 'r')
data = f.read() #파일의 내용 전체를 문자열로 돌려준다.
print(data)
f.close()

#파일에 새로운 내용 추가하기 -> 'a'모드

