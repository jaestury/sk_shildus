userName = "wlsgk"
userPW = "1314"

dbUserName = "wlsgk"
dbUserPW = "1313"

if (userName == dbUserName) and (userPW == dbUserPW) :
    result = True, "로그인에 성공했습니다."
else : 
    result = False, "로그인에 실패했습니다."

if userName == dbUserName : 
    if userPW != dbUserPW :
        result = False, "로그인에 실패했습니다. 패스워드가 다릅니다."
    else :
        result = True, "로그인에 성공하였습니다."
else :
    result = False, "로그인에 실패하였습니다. 아이디가 다릅니다."
      
temp = 1