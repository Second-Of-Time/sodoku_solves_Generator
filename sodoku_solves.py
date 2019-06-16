
# 宫格初始化
import math
import time
import json
from random import randint


# 数独棋盘的生成
def makeBoard(CONST_SIZE):
    board = [[0 for _ in range(CONST_SIZE)] for _ in range(CONST_SIZE)]

    for i in range(0, CONST_SIZE):
        for j in range(0, CONST_SIZE):
            #             board[i][j] = int((i * int(math.sqrt(CONST_SIZE)) + int(i / int(math.sqrt(CONST_SIZE))) + j) % CONST_SIZE) + 1 #整除开方取余法
            board[i][j] = ( i +j ) %CONST_SIZE +1  # 直接生成法
    randomInt = randint(8, 16)
    for _ in range(randomInt):
        board = shuffleBoard(board,CONST_SIZE)

    return board
def shuffleBoard(arr2d,CONST_SIZE):
    chooseNumber = -1
    replacingNumber = -1
    while(replacingNumber == chooseNumber):
        chooseNumber = randint(1, CONST_SIZE)
        replacingNumber = randint(1, CONST_SIZE)
    for i in range(0, CONST_SIZE):
        for j in range(0, CONST_SIZE):
            if(arr2d[i][j] == chooseNumber):
                arr2d[i][j] = replacingNumber
            elif(arr2d[i][j] == replacingNumber):
                arr2d[i][j] = chooseNumber

    sizeOfInnerMatrix = int(math.sqrt(CONST_SIZE))
    if (sizeOfInnerMatrix > 1):
        chooseRowIndex = -1
        replacingRowIndex = -1
        while(chooseRowIndex == replacingRowIndex):
            chooseRowIndex = randint(1, sizeOfInnerMatrix)
            replacingRowIndex = randint(1, sizeOfInnerMatrix)
        multiplier = randint(0, sizeOfInnerMatrix -1)
        chooseRowIndex+=(multiplier *sizeOfInnerMatrix)
        replacingRowIndex +=(multiplier *sizeOfInnerMatrix)
        arr2d[chooseRowIndex - 1], arr2d[replacingRowIndex - 1] = arr2d[replacingRowIndex -1], arr2d[
            chooseRowIndex - 1]
        arr2d = [[x[i] for x in arr2d] for i in range(CONST_SIZE)]
        chooseRowIndex -= (multiplier * sizeOfInnerMatrix)
        replacingRowIndex -= (multiplier * sizeOfInnerMatrix)
        multiplier = randint(0, sizeOfInnerMatrix - 1)
        chooseRowIndex += (multiplier * sizeOfInnerMatrix)
        replacingRowIndex += (multiplier * sizeOfInnerMatrix)
        arr2d[chooseRowIndex - 1], arr2d[replacingRowIndex - 1] = arr2d[replacingRowIndex - 1], arr2d[
            chooseRowIndex - 1]

    return arr2d


def makePuzzleBoard(board, level="easy"):
    sizeSquare = CONST_SIZE * CONST_SIZE
    levels = {
        "easy": ((int(sizeSquare / 2) - int(sizeSquare / 10)), 0),
        "moderate": (int(sizeSquare), int(sizeSquare / 15)),
        "difficult": (int(sizeSquare), int(sizeSquare / 10))
    }
    logicalCutOff = levels[level][0]
    randomCutOff = levels[level][1]
    removeLogically(board, logicalCutOff)
    if randomCutOff != 0:
        removeRandomly(board, randomCutOff)
    return board


def getAllPossibleNumbersInPlace(rowIndex, colIndex, arr2d):
    row = arr2d[rowIndex]
    col = getColoumn(colIndex, arr2d)
    innerMatrix = getInnerMatrix(rowIndex, colIndex, arr2d)
    posibilities = [x for x in range(1, CONST_SIZE + 1) if
                    ((x not in row) and (x not in col) and (x not in innerMatrix))]

    return posibilities


def removeLogically(arr2d, cutOff=25):
    removedItems = 0
    for _ in range(CONST_SIZE * 500):
        i = randint(0, CONST_SIZE - 1)
        j = randint(0, CONST_SIZE - 1)
        temp = arr2d[i][j]
        if (temp == 0):
            continue
        arr2d[i][j] = 0
        if (len(getAllPossibleNumbersInPlace(i, j, arr2d)) != 1):
            arr2d[i][j] = temp
        else:
            removedItems += 1
        if (removedItems == cutOff):
            return


def getColoumn(index, arr2d):
    coloumn = []
    for row in arr2d:
        coloumn.append(row[index])
    return coloumn


def getInnerMatrix(rowIndex, colIndex, arr2d):
    innerMatrix = []
    sizeOfInnerMatrix = int(math.sqrt(CONST_SIZE))
    startRowIndex = 0
    startColIndex = 0
    while ((startRowIndex + sizeOfInnerMatrix) <= rowIndex):
        startRowIndex += sizeOfInnerMatrix
    while ((startColIndex + sizeOfInnerMatrix) <= colIndex):
        startColIndex += sizeOfInnerMatrix
    endRowIndex = startRowIndex + sizeOfInnerMatrix
    endColIndex = startColIndex + sizeOfInnerMatrix
    for i in range(startRowIndex, endRowIndex):
        for j in range(startColIndex, endColIndex):
            innerMatrix.append(arr2d[i][j])
    return innerMatrix


