# import 방법 중에 from
# import 안에 함수가 많은데 특정 함수만 가져올 경우
# from 파일이름 import 함수이름 : 특정 함수만 가져오기

from Lab24m import compare

# 함수가 많아 2개 이상을 가져올 경우
# from 모듈이름 import 함수이름, 함수이름, 함수이름, ...

# 모든 함수를 가져오고 싶으면
# from 모듈이름 import *

arrayData = [3, 5, 555, 777, 999]
inputData = 600

# result = Lab24m.compare(inputData, arrayData)
result = compare(inputData, arrayData)
# compare 만 가져오기 때문에 파일이름을 적어줄 필요가 없다.

# 별칭도 가능
# from 모듈이름 import 함수이름 as 별칭
# 함수를 호출할 때 별칭으로 호출할 수 있다.
# from Lab24m import compare as com

# arrayData = [3, 5, 555, 777, 999]
# inputData = 600

# result = com(inputData, arrayData)
# 위와 같이 사용 가능하다.
