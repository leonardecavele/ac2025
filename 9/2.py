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

result = 0
with open("test", "r", encoding="utf-8") as f:
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

    tmp = []
    for x, y in green_tile:
        for index in range(x, board_width):
            tmp.append((index, y))
    green_tile = set(list(green_tile) + tmp)

    for i in range(len(board)):
        x1, y1 = board[i]
        for j in range(i + 1, len(board)):
            x2, y2 = board[j]
            tmp = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            if tmp > result and (x1, y2) in green_tile and (x2, y1) in green_tile:
                result = tmp
    print(result) 
