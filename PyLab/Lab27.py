import Lab26m


def callLab26m():
    # 인스턴스화
    cls = Lab26m.MyClass()
    result = cls.compare(99, [50, 100, 200, 300])

# 프로그램 실행.
# 스크립트 방식의 실행 : 한줄 한줄 순차적으로 위에서부터 실행한다.
# 함수를 만나면 이름만 확인 후 함수 안에 내용은 호출할 때 실행된다.
# Python 은 모듈을 가져올 경우 import 안에 함수 또는 메서드 이름을 확인한다.
# 특수한 모듈과 기능을 실행
# 특수한 것을 표시할 때는 __(언더바 두개)를 이용해서 표시함.

# __name__ 특수한 기능 또는 변수를 이용해서
# 스크립트 언어의 특징인 한 줄 한줄 실행을 할 때 특정 함수를 지정할 수 있다.
# 이렇게 지정된 함수는 '먼저 실행되는 함수'가 된다.
# 정확히는 프로그램의 시작 함수를 지정할 수 있다.
# 파이썬은 스크립트 방식이여서 위부터 아래로 차례차례 실행되지만 이것을 사용해서 프로그램의 시작 위치를 바꿔줄 수 있다.


# 클래스 안에서는 사용하지 않음. 프로그램을 실행하는 파일에서만 사용.
if __name__ == '__main__':
    # cls2 = Lab26m.MyClass()
    # cls2.compare(2, [1, 4, 8, 10])
    callLab26m()


# 파이썬의 특수한 기능, 내용을 사용할 때 __ 를 사용.
# __main__  특정 함수를 지정해서 실행 : 프로그램의 실행 함수

# 보안을 위해서 :
#   여러 개의 함수가 있다면, 프로그램의 시작을 알리는 함수를 설정할 것
#   전역변수를 최대한 사용하지 않을 것.