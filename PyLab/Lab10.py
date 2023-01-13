# 조사식 사용하기

data1 = 2000
data2 = 1010

# 문법
# if 조건식 (연산) => 결과 참/거짓 :
if data1 == data2 : # data1과 data2가 같은지? 참일 때
    result = True
    data1 = 20000
else : # 거짓일 때 처리하는 부분
    result = False
    data2 = 101010

# 2개 이상 연산
# 연산이 복잡할 때는 조사식을 사용하자
if (data1 == data2) and (data1 <= data2) : 
    result = True
    data3 = "or 은 둘 중 하나만 참이어도 만족"

else :
    result = False
    data3 = "and 는 둘 다 참이어야 만족"

temp = 1