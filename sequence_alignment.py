#-*- coding: cp949 -*-
import sys

def main(string) :

    f = open(string, "r")
    inData = f.readlines()

    x = []
    y = []
    for data in inData[0] :
        if data != '\n' :
            x.append(data)
    for data in inData[1] :
        y.append(data)
    #print("x : ", x)
    #print("y : ", y)
    #print(len(y+1))
    N = max(len(x), len(y))
    M = min(len(x), len(y))
    swapFlag = True

    if len(x) < len(y) :
        x, y = y, x
        swapFlag = False

    #print("x : ", x)
    #print("y : ", y)
    #opt = [[0]*len(y+1) for i in range(len(y)+1)]
    opt = [[0]*(M+1) for i in range(N+1)]

    #opt[1][N] = 1
    #print(opt)



    for i in range(N+1) :
        opt[i][M] = 2*(N-i)
    for j in range(M+1) :
        opt[N][j] = 2*(M-j)
    #print(opt)


    #temp = []
    #indexGapN = []
    #indexGapM = []
    #startNum = opt[N][M]
    for i in range(N-1, -1, -1) :
        for j in range(M-1, -1, -1):
            #print("i : ", i, "j : ", j)
            if x[i] == y[j] :
                diagonal = opt[i+1][j+1]
            else :
                diagonal = opt[i+1][j+1]+1
            opt[i][j] = min(diagonal,
                            opt[i+1][j]+2, opt[i][j+1]+2)

            #temp = [diagonal, opt[i+1][j]+2, opt[i][j+1]+2]
            #if temp[0] != min(diagonal, opt[i+1][j]+2, opt[i][j+1]+2) :
            #    tempIndex = temp.index(min(opt[i+1][j]+2, opt[i][j+1]+2))
            #    if tempIndex == 1 : indexGapN.append(j)
            #    else : indexGapM.append(i)


            #temp.append(tuple())
    #print(opt)
    #print(indexGapN)
    #print(indexGapM)

    tempValue = (opt[0][0], 0, 0)
    gapAmount = []
    indexGapY = []
    indexGapX = []
    count1 = 0
    count2 = 0

    for i in range(N) :
        for j in range(M) :
            if x[i] == y[j] :
                diag = opt[i+1][j+1]
            else :
                diag = opt[i+1][j+1]+1
            if opt[i][j] == diag :
                if tempValue == (opt[i][j], i, j) :
                    tempValue = (opt[i+1][j+1], i+1, j+1)
                    if diag == opt[i+1][j+1] :
                        gapAmount.append(0)
                    else :
                        gapAmount.append(1)
            elif opt[i][j] == opt[i+1][j]+2 :
                if tempValue == (opt[i][j], i, j) :
                    indexGapY.append(j)
                    gapAmount.append(2)
                    tempValue = (opt[i+1][j], i+1, j)
            elif opt[i][j] == opt[i][j+1] + 2 :
                if tempValue == (opt[i][j], i, j) :
                    indexGapX.append(i)
                    gapAmount.append(2)
                    tempValue = (opt[i][j+1], i, j+1)


    if not (tempValue[1] == N and tempValue[2] == M) :
        if tempValue[1] < N :
            for tempi in range(tempValue[1], N) :
                indexGapY.append(tempi)
                gapAmount.append(2)
        elif tempValue[2] < M :
            for tempj in range(tempValue[2], M) :
                indexGapX.append(tempj)
                gapAmount.append(2)

    #print("indexGapX : ", indexGapX)
    #print("indexGapY : ", indexGapY)
    #print("gapAmount : ", gapAmount)

    print("Sequence penalty score = ", opt[0][0])



    countX = 0
    countY = 0
    for xdata in indexGapX :
        x.insert(xdata+countX, '-')
        countX = countX+1
    for ydata in indexGapY :
        y.insert(ydata+countY, '-')
        countY = countY + 1

    if swapFlag == False :
        x, y = y, x

    for xdata in x :
        print(xdata, end = ' ')
    print()
    for ydata in y :
        print(ydata, end = ' ')
    print()
    for gap in gapAmount :
        print(gap, end = ' ')

if __name__ == "__main__" :
    main(sys.argv[1])
