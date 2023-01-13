# 반복문 : loop 구문
# for, while

# while 문법
# while 조사식 (결과는 참/거짓) : 아래줄에는 참일 때 실행되는 구문
# 참일 떄 실행되는 구문 중에 조사식을 거짓으로 변경해야 함.

# 1~100 까지의 합
sum1 = 0
count1 = 0

# while 구문의 조사식은 관계/논리 연산이 올 수 있다.
while count1 < 101 : # 참일때 아래 구문을 실행한다.
    # sum = 1~100 의 합
    sum1 = sum1 + count1
    count1 = count1 + 1
# 중단점 적중 횟수 : 해당 줄을 실행한 횟수. 실행한 횟수가 설정한 값이 되면 멈춘다.

sum2 = 0
count2 = 0

while count2 <= 100 : # 참일때 아래 구문을 실행한다.
    # sum = 1~100 의 합
    sum2 = sum2 + count2
    count2 = count2 + 1
# 중단점 식 : 관계 연산자를 이용, 조건이 참일 때 멈춤

temp = 1