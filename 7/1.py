# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    1.py                                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ldecavel <ldecavel@student.42lyon.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/07 10:56:16 by ldecavel          #+#    #+#              #
#    Updated: 2025/12/07 11:51:14 by ldecavel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

RED = "\033[31m"
RESET = "\033[0m"

result = 0
with open("input", "r", encoding="utf-8") as f:
    beams = set()
    diagram = [list(line.rstrip("\n")) for line in f]
    for y, line in enumerate(diagram):
        for x, char in enumerate(line):
            if char == 'S' or char == '|':
                beams.add((y + 1, x))
        while beams:
            position = beams.pop()
            if position[0] > len(diagram) - 1:
                continue
            if diagram[position[0]][position[1]] == '.':
                diagram[position[0]][position[1]] = '|'
            elif diagram[position[0]][position[1]] == '^':
                result += 1
                if position[1] + 1 < len(diagram[0]):
                    diagram[position[0]][position[1] + 1] = '|'
                if position[1] - 1 >= 0:
                    diagram[position[0]][position[1] - 1] = '|'
for line in diagram:
    for char in line:
        if char == '|':
            print(f" {RED}{char}{RESET} ", end="")
        else:
            print(f" {char} ", end="")
    print("\n")
print(result)
