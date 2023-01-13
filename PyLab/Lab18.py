# 튜플의 인덱싱과 슬라이싱

tupleData = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# 인덱스 [] <- 리스트 데이터 사용 또는 인덱스 기호
# 리스트 사용과 거의 비슷함
data1 = tupleData[1]
data2 = tupleData[-1] # 뒤에서

data3 = tupleData[1:2]
data4 = tupleData[2:] # 콜론 앞에 있으면 0번부터 셀 것
data5 = tupleData[:4] # 콜론 뒤에 있으면 일반적으로 셀 것

# 리스트에서는 : : 콜론 두 번 쓸 수 있었는걸?
data6 = tupleData[1:6:2]
data7 = tupleData[::-1] # 튜플은 변경이 되면 안된다. 할 수는 있지만, 웬만하면 하지 말자.

pick = 1 