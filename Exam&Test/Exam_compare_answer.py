# 요구사항 나열. 
# 1. 반복문 사용(while, for)
# 2. 리스트 데이터 비교
# 3. 출력 형식이 있다 : "XXX, XXX 사이에 있다."
# 리스트 형식 - 자릿수 확인 : len
# for : 몇 번 반복하는지 알고 있을 때 사용 / while : 몇 번 반복하는지 모를 때 사용. 
# 일반적으로 for을 사용하는 것이 조금 더 안전하다.
# 리스트 안에 데이터를 확인함 [] 비교 후 출력 형식.
# 111, 222, 666, 888, 9999, 6666 사이에 있으면 문제 없지만,
# 100, 7000 등의 경우는 어떻게 출력해야할까?

def compare(inputData) : 
    listData = [111, 222, 666, 888, 999, 6666] # 전역으로 데이터를 선언하는 것은 주의해야 한다.
    # 전역 데이터에 이상하게 접근할 수도 있기 때문. 변수는 될 수 있다면 지역변수로 선언하자. 
    # 전역 데이터 선언 : 공용으로 사용한다. 기준값. 매우 중요한 데이터 .... 

    # 출력해주고자 하는 것이 문자열 타입이라면 None을 사용하는 것이 좋다. 데이터가 들어갈 공간 확보.
    printType = None

    # 안에 있는 데이터 비교
    for i in range(len(listData)) : # 리스트 안의 데이터는 지금은 6개이지만, 추가되거나 감소할 수도 있다.
        # 111보다 작을 때와 6666보다 클 때보다는 어떻게 할 것인가?

        # inputData가 리스트 중 가장 작은 값보다 작을 때
        if inputData < listData[0] : 
            # % 사용해서 출력 형식 지정.
            printType = "%d보다 작다" %(listData[0]) # 출력 형식을 지정하고 끝내면 됨. 
            break
        
        # 리스트 안에 있는 값 사이에 있을 때
        elif inputData <= listData[i] : 
            printType = "%d, %d 사이에 있다." %(listData[i-1], listData[i])# 출력 형식을 지정하고 끝내면 됨. 
            break

        # 리스트 중 가장 큰 값보다 클 때
        # listData 중 마지막 값보다 커야하기 때문에 마지막 값을 호출하기 위해 len 사용. 
        # 뒤에 -1을 붙인 이유는 배열은 0부터 카운트가 시작되기 때문. 
        # elif inputData >= listData[len(listData) -1] : 

        # [-1]을 대신 사용할 수도 있다. -1로 배열의 마지막 요소를 호출할 수 있기 때문.   
        elif inputData >= listData[-1] : 
            printType = "%d, %d 사이에 있다." %(listData[-1], inputData)# 출력 형식을 지정하고 끝내면 됨. 
            break


    return printType

result = compare(7000)
temp = 1

print(result)