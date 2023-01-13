# 튜플. Tuple = ( ) 데이터를 저장 후 수정 불가
# 데이터를 튜플 형식으로 하는 것 : 패킹
# 튜플 안에 있던 데이터를 변수에 할당하는 것 : 언패킹

# 한번 변수에 할당하면 절대 변경 불가
tupleData1 = ("홍길동", 20, 99.99, False)

intTypeData = (999) # int 형식으로 저장
intTypeData = 21131.23
tupleTypeData = (999, 22) # tuple형식으로 저장 : 명시적으로 튜플 형식 지정
tupleTypeData = 123124

# 튜플 변경은 불가하지만, 병합은 가능하다. : 리스트의 extend는 쓰지 않는다.
tupleData2 = ("주소", "서울시", "동국대학교")
tupleData3 = tupleData1 + tupleData2 # 병합 : 튜플들을 병합하여 새로운 튜플을 생성한다.

# 튜플 데이터를 변수에 할당
# 언패킹. 인덱스 기호 이용한다.
name = tupleData1[0]

age = tupleData1[1]


ill = 1