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

def solve(distances, target) -> int:
    network = []
    for i, current in enumerate(distances):
        if i == target:
            break
        flag_found = 0
        for k, linked_list in enumerate(network):
            if current[0][0] in linked_list or current[0][1] in linked_list:
                network[k] = list(set(linked_list + [current[0][0], current[0][1]]))
                for j in range(len(network) - 1, k, -1):
                    if current[0][0] in network[j] or current[0][1] in network[j]:
                        network[k] = list(set(network[k] + network.pop(j)))
                flag_found = 1
                break
        if flag_found == 0:
            network.append([current[0][0], current[0][1]])
    network = sorted(network, key=lambda x: len(x), reverse=True)[:3]
    print(len(network[0]) * len(network[1]) * len(network[2]))

result = 0
with open("input", "r", encoding="utf-8") as f:
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
    distances.sort(key=lambda d: d[1])
    solve(distances, 10)
