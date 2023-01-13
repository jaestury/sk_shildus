# class extempinfo (부모 클래스 이름) : <- 상속

# 파일이 다른 곳에 있으면 무조건 import 해줘야 함.
# import classempinfo
from Info.classempinfo import clsempinfo


class extempinfo(clsempinfo):
    def empmobile(self):
        return "010-2345-3456"
