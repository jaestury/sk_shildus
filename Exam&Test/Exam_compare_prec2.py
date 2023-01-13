# 입력값과 리스트 값 비교하는 함수 만들기. 

# 함수 만들기.
def compare(inputData) : 

    # 배열 선언. 지역변수로 선언하는 것이 더 좋기 때문에 함수 안에 넣어준다.
    arrayList = [111, 222, 666, 888, 999, 6666] 

    # 문자열이 들어갈 메모리 공간 마련해두기.
    printType = None

    # 반복문 설계하기
    # input와 배열 안에 있는 값을 반복해서 비교해야하기 때문에 for 문으로 반복문을 설계한다.
    # 지금 List 안의 데이터는 6개 뿐이지만, 늘어나거나 줄어들 수 있기 때문에 
    # len(length) 를 사용해 리스트의 전체 길이 사용한다.
    for i in range(len(arrayList)) : 

        # 조건문 설계하기
        # 문자열 출력을 위해서 조건문을 설계하자. if 문 사용
        # input된 값이 배열의 가장 작은 값보다 작을때
        if inputData < arrayList[0] : 
            printType = "%d는 %d 보다 작다" %(inputData, arrayList[0])
        # 디버그로 확인해본 결과 잘 나온다.
        # break 로 조건을 만족할 시 반복문을 탈출해준다.
            break

        # input된 값이 배열의 값 사이에 있을 때
        elif inputData <= arrayList[i] :
            printType = "%d은 %d와 %d 사이에 있다." %(inputData, arrayList[i-1], arrayList[i])
            break

        # input된 값이 배열이 가장 큰 값보다 클 때
        # 배열의 가장 마지막 값을 사용해야한다. 방법은 두가지가 있다.
        # [-1] 사용해서 역순으로 1번을 사용한다.
        # listData[len(listData) -1] len 함수를 사용하기. -1을 한 이유는 배열은 0에서부터 세기 때문이다.
        elif inputData > arrayList[-1] : 
            printType = "%d은 %d보다 크다." %(inputData, arrayList[-1])
            break

    # printType 반환해주기
    return printType

# compare 함수를 사용하고, 입력값 넣어주기.
result = compare(300)