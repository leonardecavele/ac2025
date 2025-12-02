# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    1.py                                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ldecavel <ldecavel@student.42lyon.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/02 15:34:57 by ldecavel          #+#    #+#              #
#    Updated: 2025/12/02 16:12:11 by ldecavel         ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

def is_id_doubled(s: str) -> bool:
    if len(s) % 2 != 0:
        return False
    return s[:len(s) // 2] == s[len(s) // 2:]

result = 0
ids: list[tuple[int, int]] = []

with open("input", "r", encoding="utf-8") as f:
    line = f.readline().rstrip("\n")
    for bit in line.split(","):
        bit = bit.strip()
        a, b = map(int, bit.split("-"))
        ids.append((a, b))
for pair in ids:
    for i in range(pair[0], pair[1] + 1): 
        if is_id_doubled(str(i)):
            result += i
print(result)
