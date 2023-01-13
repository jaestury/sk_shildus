# 원본 코드를 수정하고 싶은데 원본 파일의 코드를 수정 못할 경우 사용
# 다형성 - 재정의. 오버라이드.
# 상황에 따라 개발자가 선택할 수 있게 해주는 것이 다형성.

# import Info.classempinfo
from Info.classempinfo import clsempinfo


class polyextempinfo (clsempinfo):
    def empname(self):
        # 부모 클래스의 메서드에 접근할 때는 super 사용한다.
        tempname = super().empname() + "님"
        return tempname
