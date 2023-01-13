# 연습 문제
# 3개의 매개 변수 : 숫자 형식으로 전달 2개, 1개는 문자열
# 문자열 : + - * /
# 전달 받은 문장열 비교해서 사칙연산을 하도록 함.
# 결과 리턴받아, 변수 저장하는 프로그램 만들기 
# if 구문 활용.
# 문제 후 elif 배울 예정

def calculator(num1, num2, cal) : 
    result = 0
    if cal == "+" : 
        result = num1 + num2
    elif cal == "-" :
        result = num1 - num2
    elif cal == "*" : 
        result = num1 * num2
    elif cal == "/" : 
        result = num1 / num2
    return result

num1 = 35
num2 = 33
answer1 = calculator(num1, num2, "+")
answer2 = calculator(num1, num2, "-")
answer3 = calculator(num1, num2, "*")
answer4 = calculator(num1, num2, "/")

temp = 1

# 함수 정의하기
def fourOperation(inputData1, inputData2, type) :
    result = 0
    if type == "+" :
        result = inputData1 + inputData2
    if type == "-" :
        result = inputData1 - inputData2
    if type == "*" :
        result = inputData1 * inputData2
    if type == "/" :
        result = inputData1 / inputData2
    
    return result


# 조건을 만족을 못했을 때 다음 elif 문을 실행하게 된다.
# if 문과 다른 점은, if 문은 모든 if 문을 실행하지만, 
# elif 문의 경우 조건을 만족하는 경우 더 이상 실행하지 않고 조건문을 탈출한다.
def fourElseIf(inputData1, inputData2, type) :
    result = 0
    if type == "+" : 
        result = inputData1 + inputData2
    elif type == "-" : 
        result = inputData1 - inputData2
    elif type == "*" : 
        result = inputData1 * inputData2
    elif type == "/" : 
        result = inputData1 / inputData2

    return result

# 사칙연산
data1 = 200
data2 = 100

result1 = fourOperation(data1, data2, "+")
result2 = fourOperation(data1, data2, "-")
result3 = fourOperation(data1, data2, "*")
result4 = fourOperation(data1, data2, "/")

data3 = 444
data4 = 333

result5 = fourElseIf(data3, data4, "+")
result6 = fourElseIf(data3, data4, "-")
result7 = fourElseIf(data3, data4, "*")
result8 = fourElseIf(data3, data4, "/")
# 이런식으로 계속 코딩을 해야한다. 


     
