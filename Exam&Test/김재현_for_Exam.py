# 반복문 이용해서 정삼각형 찍기

# 1 ~ 30
# for 반복문 사용한 구문 1.
# while 반복문 사용한 구문 1. 
# bjkim@sirmd.net 으로 메일
# 파일 형식 = 이름_for_Exam.py
#          =  이름_while_Exam.py

n = 30
a = 0

for i in range(1, 31):
    print(" " * (n-i) + "*" * (i*2-1))

# 참고 : https://songsw.tistory.com/30