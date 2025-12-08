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

def solve(distances, taken, target) -> int:
    network = []
    for i, current in enumerate(distances):
        flag_found = 0
        if i == target:
            break
        if taken[current[0][0]] or taken[current[0][1]]:
            continue
        for linked_list in network:
            if min(current[0]) == min(linked_list[0]) and max(current[0]) == max(linked_list[0]):
                break
            if linked_list[0][0] == current[0][0] or linked_list[0][0] == current[0][1]:
                if linked_list[0][0] == current[0][0]:
                    taken[linked_list[0][0]] = True
                    linked_list[0][0] = current[0][1]
                else:
                    taken[linked_list[0][0]] = True
                    linked_list[0][0] = current[0][0]
                linked_list[1] += 1
                flag_found = 1
                break
            elif linked_list[0][1] == current[0][0] or linked_list[0][1] == current[0][1]:
                if linked_list[0][1] == current[0][0]:
                    taken[linked_list[0][1]] = True
                    linked_list[0][1] = current[0][1]
                else:
                    taken[linked_list[0][1]] = True
                    linked_list[0][1] = current[0][0]
                linked_list[1] += 1
                flag_found = 1
                break
        if not flag_found:
            network.append([[current[0][0], current[0][1]], 2])
        print(network)

result = 0
with open("test", "r", encoding="utf-8") as f:
    taken: list[bool] = []
    distances: list[tuple[tuple[int, int], int]] = []
    values: list[list[int]] = [list(map(int, line.rstrip("\n").split(","))) for line in f]
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            a = values[i]
            b = values[j]
            tmp = 0
            for k in range(3):
                tmp += (a[k] - b[k]) ** 2
            distances.append(((i, j), int(sqrt(tmp))))
        taken.append(False)
    distances.sort(key=lambda d: d[1])
    solve(distances, taken, 10)
