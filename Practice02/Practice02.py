#02장 파이썬 프로그래밍의 기초, 자료형

####### Practice02-1 (숫자형)

# - 8진수 만들때는 숫자가 0O or 0o로 시작 ex) a = 0o177
# - 16진수 만들때는 숫자가 0x로 시작 ex) a = 0x8ff
a = 3
b = 4
print(a + b)
print(a ** b) #a의 b제곱

####### Practice02-2 (문자형 자료형)

# - 문자열 만들때 "Hello World", 'Hello World', """Hello World""", '''Hello World'''
food = "Python's favorite food is perl"
print(food)
food1 = '"Python favorite food is perl"' #큰따옴표 인식
print(food1)
food2 = "\"Python's favorite food is perl\""
print(food2)

#여러 줄 변수 대입
# - \n 삽입
# - ''' 사용
# - """ 사용

#문자열 연산
head = "py"
tail = "thon"
print(head + tail)
print(head * 3)
print("-" * 50)
print(head + tail)
print("-" * 50)

#문자열 길이 구하기
print(len(head))

#문자열 인덱싱과 슬라이싱 
#인덱싱 -> 가리킨다
a = "Life is too short, You need Python"
print(a[3]) #파이썬은 0부터 숫자를 센다
print(a[-1]) #뒤에서 첫번째
             #-(마이너스)는 뒤에서 부터 읽는다. -0이랑 0은 같다.

#슬라이싱 -> 한 문자만이 아니라 단어를 뽑아낸다.
b = a[0] + a[1] + a[2] + a[3]
print(b)
#슬라이싱 기법
print(a[0:4]) #a[시작번호:끝번호] 
              # - a[:17] 시작번호 생략시 처음부터 뽑아낸다
              # - a[:] 처음부터 끝까지 뽑아낸다

#pithon 을 python 으로 바꿔보자
a = "pithon"
print(a[:1] + 'y' + a[2:])
       
#문자열 포매팅
print("I eat %d apples" %3)
print("I eat %s apples" %"three")
print("I eat %d %s apples" %(3, "three"))
# %s (문자열), %c (문자1개), %d (정수), %f (부동소수), %o (8진수), %x (16진수), %% (Literal %, 문자 % 자체)
print("%10s" %"hi") #공백, 오른쪽 정렬
print("%-10s" %"hi") #왼쪽 정렬

print("%0.4f" % 3.123456789) #.은 소수점 푸인트 4는 소수점 뒤에 나올 숫자의 개수 (반올림)

#format 함수 사용
print("I eat {0} apples" . format(3))
print("I eat {0} apples" . format("three"))
print("I eat {0} {1} {count} apples" . format(3, "three", count="four"))

#왼쪽 정렬
print("'{0:<10}'" .format("hi")) #:<10 -> 치환되는 문자열을 왼쪽으로 정렬하고 총자릿수를 10으로 맞춘다.
#오른쪽 정렬
print("'{0:>10}'" .format("hi")) 
#가운데 정렬
print("'{0:^10}'" .format("hi")) 
#공백 채우기
print("'{0:=>10}'" .format("hi"))
print("'{0:*^10}'" .format("hi")) 

#소수점 표현
y = 3.12345678
print("{0:0.5f}" . format(y))
#{또는} 문자 표현
print("{{and}}" . format())
#f 문자열 포매팅
name = 'yj'
age = 24
print(f"나의 이름은 {name}, 나이는 {age}야")

d = {'nm' : 'yj', 'age' : 24}
print(f"내 이름은 {d['nm']} 이고 나이는 {d['age']}에오.")

print(f'{"hi":^10}') #정렬
y = 1.23456789
print(f'{y:0.4f}')
print(f'{{and}}')


#f, format 함수 써서 !!!python!!! 출력
print("{0:!^12}" .format("python"))
print(f'{"python":!^12}')

##### 문자열 관련 함수 #####
#count (문자 개수 반환)
a = "abcdefe"
print(a.count("e")) #a 문자열 중 e의 개수 반환

