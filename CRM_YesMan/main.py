# 순서. main 파일을 만들어서 전체 틀을 만든다.
# 다음 기초 모듈 crmInfo 구성
# 기능 추가를 위해 classCrmInfo 를 구성하고 함수를 추가해준다.
# 추가된 함수를 상속하기 위한 extClassCrmInfo 구성
#   클래스 사용을 위한 인스턴스 작성.  crm = Info.extClassCrmInfo.extCrmInfo()
# 데이터 변경을 위한 polyClassCrmInfo 구성.
#   클래스 사용을 위한 인트선스 작성.  polyCrm = Info.polyClassCrmInfo.polyExtCrmInfo()

import Info.crmInfo
import Info.classCrmInfo
import Info.extClassCrmInfo
import Info.polyClassCrmInfo


# 프로그램을 시작하는 첫 파일, 첫 함수
if __name__ == '__main__':

    # 상속 인스턴스 작성
    extCrm = Info.extClassCrmInfo.extCrmInfo()

    # 다형성 인스턴스 작성
    polyCrm = Info.polyClassCrmInfo.polyExtCrmInfo()

    # 모듈에서 함수 가져다가 쓰기
    name = Info.crmInfo.crmName()

    # 모듈에서 함수 가져다가 사용했지만, 내용 수정이 필요함으로 poly 로 내용을 바꿔준다.
    # address = Info.crmInfo.crmAddress()
    crmAddress = polyCrm.crmAddress()

    # 모듈에서 함수 가져다 쓰기
    phoneNumber = Info.crmInfo.crmPhoneNum()

    # age는 추가된 내용이기 때문에 ext 를 사용해 내용을 추가한다.
    age = extCrm.crmAge()

    # email 은 추가되었으며, 내용도 바꿔야한다. 때문에 ext 로 추가되고, poly 로 변경된다.
    # email = extCrm.crmemail()
    email = polyCrm.crmEmail()

temp = 1
