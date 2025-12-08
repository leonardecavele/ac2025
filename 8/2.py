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

def solve(distances) -> int:
    network = []
    last = 0
    for current in distances:
        flag_found = 0
        for k, linked_list in enumerate(network):
            if current[0][0] in linked_list or current[0][1] in linked_list:
                before_len = len(linked_list)
                new_list = list(set(linked_list + [current[0][0], current[0][1]]))
                network[k] = new_list
                if len(new_list) > before_len:
                    last = current[2] * current[3]
                for j in range(len(network) - 1, k, -1):
                    if current[0][0] in network[j] or current[0][1] in network[j]:
                        before_k = len(network[k])
                        network[k] = list(set(network[k] + network.pop(j)))
                        if len(network[k]) > before_k:
                            last = current[2] * current[3]
                flag_found = 1
                break
        if flag_found == 0:
            network.append([current[0][0], current[0][1]])
            last = current[2] * current[3]
    return last

result = 0
with open("input", "r", encoding="utf-8") as f:
    distances: list[tuple[tuple[int, int], int, int, int]] = []
    values: list[list[int]] = [list(map(int, line.rstrip("\n").split(","))) for line in f]
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            a = values[i]
            b = values[j]
            tmp = 0
            for k in range(3):
                tmp += (a[k] - b[k]) ** 2
            distances.append(((i, j), tmp, a[0], b[0]))
    distances.sort(key=lambda d: d[1])
    print(solve(distances))
