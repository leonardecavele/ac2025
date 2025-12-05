# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    2.py                                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ldecavel <ldecavel@student.42lyon.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/05 11:10:48 by ldecavel          #+#    #+#              #
#    Updated: 2025/12/05 12:22:45 by ldecavel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

result = 0
with open("input", "r", encoding="utf-8") as f:
    fresh_ids: list[tuple[int, int]] = []
    merged_ids: list[tuple[int, int]] = []
    for line in f:
        line = line.rstrip("\n")
        if not line:
            break
        fresh_ids.append(tuple(map(int, line.split("-"))))
    fresh_ids.sort()
    for i, (a, b) in enumerate(fresh_ids):
        if i > 0 and a <= merged_ids[-1][1] + 1:
            previous = merged_ids.pop()
            merged_ids.append((previous[0], max(previous[1], b)))
        else:
            merged_ids.append((a, b))
    for a, b in merged_ids:
        #print(f"{a}-{b}")
        result += b - a + 1
print(result)
