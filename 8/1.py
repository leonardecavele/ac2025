# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    1.py                                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ldecavel <ldecavel@student.42lyon.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/08 11:11:32 by ldecavel          #+#    #+#              #
#    Updated: 2025/12/08 11:14:49 by ldecavel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from math import sqrt

def solve(distances, ban) -> int:
    minimum = None
    network: list[list[tuple[tuple[int, int], int]]] = []
    for current in enumerate(distances):
        if ban[current[0][0]] < 2 and ban[current[0][1]] < 2:
            ban[current[0][0]]["count"] += 1
            ban[current[0][1]]["count"] += 1
            ban[current[0][0]]["links"].append(current[0][1])
            ban[current[0][1]]["links"].append(current[0][0])
            network.append([])
        #if minimum is None or current[1] < minimum[1]:
        #    if (minimum[0][0] not in ban and minimum[0][1] not in ban) and 
        #        minimum = current
    print(ban)
    #



result = 0
with open("test", "r", encoding="utf-8") as f:
    distances: list[tuple[tuple[int, int], int]] = []
    ban: dict[int, int] = {}
    values: list[list[int]] = [list(map(int, line.rstrip("\n").split(","))) for line in f]
    for i in range(len(values)): # loop to previous last
        for j in range(i + 1, len(values)): # loop to last
            a = values[i]
            b = values[j]
            tmp = 0
            for k in range(3):
                tmp += (a[k] - b[k]) ** 2
            distances.append(((i, j), int(sqrt(tmp))))
            ban[i] = 0
    distances = sorted(distances, key=lambda d: (d[0][0], d[1]))
    print(distances)
    print(ban)
