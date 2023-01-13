# 리스트 : 수정, 삭제, 추가

arrayList1 = [11, 22, 33, 44, 55]

# 리스트 추가 : 기능 이용. append() 기능

arrayList1.append(66)

# 리스트 변경 : [] 몇번째 데이터를 변경할지 지정
arrayList1[1] = 22.22

# 리스트 삭제 : del 기능 사용
del arrayList1[1]

# 리스트의 병합 : + 기호 이용하면 새로운 리스트 변수 추가
arrayList2 = [11, 22, 33, 44, 55]
arrayList3 = [66, 77, 88, 99]
arrayplus = arrayList2 + arrayList3

# extend() 기능 사용하면 기존 리스트에 추가.
arrayList5 = [11, 22, 33, 44, 55]
arrayList6 = [66, 77, 88, 99]

# arrayList5 에 arrayList6 을 추가한다.
arrayList5.extend(arrayList6)

# 검색과 갯수 구하기
arrayList7 = [111, 222, 333, 444, 555]

# index : 몇 번 째 요소에 있는지 확인한다.
arraySearchResult = arrayList7.index(333) # 333이라는 값이 있는지 확인하고 몇번째 요소인지 알려줌

arrayList7.append(444)
# count : 몇 개 있는지 확인하기
arrayListCount = arrayList7.count(444) # 444라는 값이 몇 개 있는지 확인한다.

if arrayListCount > 0 :
    # 몇 개의 데이터가 있습니다. 처리한다.
    print("")

# List의 갯수 확인 : 우리가 생각하는 갯수. 즉 1부터 센 숫자로 준다.
arrayListLength = len(arrayList7)

when = 1