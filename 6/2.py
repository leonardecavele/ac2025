# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    2.py                                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ldecavel <ldecavel@student.42lyon.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/06 11:40:56 by ldecavel          #+#    #+#              #
#    Updated: 2025/12/06 14:32:37 by ldecavel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

to_compute: list[list[int | str]] = []

def parse(file: list[str]) -> None:
    calc = []
    for line in reversed(list(zip(*file))):
        power = 1
        number = 0
        for c in range(len(line) - 1, -1, -1):
            if line[c] == '*' or line[c] == '+':
                opcode = line[c]
            if line[c].isdigit():
                number += int(line[c]) * power
                power *= 10
            if c == 0:
                if not number:
                    calc.append(opcode)
                    to_compute.append(calc)
                    calc = []
                else:
                    calc.append(number)
    calc.append(opcode)
    to_compute.append(calc)

result = 0
tmp = 0
with open("input", "r", encoding="utf-8") as f:
    parse([line.rstrip("\n") for line in f])
    for operation in to_compute:
        opcode = operation.pop()
        result += tmp
        tmp = 0
        for i, operand in enumerate(operation):
            if opcode == '+' or not i:
                tmp += operand
            elif opcode == '*':
                tmp *= operand
result += tmp
print(result)
