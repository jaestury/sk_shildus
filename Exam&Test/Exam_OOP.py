# 사칙연산 & 리스트처리 
# 2개의 함수를 클래스로 만들어서 사용하는 코드로 만들기. 
# 클래스 이름 : MyClass, 객체 이름 : cls
# 클래스를 이용해서 메서드 2개 만들고, 메서드 호출하는 코드를 작성하자.
# 인스턴스 : 클래스를 객체화하는 작업. 인스턴스화 한 결과물이 객체이다.

class MyClass :
    def fourElseIf(self, inputData1, inputData2, type) :
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

    def compare(self, inputData, listData) :
        printType = None    
        for i in range( len(listData) ) :
            if inputData < listData[0] :
                printType = "0, %d 사이에 있다"%(listData[0])       
                break        
            elif inputData <= listData[i] :
                printType = "%d, %d 사이에 있다"%(listData[i-1], listData[i]) 
                break
            elif inputData >= listData[len(listData) -1] :
                printType = "%d, %d 사이에 있다"%(listData[len(listData) -1], inputData) 
                break 
        return printType

cls = MyClass()

arrayData = [111, 222, 666, 888, 999, 6666]
result = cls.compare(7000, arrayData)

result2 = cls.fourElseIf(81, 99, "+")


temp = 1
