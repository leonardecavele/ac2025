# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    2.py                                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ldecavel <ldecavel@student.42lyon.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/02 15:34:57 by ldecavel          #+#    #+#              #
#    Updated: 2025/12/02 16:36:09 by ldecavel         ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

def is_id_repeated(s: str) -> bool:
    for i in range(1, len(s)):
        if len(s) % i != 0:
            continue
        slices: list[str] = []
        for j in range(0, len(s), i):
            slices.append(s[j:j+i])
        if all(res == slices[0] for res in slices):
            return True
    return False

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
        if is_id_repeated(str(i)):
            result += i
print(result)