def removeRandomly(board, cutOff):
    removedItem = 0
    for i in range(CONST_SIZE):
        for j in range(CONST_SIZE):
            if (board[i][j] == 0):
                continue
            temp = board[i][j]
            board[i][j] = 0
            tempBoard = [[ele for ele in row] for row in board]
            if (not solveBoard(tempBoard)):
                board[i][j] = temp
            else:
                removedItem += 1
            if (removedItem == cutOff):
                return board
    return board


def solveBoard(arr2d):
    l = [0, 0]
    if (not find_empty_location(arr2d, l, CONST_SIZE)):
        return True
    row = l[0]
    col = l[1]
    for num in range(1, CONST_SIZE + 1):
        safeList = getAllPossibleNumbersInPlace(row, col, arr2d)
        if num in safeList:
            arr2d[row][col] = num
            if (solveBoard(arr2d)):
                return True
            arr2d[row][col] = 0
    return False


def find_empty_location(arr, l, CONST_SIZE):
    for row in range(CONST_SIZE):
        for col in range(CONST_SIZE):
            if (arr[row][col] == 0):
                l[0] = row
                l[1] = col
                return True
    return False


# solve数独

def stringToChar2dArray(input):
    return json.loads(input)


def char2dArrayToString(input):
    return json.dumps(input)


class Solutions():
    def main(self, n):
        def get_sodoku(self, n):
            data = []
            for i in range(n):
                in_put = list(map(int, input('Please input {}th line'.format(i + 1)).split()))
                #                 in_put = list(input('Please input {}th line'.format(i+1)).split())
                data.append(in_put)
            return data

        def print_data(self, data, n):
            for i in range(n):
                for j in range(n):
                    print(data[i][j], end=' ')
                print(' ')

        while True:
            data = get_sodoku(self, n)
            choice = input('ok ?(Yes or No)')
            if choice == 'Y' or choice == 'y':
                break
        print_data(self, data, n)
        #         for i in range(n):
        #                 for j in range(n):
        #                     print(data[i][j],end = ' ')
        return data

    def solveSudokus(self, board, n):
        """
        Do not return anything, modify board in-place instead.
        """
        # 把所有没填数字的位置找到
        all_points = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 0:
                    all_points.append([i, j])
        print('all_points:', all_points)

        # check函数是为了检查是否在point位置k是合适的
        def check(point, k):
            row_i = point[0]
            col_j = point[1]
            for i in range(n):
                # 检查 行
                if i != row_i and board[i][col_j] == k:
                    return False
                # 检查 列
                if i != col_j and board[row_i][i] == k:
                    return False
            # 检查块
            #             print('i:', row_i // 3 * 3, row_i // 3 * 3 + 3)
            #             print(row_i)
            #             print('j', col_j // 3 * 3, col_j // 3 * 3 + 3)
            #             print(col_j)
            for i in range(row_i // 3 * 3, row_i // 3 * 3 + 3):
                for j in range(col_j // 3 * 3, col_j // 3 * 3 + 3):
                    if i != row_i and j != col_j and board[i][j] == k:
                        return False

            return True

        def backtrack(i):
            # 回溯终止条件
            if i == len(all_points):
                return True
            for j in range(1, n + 1):
                # 检查是否合适
                #                 print(str)
                if check(all_points[i], int(j)):
                    # 合适就把位置改过来

                    board[all_points[i][0]][all_points[i][1]] = int(j)
                    if backtrack(i + 1):  # 回溯下一个点
                        return True
                    board[all_points[i][0]][all_points[i][1]] = 0  # 不成功把原来改回来
            return False

        backtrack(0)
    #


if __name__ == '__main__':
    time_start = time.time()
    # 输入宫格数
    n = int(input('Please input the size (3<= N<=5):'))
    CONST_SIZE = 3 * n
choice = input('Are you input sodoku ?(y or n),using the default sodoku')
if choice == 'Y' or choice == 'y':
    n = int(input('Please input the size:'))
    Solve = Solutions()
    data = Solve.main(n)
    print(data)
    Solve.solveSudokus(data, n)
    an = char2dArrayToString(data)
    with open('./sodoku.txt', 'w') as fi:
        fi.write(an)
    print('save success')
else:

    difficulty = input('Please input the difficulty of the sodoku:(1.easy 2.moderate 3.difficult)')
    if difficulty == 1:
        difficultys = 'easy'
    elif difficulty == 2:
        difficultys = 'moderate'
    else:
        difficultys = 'difficult'
    board = makeBoard(CONST_SIZE)
    sodoku = makePuzzleBoard(board, difficultys)
    solve = Solutions()
    solve.solveSudokus(sodoku, CONST_SIZE)
    ans = char2dArrayToString(sodoku)
    print(ans)
    with open('./sodoku.txt', 'w') as fi:
        fi.write(ans)
    print('save success')
    time_ends = time.time()
    print(time_ends - time_start, 's')