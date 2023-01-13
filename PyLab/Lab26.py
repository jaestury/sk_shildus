# import, from 등은 가독성을 위해 코드의 가장 위에다가 올려 놓는 것이 좋다.
from Lab26m import MyClass
import Lab26m

arrayData = [111, 222, 333, 444, 555]
inputData = 300
cls = Lab26m.MyClass()
result = cls.compare(inputData, arrayData)

# 클래스는 인스턴스화 해야한다.
cls2 = MyClass()
result2 = cls2.compare(250, [100, 200, 300, 400, 500])
# 데이터를 다이렉트로 데이터를 넣어도 된다.

temp = 1
