# 프로그램의 시작점.
# 파이썬은 다른 언어들과 다르게 Main 이라는 함수가 없다.
# 파이썬은 프로그램의 첫 파일의 첫 줄부터 시작하니까.

# 객체 지향은 조심스러워야 한다. 왜?
# 기능을 분할하고 역할을 나눌 수 있는 만큼, 분담된 역할을 충족하지 못한다면 못하는 사람이 된다.
# 객체 지향의 핵심은 원하는 기능을 갖춘 프로그램을 약속한 기한까지 모아 완성할 수 있는 것이다.

# 최고의 프로그램 : 내가 넘긴 프로그램을 사용하는 사람에게 전화가 오지 않는 프로그램.
# 너무 작동이 잘돼서 안오든지, 너무 안돼서 사용을 안하기 때문에 안오든지.

# import Info.empinfo
# from Info import empinfo # from을 사용해서 코드를 줄일 수 있다.
# import Info.classempinfo
import Info.extclassempinfo
import Info.polyclassempinfo


# 프로그램이 시작하는 파일, 그리고 처음 시작되어야 하는 함수
if __name__ == '__main__':
    # 부모 클래스를 인스턴스한 결과인 부모 객체를 주석처리한다.
    # emp = Info.classempinfo.clsempinfo
    # 상속 받은 자식 클래스를 객체로 생성하기 때문에 객체 이름이 같음.
    emp = Info.extclassempinfo.extempinfo()
    # 자식 클래스를 통해 자식 클래스에 있는 메서드를 사용할 수 있다.
    # 자식 클래스를 통해 부모 클래스에 있는 메서드도 사용.
    # 자식 클래스를 통해 부모 기능을 모두 사용할 수 있는 것 : 상속
    # 상속 : 원본 코드를 수정, 삭제 못할 경우 부모 클래스의 코드를 그대로 두고 새로운 클래스를 통해서
    # 부모와 자식 클래스를 사용하는 것 : 상속
    nameemp = Info.polyclassempinfo.polyextempinfo()
    # name = emp.empname()
    name = nameemp.empname()  # 재정의 된 것을 사용한다 => 다형성
    age = emp.empage()
    address = emp.empaddress()
    phone = emp.empmobile()
