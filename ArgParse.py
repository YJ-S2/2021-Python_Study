##########argparse 사용법 정리

import argparse
import os #output director를 만드는 등의 역할을 위해 필요



#파서 만들기
parser = argparse.ArgumentParser(description='Argparse Tutorial') 
#원하는 description을 입력하여 parser객체 생성, description외에도 usage, default value 지정가능



##### [ArgumentParser 객체]
#prog - 프로그램의 이름 (기본값 : sys.argv[0])
#usage - 프로그램 사용법을 설명하는 문자열 (기본값: 파서에 추가된 인자로부터 만들어지는 값)
#description - 인자 도움말 전에 표시할 텍스트 (기본값: none)
#epilog - 인자 도움말 후에 표시할 텍스트 (기본값: none)
#parents - ArgumentParser 객체들의 리스트이고 이들의 인자들도 포함된다.
#fomatter_class - 도움말 출력을 사용자 정의하기 위한 클래스
#prefix_chars - 선택 인자 앞에 붙는 문자 집합 (기본값: <-<)
#fromfile_prefix_chars - 추가 인자를 읽어야 하는 파일 앞에 붙는 문자 집합 (기본값: none)
#argument_default - 인자의 전역 기본값 (기본값: none)
#conflict_handler - 충돌하는 선택 사항을 해결하기 위한 전략 (일반적으로 불필요함)
#add_help - 파서에 -h/--help 옵션을 추가 (기본값: True)
#allow_abbrev - 약어가 모호하지 않으면 긴 옵션을 축약할 수 있도록 한다 (기본값: True)
#exit_on_error - 에러가 발생했을 때 ArgumentParser가 에러 정보로 종료되는지를 결정 (기본값: True)



#<formatter_class>
#class argparse.RawDesciptionHelpFormatter     .1
#class argparse.RawTextHelpFormatter           .2
#class argparse.ArgumentDefaultsHelpFormatter  .3
#class argparse.MetavarTypeHelpFormatter       .4

#1, 2 -> 텍스트 설명이 표시되는 방법을 더 제어할 수 있도록 한다.
#1을 formatter_class= 로 전달하는것은 description과 epilog가 이미 올바르게 포맷되어 있어서
#줄바꿈 되어서는 안된다는 것을 가리킨다.

#2는 인자 설명을 포함하여 모든 종류의 도움말 텍스트에 있는 공백을 유지 , 여러개의 줄넘김은 하나로 치환 

#3은 기본값에 대한 정보를 각각의 인자 도움말 메시지에 자동으로 추가

#4는 각 인자값의 표시 이름으로 type 인자의 이름응 사용 





#인자 추가하기
#add_argument() method를 통해 원하는 만큼 인자 종류 추가 
#argument 이름, type 정의 -> 주어진 인자 파싱할 때 문자열 취급한다. 데이터 타입 지정하고 싶으면 type = 
parser.add_argument('--print-number', type = int, help = 'an integer for printing repeatably')



#인자 파싱하기
args = parser.parse_args() 
#parse_args() method 로 주어진 인자 파싱 
#parse_args() -> 명령행을 검사하고 각 인자를 적절한 형으로 변환한 다음 적절한 액션을 호출한다.





##### [add_argument() 메서드]
#name or flags - 옵션 문자열의 이름이나 리스트, ex)foo 또는 -f, --foo
#action - 명령행에서 이 인자가 발견될 때 수행할 액션의 기본형
#nargs - 소비되어야 하는 명령행 인자의 수 
#const - 일부 action 및 nargs를 선택할 때 필요한 상숫값
#default - 인자가 명령행에 없고 namespace 객체에 없으면 생성되는 값
#type - 명령행 인자가 변환되어야 할 형
#choices - 인자로 혀용되는 값의 컨테이너
#required - 명령행 옵션을 생략할 수 있는지 아닌지 (선택적일때만)
#help - 인자가 하는 일에 대한 간단한 설명
#metavar - 사용 메시지에 사용되는 인자의 이름
#dest - parse_args()가 반환하는 객체에 추가될 attribute의 이름



#help, -h 기본으로 내장되어 있는 옵션. 이 인자를 넣고 실행하면 사용법에 대한 도움말 출력
#python ArgParse.py -h
for i in range(args.print_number):
    print('print number {}'.format(i+1))

#인자의 이름 앞에 - 가 붙으면 optional 아니면 positional 인자로서 필수로 지정해야한다
parser.add_argument('--foo', '-f') #optional
parser.add_argument('bar') #positional

#default 값 지정
parser.add_argument('--foo', '-f', type = int, default = 5)

### [action의 종류 지정], 기본값은 store
#store -> 인자 이름 바로 뒤의 값을 해당 이나에 대입 시킨다
#store_const -> add_argument() 에서 미리 지정되어 있는 const=에 해당하는 값이 저장된다. const= 는 반드시 써주어야한다
#store_true, store_false -> 인자를 적으면 해당 인자에 true나 false가 저장
#append -> 값을 하나가 아닌 여러개를 저장하고 싶을때 쓴다. 여러번 호출하면 같이 주는 값이 계속 append된다
#append_const -> append와 비슷하지만 사전에 지정한 const값이 저장된다
#count -> 인자를 적은 횟수만큼 값이 올라간다 보통 verbose 옵션에 많이 쓴다
#help -> 도움말 메시지를 출력하게 하고 종료하여 코드는 실행시키지 않는다
#version -> version 인자에 사용가능 버전 정보 출력 후 종료



###attribute -, _ 구분
#변수명에 - 허용하지 않음. -가 들어갔다면 args.인자로 접근하기 위해 -를 _로 바꾼다


###dest 적용 위치 지정
#argument를 지정할 때 store나 action의 저장 또는 적용위치를 바꿔서 지정 
parser.add_argument('--foo', action='append', dest='foo_list')


###nargs 값 개수 지정 
#N -> N개의 값을 읽어들인다
#? -> 0개 또는 1개의 값을 읽어들인다.
#  - 인자와 값을 모두 적은경우 해당값 저장
#  - 인자만 적은 경우 const값이 저장
#  - 아무것도 적지 않았으면 default 값 저장
#* -> 0개 이상의 값을 전부 읽어들인다
#+ -> 1개 이상의 값을 전부 읽어 들인다 정규 표현식의 것과 매우 비슷
#argparse.REMAINDER 남은 값을 개수 상관없이 전부 읽어들인다



###choices 값범위 지정
#인자와 같이 주어지는 값의 범위를 제한하고 싶으면 choices 옵션을 쓰면 된다. 
#list등 iterable 객체(in 조건 검사를 할 수 있으면 된다) 가 들어갈 수 있다.
parser.add_argument('--foo', chioces = range(1, 5))



###metavar 이름 재지정
#help 에서 도움말 메시지를 생성할 때 표시되는 이름을 변경할 수 있다.
#직접 값을 참조하는 args.foo 같은 경우 기본 이름 또는 dest에 의해 재지정된 이름을 써야한다.