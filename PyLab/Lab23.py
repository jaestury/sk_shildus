# 클래스: 함수의 묶음 - 함수가 많아서 그룹으로 관리하는 단위

# 함수 - 클래스 안에서는 이름이 메서드 변경
class MyClass:  # 첫 알파벳을 대문자로 표시
    # 클래스 안에 있기 때문에 메서드로 변경됨
    # 함수하고 다른 른 것은 유일하게 매개변수 self 먼저 입력
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


# 클래스 안에 있는 기능(메서드) 가져오는 것은 인스턴스를 하면 됨
# 인스턴스 한 결과 -> 객체 (클래스를 변수화 한 것)
# cls 객체를 통해 MyClass 클래스 기능 또는 전역변수 사용 가능
cls = MyClass()  # 인스턴스를 함 : 결과 cls 하는 객체를 생성

arrayData = [111, 222, 666, 888, 999, 6666]
result = cls.compare(7000, arrayData)
temp = 1
