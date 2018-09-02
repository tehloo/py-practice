#   파이썬 장비관리 프로그램 구현

import sys

def showAndGetMenu() :
    print ('''
    1. 입력
    2. 출력
    3. 검색
    4. 종료
    ''')
    return input("메뉴를 선택하시오 : ")

def inputData() :
    bContinue = True

    while (bContinue) :
        data = {}
        data['device'] = input("장비명 : ")
        data['count'] = int(input("수량 : "))
        data['date'] = input("생산일(예: 1990-01-01) : ")
        dataList.append(data)

        while True :
            c = input("계속 입력 하시겠습니까 (y/n) ")
            if ( c == 'y' ) :
                bContinue = True
                break
            elif ( c == 'n') :
                bContinue = False
                break
            else :
                print("y 혹은 n을 입력하세요.")

    return dataList
def printTitleRow () :
    print("------------------------------------")
    print("\t\t%s\t%s\t\t%s" % ("장비명", "수량", "생산일"))
    print("------------------------------------")
    pass

def printDataList (item) :
    print("\t%10s %4d %12s" % (item['device'], item['count'], item['date']))
    pass

def outputData() :
    printTitleRow()
    for d in dataList :
        printDataList(d)

    return True

def searchData ():
    query = input("검색할 장비명을 입력하세요 : ")

    printTitleRow()
    for d in dataList:
        if (d["device"] == query) :
            printDataList(d)
            break

    else:
        print("장비명 %s 을 찾을 수 없습니다. " % query)

    return True

def askToQuit():
    while True:
        q = input("프로그램을 종료하시겠습니까 (y/n) ")
        if (q == 'y') : return "exit"
        elif (q == 'n') : return "continue"
        else : print("y 혹은 n을 입력해주세요")

    pass


gMenuList = {
    1: inputData,
    2: outputData,
    3: searchData,
    4: askToQuit
}

dataList = []

while True :
    menu = int(showAndGetMenu())
    rtn = gMenuList.get(menu)()

    if (rtn == "exit") :
        print ("bye bye~")
        sys.exit(1)

