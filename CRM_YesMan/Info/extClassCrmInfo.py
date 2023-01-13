# 추가된 내용을 사용하기 위해 상속을 해준다.
# 상속 클래스인 ext 를 만들어준다. 변수에는 클래스인 clsCrmInfo 를 넣어준다.
# 이제 클래스에서 추가한 내용을 사용할 수 있다. main 에서 클래스를 인스턴스화 해서 사용하자.

from Info.classCrmInfo import clsCrmInfo


class extCrmInfo(clsCrmInfo):
    def crmage(self):
        return "40대"

    def crmEmail(self):
        return "aaa@aaa.co.kr"