#find (위치 알려주기1)
print(a.find('d'))

#index (위치 알려주기2)
print(a.index('d'))

#join (문자열 삽입)
print("," .join('abcdefg'))
print("," .join(['a', 'b', 'c', 'd', 'e']))

#upper (소문자를 대문자로 바꾸기)
a = "github"
print(a.upper())

#lower (대문자를 소문자로 바꾸기)
a = "GITHUB"
print(a.lower())

#lstrip (왼쪽 공백 지우기)
a = "   github   "
print(a.lstrip())

#rstip (오른쪽 공백 지우기)
print(a.rstrip())

#strip (양쪽 공백 지우기)
print(a.strip())

#replace (문자열 바꾸기)
a = "hi hello"
print(a.replace("hi", "hello"))

#split (문자열 나누기)
a = "git hub study"
print(a.split())
b="g:i:t:hub"
print(b.split(':'))

####### Practice02-3 (리스트 자료형)
#리스트 -> []로 감싸주고 쉼표로 구분. 숫자, 문자열, 리스트 자체 등 어떠한 자료형도 포함가능
#리스트의 인덱싱
a = [1, 2, 3, 4, 5]
print(a[0]) #a[-1]은 리스트 a의 마지막 요솟값
print(a[2] ** a[1]) 

b = [1, 2, 3, [7, 8, 9]] 
print(b[3][0]) #이중 리스트 인덱스

#리스트의 슬라이싱
a = [1, 2, 3, 4, 5, 6, 7]
print(a[4:7])

A = [1, 2, 3, 4, 5]
print(A[1:3])

B = [1, 2, 3, [ 'a', 'p', 'l'], 4, 5, 6, 7]
print(B[0:6])
print(B[3][:3])

#리스트 더하기
a = [3, 6, 9]
b = [17, 1, 7]
print(a + b)

#리스트 반복하기
print(a * 2)

#리스트 길이 구하기
print(len(b))

#리스트에서 값 수정하기
c = [1, 2, 7]
c[1] = 6
print(c)

#del 함수 사용해 리스트 요소 삭제
a = [7, 3, 1]
del a[2]
print(a)

b = [2, 4, 6, 8]
del b[2:] #슬라이싱 기법으로 한꺼번에 삭제
print(b)

###리스트 관련 함수
#append (리스트에 요소 추가)
a = [1, 2, 3]
a.append(7) #리스트의 마지막에 7 추가
print(a)
a.append([8, 9])
print(a)

#sort (리스트 정렬)
b = [9, 7, 5, 3]
b.sort() #문자도 알파벳 순서로 정렬
print(b) 

#reverse (리스트 뒤집기)
c = ['b', 'n', 'a'] 
c.reverse() #역순
print(c)

#index (위치 반환)
d = [1, 3, 5, 7]
print(d.index(7))

#insert (리스트에 요소 삽입)
e = [5, 6, 7]
e.insert(0, 9) #e[0] 위치에 9 삽입
print(e)

#remove (리스트 요소 제거)
f = [3, 5, 7, 4, 5, 2]
f.remove(5) #첫번째로 나오는 5 삭제
print(f)

#pop (리스트 요소 끄집어내기)
g = [1, 7, 5, 3, 1, 0]
g.pop() #리스트의 맨 마지막 요소를 돌려주고 그 요소 삭제
print(g) 
g.pop(1) #리스트의 1번째 요소를 돌려주고 그 요소는 삭제 
print(g)

#count (리스트에 포함된 요소의 개수 세기)
g.count(1) #1이 몇 개 있는지 조사 후 개수를 돌려준다

#extend (리스트 확장) -> extend(x) x에는 리스트만 올 수 있다.
h = [7, 8, 9]
h.extend([10, 5])
print(h)

