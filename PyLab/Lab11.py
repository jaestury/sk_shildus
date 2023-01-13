# 사용자 입력받는 값을 지정
userID = "abd"
userPW = "123"

# DB에 사용자 계정이 있는지 확인하는 구문 작성
# DB 정보를 가져왔다 가정을 하고 코드 작성
dbUserID = "abcd"
dbUserPW = "1234"

if (userID == dbUserID) and (userPW == dbUserPW) : 
    result = True # 로그인 성공 후 작업 코드를 작성
else : 
    result = False
    # 로그인 실패 코드를 작성
    # 로그인 실패 : ID 또는 비밀번호 잘못 입력
    # ID와 비밀번호 둘 중 어느 쪽이 틀렸는지 표시하면 안됨

# 중첩 if 문 사용하는 방법. 
if userID == dbUserID :
    if userPW == dbUserPW :
        result = "로그인 성공"
    else :
        result = "로그인 실패 : ID 또는 비밀번호를 잘못 입력"
    # 시스템 로그에 비밀번호 실패 기록만 한다.
else : 
    result = "로그인 실패 : ID 또는 비밀번호를 잘못 입력"
    # 시스템 로그에 아이디 실패 기록만 한다.
 
# 보안 요소에 아이디, 비밀번호 성공/실패 기록이 필요하다면 아래 쪽처럼 만들 필요가 있다.
# 시스템 입장에서 실행에 아무 문제 없지만, 사용자 요구사항을 반영하여 더 적합한 코드를 작성할 필요가 있다.

temp =1 