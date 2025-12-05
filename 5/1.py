# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    1.py                                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ldecavel <ldecavel@student.42lyon.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/05 11:10:48 by ldecavel          #+#    #+#              #
#    Updated: 2025/12/05 11:43:25 by ldecavel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def is_fresh(ingredient_id: int) -> bool:
    for a, b in fresh_ids:
        if a <= ingredient_id <= b:
            return True
    return False

result = 0
with open("input", "r", encoding="utf-8") as f:
    fresh_ids: list[tuple[int, int]] = []
    for line in f:
        line = line.rstrip("\n")
        if not line:
            break
        fresh_ids.append(tuple(map(int, line.split("-"))))
    for line in f:
        ingredient_id = int(line.rstrip("\n"))
        if is_fresh(ingredient_id):
            result += 1
print(result)
