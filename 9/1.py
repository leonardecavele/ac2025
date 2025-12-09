# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    1.py                                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ldecavel <ldecavel@student.42lyon.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/09 10:03:53 by ldecavel          #+#    #+#              #
#    Updated: 2025/12/09 10:07:54 by ldecavel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

result = 0
with open("input", "r", encoding="utf-8") as f:
    board = [list(map(int, line.rstrip("\n").split(","))) for line in f]
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            tmp = (abs(board[i][0] - board[j][0]) + 1) * (abs(board[i][1] - board[j][1]) + 1)
            if tmp > result:
                result = tmp
    print(result)

