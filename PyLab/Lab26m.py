class MyClass:
    # 전역 변수 : 필드
    # 함수와 메서드 차이는 매개변수 self
    # self : 클래스 안에서 메서드나 필드를 가리킬 때 사용.
    # 나를 호출해 달라는 의미로 self 를 사용.
    def compare(self, inputData, listData):
        printType = None
        for i in range(len(listData)):
            if inputData < listData[0]:
                printType = "0, %d 사이에 있다" % (listData[0])  # 출력 형식 지정하고
                break
            elif inputData <= listData[i]:
                printType = "%d, %d 사이에 있다" % (
                    listData[i-1], listData[i])  # 출력 형식 지정하고
                break
            elif inputData >= listData[len(listData) - 1]:
                printType = "%d, %d 사이에 있다" % (
                    listData[len(listData) - 1], inputData)  # 출력 형식 지정하고
                break
        return printType
