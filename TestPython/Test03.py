##########인자 두개를 받아야 실행되는 코드
#내가 짠 코드
import sys
def sub(a):
    print(a)
 
if __name__ == "__main__":    
    args = sys.argv[1:]
    for i in args:
        if(len(args) == 2):
            sub(i)
        else:
            print("FAIL")
            break


#파이썬이 좀 더 드러나는 코드
import sys
def sub(a, b):
    print(a, b)
    
if __name__ == "__main__":    
        if len(sys.argv) is 3:
            sub(sys.argv[1], sys.argv[2])
        else:
            print("FAIL")
            sys.exit(1)    