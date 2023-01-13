# 모듈의 수정을 위해 class로 변경해준다.
# class 를 선언해주고 함수를 갖다 붙여준 뒤, 추가하고픈 내용을 넣어준다.
# 하지만 클래스를 만든 것만으로는 사용할 수 없기 때문에 상속을 해줄 필요가 있다.
# 사용되는 모든 함수는 클래스 안에 포함될 필요가 있다.

class clsCrmInfo:
    def crmName(self):
        return "크레토스"

    def crmAddress(self):
        return "서울시 중구"

    def crmPhoneNum(self):
        return "010-1234-5678"

    def crmAge(self):
        return "40대"

    def crmEmail(self):
        return "aaa@aaa.co.kr"
