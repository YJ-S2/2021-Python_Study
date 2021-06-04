#03장 프로그램의 구조를 쌓는다! 제어문

####### Practice03-1 (if문)
#if문의 기본 구조
#if 조건문:
#   수행할 문장 
#else:
#   수행할 문장

#조건문이란 참과 거짓을 판단하는 문장

#연산자 x or y -> 둘중에 하나만 참이면 참이다
#      x and y -> x와 y모두 참이어야 참이다
#        not x -> x가 거짓이면 참이다

#x in s , x not in s   . . .  in ~안에
#x in 리스트, 튜플, 문자열
#x not in 리스트, 튜플, 문자열
print('a' in ('a', 'p', 'l'))
print('e' not in ('a', 'p', 'l', 'e'))

pocket = ['card','money', 'phone', 'lipstick']
if 'card' in pocket:
    print("버스를 타고 가라")
else:
    print("걸어가라")

#다양한 조건 판단 elif , else if 같은 느낌인듯.

#조건부 표현식
score = 70
if score >= 60:
    message = "success"
else:
    message = "failure"

message = "success" if score >= 60 else "failure"
#조건문이 참인경우 if 조건문 else 조건문이 거짓인 경우 (가독성)


####### Practice03-2 (while문)
#while 조건문:    #참인 동안에 while 문 아래의 문장이 반복해서 수행된다.
#    수행할 문장
#while 문 나갈때 -> break
#while 문 맨 처음으로 돌아가기 -> continue
#무한루프 while True: -> ctrl + c 누르면 빠져나감



####### Practice03-3 (for문)
