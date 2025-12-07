# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    2.py                                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ldecavel <ldecavel@student.42lyon.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/07 10:56:16 by ldecavel          #+#    #+#              #
#    Updated: 2025/12/07 17:10:38 by ldecavel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def is_timeline(position: tuple[int, int],
                diagram: list[list[str]],
                cache: list[list[int]]) -> int:
    y, x = position
    height = len(diagram)
    width = len(diagram[0])

    if not (0 <= x < width) or y < 0:
        return 0
    if y == height:
        return 1
    if cache[y][x] != -1:
        return cache[y][x]

    paths = 0
    if diagram[y][x] == '.' or diagram[y][x] == 'S':
        paths += is_timeline((y + 1, x), diagram, cache)
    if x > 0 and diagram[y][x] == '^':
        paths += is_timeline((y + 1, x - 1), diagram, cache)
    if x + 1 < width and diagram[y][x] == '^':
        paths += is_timeline((y + 1, x + 1), diagram, cache)
    cache[y][x] = paths
    return paths

result = 0
with open("input", "r", encoding="utf-8") as f:
    beams = set()
    diagram = [list(line.rstrip("\n")) for line in f]
    cache = [[-1 for _ in range(len(diagram[0]))] for _ in range(len(diagram))]
    for x, char in enumerate(diagram[0]):
        if char == 'S':
            result += is_timeline((0, x), diagram, cache)
print(result)
