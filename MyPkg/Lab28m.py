def compare(inputData, listData):
    printType = None
    for i in range(len(listData)):
        if inputData < listData[0]:
            printType = "0, %d 사이에 있다" % (listData[0])  # 출력 형식 지정하고
            break
        elif inputData <= listData[i]:
            printType = "%d, %d 사이에 있다" % (
                listData[i-1], listData[i])  # 출력 형식 지정하고
            break
        elif inputData >= listData[len(listData) - 1]:
            printType = "%d, %d 사이에 있다" % (
                listData[len(listData) - 1], inputData)  # 출력 형식 지정하고
            break
    return printType