####### Practice02-4 (튜플 자료형)
#튜플은 리스트와 거의 비슷
# - 리스트는 []으로 둘러싸지만 튜플은 ()으로 둘러싼다.
# - 리스트는 그 값의 생성, 삭제, 수정이 가능하지만 튜플은 그 값을 바꿀 수 없다. 
# - 가장 큰 차이는 값을 변화시킬 수 있는지의 여부. 평균적으로는 값이 변경되는 형태의 변수가 많기 때문에 리스트 더 많이 사용.
#튜플의 형태
t1 = ()
t2 = (1,) #1개의 요소일때에는 반드시 요소뒤에 콤마(,)를 붙여야 한다.
t3 = (1, 2, 3)
t4 = 1, 2, 3 #괄호() 생략 무방
t5 = ('a', 'b', 'c', ('ab', 'cd'))

#튜플의 요솟값을 삭제하려 할 때 (에러)
#Traceback (most recent call last):
#File "<stdin>", line 1, in <module>
#TypeError: 'tuple' object doesn't support item deletion

#튜플 요솟값을 변경하려 할 때 (에러)
#Traceback (most recent call last):
#File "<stdin>", line 1, in <module>
#TypeError: 'tuple' object does not support item assignment

#튜플 인덱싱하기
t = (1, 2, 'a', 'b')
print(t[1])

#튜플 슬라이싱하기
tt = (7, 6, 'b', 'a')
print(tt[0:])

#튜플 더하기
print(t + tt)

#튜플 곱하기
print(t * 3)

#튜플 길이 구하기
print(len(tt))

#(1, 2, 3)이라는 튜플에 값 4를 추가하여 출력
ttt = (1, 2, 3)
print(ttt + (4,))


####### Practice02-5 (딕셔너리 자료형)
#대응 관계를 나타낼 수 있는 자료형 
#연관 배열(Associative array) 또는 해시(Hash)
#파이썬에서는 이러한 자료형을 딕셔너리 라고 한다. key, value 한 쌍으로 갖는 자료형 -> 순차적으로 모두 검색하는 것이 아니라 단어가 있는 곳만 펼쳐본다
#{Key1:Value1, Key2:Value2, Key3:Value3, …}

#딕셔너리 쌍 추가하기
a = {1: 'a'}
a[2] = 'b' #{2:'b'} 쌍추가
print(a)

a['name'] = 'apple'
print(a)
 
a['list'] = ['a', 'b', 'c']
print(a)

#딕셔너리 요소 삭제하기
del a[1] #key 가 1인 key;value 쌍 삭제
print(a)

#딕셔너리에서 key 사용해 value 얻기
print(a['list']) #딕셔너리 변수이름 [key]

#딕셔너리 만들 때 주의할 사항
# - key 는 고유한 값이므로 중복되면 하나를 제외한 나머지것들이 무시된다. 
# - key에 리스트는 쓸 수 없다. 튜플은 key로 쓸 수 있다. -> 리스트는 그 값이 변할 수 있기 때문에 key로 쓸 수 없다.
#value 에는 상관없이 아무 값이나 쓸 수 있다. 
#리스트를 key 로 쓸 때 (오류)
#Traceback (most recent call last):
#File "<stdin>", line 1, in <module>
#TypeError: unhashable type: 'list

###딕셔너리 관련 함수
#keys (key 리스트 만들기) 
#key 만을 모아서 dict_keys 객체를 돌려준다
a = {'apple' : 'red', 'banana' : 'yellow', 'abc' : 111}
print(a.keys()) #리스트를 사용하는 것과 차이가 없지만 append, insert, pop, remove, sort 함수 수행 불가

print(list(a.keys())) #dict_keys 객체를 리스트로 변환

#values (value 리스트 만들기)
print(a.values()) #dict_values 객체를 돌려준다

#items (key, value 쌍 얻기)
print(a.items()) #key와 value의 쌍을 튜플로 묶은 값을 dict_items객체로 돌려준다

#clear (key:value 쌍 모두 지우기)
print(a.clear())

