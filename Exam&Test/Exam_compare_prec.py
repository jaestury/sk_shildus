# 연습 문제 
# 리스트의 데이터 111, 222, 666, 999, 6666
# 사용자 요청한 값을 선언 : 직접 값을 입력 (변수에 데이터 입력)
# 입력한 값을 비교 - 리스트에 있는 데이터와 비교
# 예시) 555를 비교할 경우 -> "222, 666 사이에 있다." 라고 변수에 저장함.
# 이걸 함수로 만들기
# if 사용하기. 반복문 사용하기. 

# def compare(data) : 
#     result = 0
#     if arrayList[0] < data : 
#         result = data + "은 " + arrayList[0] + "보다 크지만, " + arrayList[1] + "보다 작다."
#     elif arrayList[1] < data : 
#         result = data + "은 " + arrayList[1] + "보다 크지만, " + arrayList[2] + "보다 작다."
#     elif arrayList[2] < data : 
#         result = data + "은 " + arrayList[2] + "보다 크지만, " + arrayList[3] + "보다 작다."
#     elif arrayList[3] < data : 
#         result = data + "은 " + arrayList[3] + "보다 크지만, " + arrayList[4] + "보다 작다."
#     elif arrayList[4] < data : 
#         result = data + "은 " + arrayList[4] + "보다 크다."

#     return result

# 데이터가 입력되면 배열의 첫 요소부터 입력된 데이터와 비교한다. 비교하는 행위가 반복되기 때문에 반복문인 for 문을 사용.


# def arrayCompare(data) : 
#     arrayList = [111, 222, 666, 999, 6666]
#     result = 0
#     for i in range (len(arrayList)) : 
#         if data < arrayList[i] : 
#             result = data + "은 " + arrayList[i] + " 보다 작다."
#         elif arrayList[i] < data < arrayList[i] : 
#             result = data + "은 " + arrayList[i] + "보다 크지만, " + arrayList[i+1] + "보다 작다."
#         elif arrayList[i] < data : 
#             result = data + "은 " + arrayList[i] + "보다 크다."
#     return result

# data = 400

# result1 = arrayCompare(data)



# 



    