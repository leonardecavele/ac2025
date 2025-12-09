# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    2.py                                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ldecavel <ldecavel@student.42lyon.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/09 10:25:57 by ldecavel          #+#    #+#              #
#    Updated: 2025/12/09 10:29:49 by ldecavel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def unique(array):
    return (list(set(array)))

result = 0
with open("input", "r", encoding="utf-8") as f:
    green_tile = set()
    board = [list(map(int, line.rstrip("\n").split(","))) for line in f]

    board.sort(key=lambda v: v[0])
    i = 0
    while i < len(board):
        if i + 1 == len(board):
            break
        if board[i + 1][0] == board[i][0]:
            y_min = min(board[i][1], board[i + 1][1])
            y_max = max(board[i][1], board[i + 1][1])
            for y in range(y_min, y_max + 1):
                green_tile.add((board[i][0], y))
        i += 1
    board_width = board[len(board) - 1][0]

    board.sort(key=lambda v: v[1])
    board_height = board[len(board) - 1][1]

    for y in range(board_height + 1):
        first = None
        last = None
        for x in range(board_width + 1):
            if (x, y) in board or (x, y) in green_tile:
                if first == None:
                    first = x
                last = x
        while first is not None and last is not None and first < last:
            green_tile.add((first, y))
            first += 1

    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            tmp = (abs(board[i][0] - board[j][0]) + 1) * (abs(board[i][1] - board[j][1]) + 1)
            if tmp > result and (board[i][0], board[j][1]) in green_tile and (board[j][0], board[i][1]) in green_tile:
                result = tmp
    print(result) 
