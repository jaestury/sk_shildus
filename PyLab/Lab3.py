intData = 100
# 형을 변환해서 데이터를 저장. 정수일 경우 소수점 아래의 값을 버림
intData = int(99.99) # 값으로 99가 출력된다.

intData2 = 99.99 # 자동으로 형을 지정해서 저장. 소수점 아래 값이 있기 때문에 Float로 지정된다.
# 파이썬은 실행될 때 데이터의 형이 지정됨

# float 형식으로 형을 변환 = 문자열 -> 소숫점
floatData = float("99.99")
floatData = float(99.99)

# 파이썬의 경우 데이터 무한대 저장 : inf

# 참 거짓 저장
boolData1 = bool(0) # False : 0만 거짓을 표현
# 나머지 숫자는 모두 True
boolData2 = bool(-1) # True

# Null 형식
nullData1 = None

# Null 형식인 확인 후 맞으면 True 저장하는 방법 : is
boolData =  nullData1 is None

debugCheck = 1 # 디버깅 확인용 임시 선언 변수

# 디버그
# 중단점을 찍어놓지 않으면 디버그를 해도 아무 일도 일어나지 않고 끝나버린다. 
# 중단점 설정, 해제
# 원하는 곳에 중단점을 찍어줘야 디버깅이 멈춘다. 
# 한 단계씩 코드 실행(F11)을 사용해서 한 줄 씩 코드를 실행하며 코드 실행 결과를 파악하고, 흐름을 파악해보자.