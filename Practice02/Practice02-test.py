#######2단원 연습문제#######

#Q1
print((80+75+55) / 3)
#평균 구하기 문제

#Q2
print(13 % 2)
#2로 나눈 나머지가 1이므로 홀수

#Q3
pin = '881120-1068234'
yyyymmdd = pin[0:6]
num = pin[7:]
print(yyyymmdd)
print(num)

#Q4
print(num[0])

#Q5
a = 'a:b:c:d'
b = a.replace(':', '#')
print(b)

#Q6
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

#Q7 
#틀림
a = ['Life', 'is', 'too', 'short']
result = " ".join(a) 
print(result)

#Q8 
#틀림 튜플 추가할때 콤마 확인 !!!
a = (1, 2, 3)
a = a + (4, )
print(a)

#Q9
#오류 방생하는 경우 3번 , 리스트는 올 수 없다.(변하기 때문에)

#Q10
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a) 
print(result) 

#Q11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b) 

#Q12
#가리키는 객체가 같기 때문에 바뀐다. 