#get (key로 value얻기)
b = {'name' : 'pen', 'mark' : 'down', 'a' : 111}
print(b.get('mark'))
print(b.get('nokey')) #none을 리턴
#print(b['nokey']) #오류가 난다
#딕셔너리 안에 찾으려는 key 값이 없을 경우 미리 정해둔 디폴트값을 대신 가져오게 하고 싶을때에 get(x, '디폴트값')을 사용하면 편리

#in (해당 key가 딕셔너리 안에 있는지 조사하기)
print('name' in b) #true
print('pen' in b) #false


####### Practice02-6 (집합 자료형)
#집합에 관련됫 것을 쉽게 처리
s1 = set([1, 2, 3]) #set 키워드를 사용해 만든다
print(s1)

s2 = set('apple')
print(s2)
#집합 자료형 특징
# - 중복을 허용하지 않는다.
# - 순서가 없다.
#리스트나 튜플은 순서가 있어 인덱싱을 통해 자료형의 값을 얻을 수 있다. 
#set 자료형은 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없다. (딕셔너리와 비슷)
#set 자료형에 저장된 값을 인덱싱으로 접근하려면 리스트나 튜플로 변환한 후 해야한다.
s3 = set([1, 2, 3, 4, 5])
l1 = list(s3)
print(l1)

#교집합, 합집합, 차집합
s4 = set([1, 2, 3, 4, 5, 6, 7])
s5 = set([6, 7, 8, 9])

print(s4 & s5) 
print(s4.intersection(s5)) #(&, intersection함수) 교집합 

print(s4 | s5)
print(s4.union(s5)) #(|, union함수) 합집합

print(s4 - s5)
print(s4.difference(s5)) #(-, difference) 차집합

###집합 자료형 관련 함수
#add (값 1개 추가하기)
s6 = set([1, 3, 5, 7])
s6.add(9)
print(s6)

#update (값 여러 개 추가하기)
s6.update([11, 13])
print(s6)

#remove (특정 값 제거하기)
s6.remove(5)
print(s6)


####### Practice02-7 (불 자료형)
#참, 거짓을 나타내는 자료형
a = True
b = False
print(type(a)) #type함수 -> 자료형 bool인것 확인
print(type(s6))

print(1 == 1) #true 값

#자료형의 참과 거짓
#문자열, 리스트, 튜플, 딕셔너리 등의 값이 비어있음녀 거짓
#숫자에서는 값이 0일때 거짓 


####### Practice02-8 (자료형의 값을 저장하는 공간, 변수)
#객체를 가리키는것,  "=" (assignment) 기호 사용
#c나 java에서는 변수를 만들 때 자료형을 직접 지정해야 한다. 파이썬은 변수에 저장된 값을 스스로 판단하여 자료형 지정

#리스트 복사
c1 = [7, 3, 1]
c2 = c1
print(c2)
print(id(c1))
print(id(c2)) #가리키는 대상이 동일하다는 것을 알 수 있다. 
print(c1 is c2) #true

c1[1] = 5
print(c2) #c1을 바꾸면 c2도 바뀌어 있는것 확인 (동일한 리스틀 가리키고 있다)

#[:] 사용(c4변수를 생성할 때 c3변수의 값을 가져오면서 다른 주소를 가리키도록 만드는 방법)
c3 = [6, 8, 7]
c4 = c3[:]
print(c4)
c3[1] = 67
print(c3, c4)

#copy 모듈 사용
from copy import copy
c5 = [2, 4, 6]
c6 = copy(c5) #위에 c4 = c3[:]와 동일
print(c6 is c5) #c6와 c5가 가리키는 객체는 서로 다르다


#변수를 만드는 여러가지 방법
a, b = ('python', 'study') #튜플로 a, b에 값 대입
print(a, b)
(a, b) = 'study', 'python'
print(a, b)

[a, b] = ['funny', 'python']
print([a, b])
a = b = 'python'
print(a, b)

a1 = 6
b1 = 7
a1, b1 = b1, a1 #a1, b1 값을 바꾸기
print(a1, b1)