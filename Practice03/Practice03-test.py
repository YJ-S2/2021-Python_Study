#######3단원 연습문제#######

#Q1
#shirt

#Q2
result = 0
i = 1

while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1
print(result) 

#Q3
i = 0
while True:
    i += 1
    if i > 5: break
    print("*" * i) # * i 표현 ! 확인 !

#Q4
for i in range(1, 101): #range 표현 확인 !
    print(i)

#Q5
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A:
    total += score
average = total / 10 #10 -> len(A)
print (average) 

#Q6 #리스트 내포 표현 다시 공부하기
numbers = [1, 2, 3, 4, 5]
result = [n * 2 for n in numbers if n % 2 == 1]
print(result)