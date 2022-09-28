import csv #導入csv模組

def gotWorld():

    world = []

    with open("worldData.csv",encoding="UTF-8-sig") as csvFile:
        #建立串列儲存世界資訊之資料，判斷非1字元，改為0，1則不更改
        csvReader = csv.reader(csvFile)
        listReport = list(csvReader)
        for index in listReport:
            for j in range(len(index)):
                if index[j] != "1":
                    index[j] = "0"
            world.append( list(map(int,index)) )
    
    #回傳世界、寬度、長度資料
    width = len(world[0])
    length = len(world)

    return world,width,length

    