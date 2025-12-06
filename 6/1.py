# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    1.py                                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ldecavel <ldecavel@student.42lyon.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/06 11:40:56 by ldecavel          #+#    #+#              #
#    Updated: 2025/12/06 12:29:00 by ldecavel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

result = 0
with open("input", "r", encoding="utf-8") as f:
    values: list[list[int]] = []
    for line in f:
        try:
            values.append(list(map(int, line.split())))
        except:
            values.append(list(map(str, line.split())))
    tmp = 0
    for x in zip(*values):
        result += tmp
        tmp = 0
        for i, y in enumerate(x[:-1]):
            if x[-1] == '+' or not i:
                tmp += y
            elif x[-1] == '*':
                tmp *= y
result += tmp
print(result)
