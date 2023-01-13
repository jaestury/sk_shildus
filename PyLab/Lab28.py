# 프로그램 실행 파일 위치 : D:\PyLab
# 패키지는 실행 파일 위치 다음 폴더가 기본 패키지 : MyPkg
# 패키지는 실행 파일 위치 다음 폴더에 모듈을 모아 놓는 곳을 파이썬에서는 패키지라 부름.
# 모듈이 많으면 모듈을 폴더로 구분하기 위해서 패키지를 사용한다.
# 3.2 버전까지는 패키지 폴더 구분하기 위해 폴더에 __init__.py 파일을 생성해야 했지만,
# 3.3 이상부터는 없어도 가능하다.

# import 폴더명.모듈명 형식으로 사용한다.
# import MyPkg.Lab28m

# from, as 도 사용가능하다.
from MyPkg.Lab28m import compare

arrayData = [23, 56, 66, 77]
inputData = 50

# result = MyPkg.Lab28m.compare(inputData, arrayData)

# from - import 로 함수만 추출해서 사용하기.
result = compare(inputData, arrayData)

temp = 1
