# for 구문 : 몇 번 반복할지 알 때 사용.
# for 구문은 while 구문으로 100% 변경 가능
# while 구문은 for 구문으로 전부 변경할수는 없음.

# 1~100 까지의 합
# for 구문안에서 사용할 변수 in range (몇 번 반복할지) :

sum1 = 0 
for i in range(101) : # for 구문은 0부터 시작한다. 조건이 거짓일 때 멈춤. 
    sum1 = sum1 + i

sum2 = 0 
for i in range(1, 101) :  # 앞에 숫자를 써서 범위를 지정해 줄 수 있다.
    sum2 = sum2 + i

sum3 = 0 
for i in range(1, 101, 1) :  # 1부터 시작. 시작점, 마지막점, 증가량(1씩 증가시킴)
    sum3 = sum3 + i

sum4 = 0 
for i in range(1, 101, 3) :  # 1부터 시작. 시작점, 마지막점, 증가량(3씩 증가시킴)
    sum4 = sum4 + i

temp = 1