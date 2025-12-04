# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    2.py                                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ldecavel <ldecavel@student.42lyon.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/04 11:23:13 by ldecavel          #+#    #+#              #
#    Updated: 2025/12/04 17:16:21 by ldecavel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

pos = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def check_neighbour(board: list[str], y: int, x: int) -> bool:
    count = 0
    height = len(board)
    width = len(board[0])
    for y_offset, x_offset in pos:
        new_y = y + y_offset
        new_x = x + x_offset
        if 0 <= new_y < height and 0 <= new_x < width:
            if board[new_y][new_x] == '@':
                count += 1
    return count < 4

result = 0
tmp = -1
with open("input", "r", encoding="utf-8") as f:
    board = [list(line.rstrip("\n")) for line in f]
    while result > tmp:
        tmp = result
        for y, line in enumerate(board):
            for x, c in enumerate(line):
                if c != '@':
                    continue
                if check_neighbour(board, y, x):
                    board[y][x] = 'x'
                    result += 1
print(result)
