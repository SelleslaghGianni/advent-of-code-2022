#         [H]         [S]         [D]
#     [S] [C]         [C]     [Q] [L]
#     [C] [R] [Z]     [R]     [H] [Z]
#     [G] [N] [H] [S] [B]     [R] [F]
# [D] [T] [Q] [F] [Q] [Z]     [Z] [N]
# [Z] [W] [F] [N] [F] [W] [J] [V] [G]
# [T] [R] [B] [C] [L] [P] [F] [L] [H]
# [H] [Q] [P] [L] [G] [V] [Z] [D] [B]
#  1   2   3   4   5   6   7   8   9

from copy import deepcopy

stack = [
    ["H", "T", "Z", "D"],
    ["Q", "R", "W", "T", "G", "C", "S"],
    ["P", "B", "F", "Q", "N", "R", "C", "H"],
    ["L", "C", "N", "F", "H", "Z"],
    ["G", "L", "F", "Q", "S"],
    ["V", "P", "W", "Z", "B", "R", "C", "S"],
    ["Z", "F", "J"],
    ["D", "L", "V", "Z", "R", "H", "Q"],
    ["B", "H", "G", "N", "F", "Z", "L", "D"]
]

X = [l.strip() for l in open('input5.txt')]

for x in X:
    cleanup, move = x.split("ove ")
    amount_moved, stacks = move.split(" from ")
    first_stack, second_stack = stacks.split(" to ")
    amount_moved = int(amount_moved)
    first_stack = int(first_stack)
    second_stack = int(second_stack)
    temp_stack = []
    for y in range(amount_moved):
        if len(stack[first_stack-1]) == 1:
            if stack[first_stack-1][0] == "placeholder":
                continue
            stack[first_stack-1].append("placeholder")
            block = stack[first_stack-1].pop(0)
            stack[second_stack-1].append(block)
        else:
            temp_stack.append(stack[first_stack - 1].pop())
            # stack[second_stack - 1].append(block)
    temp_stack.reverse()
    for block in temp_stack:
        stack[second_stack - 1].append(block)

print(stack)
