from util import getlines

def getdata(lines):
    numbers = lines[0].split(',')
    boards = []
    for i in range(1, len(lines), 5):
        boards.append([list(filter(lambda s: s != '', lines[i + x].split(' '))) for x in range(5)])
    return (numbers, boards)

def checkboard(board):
    for i in range(5):
        if all(board[i][j] is None for j in range(5)):
            return True
        if all(board[j][i] is None for j in range(5)):
            return True
    if all(board[i][i] is None for i in range(5)):
        # real bingo has diagonals
        pass
    if all(board[i][4-i] is None for i in range(5)):
        # and the negative diagonal too
        pass
    return False

def safesum(arr):
    sum = 0
    for num in arr:
        sum += int(num or 0)
    return sum

def getscore(board, numbers):
    for count,number in enumerate(numbers):
        for i in range(5):
            for j in range(5):
                if number == board[i][j]:
                    board[i][j] = None
                    if checkboard(board):
                        return (count, int(number) * sum(safesum(row) for row in board))
    return None,None

numbers, boards = getdata(getlines("4"))

scores = sorted([getscore(board, numbers) for board in boards])
print(f"Best score is {scores[0]}. Worst score is {scores[-1]}")

