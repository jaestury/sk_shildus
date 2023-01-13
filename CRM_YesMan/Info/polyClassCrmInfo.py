# 기존 내용을 수정하기 위해서 다형성을 이용한다.
# 변경 클래스인 poly 를 만들어준다. 역시 클래스인 clsCrmInfo 가 변수로 사용된다.
# 이제 클래스에서 변경한 내용을 사용할 수 있다. main 에서 클래스를 인스턴스화 해서 사용하자.


from Info.classCrmInfo import clsCrmInfo


class polyExtCrmInfo (clsCrmInfo):
    def crmAddress(self):
        tempAddress = super().crmAddress() + "필동로"
        return tempAddress

    def crmEmail(self):
        tempEmail = "메일주소 : " + super().crmEmail()
        return tempEmail
