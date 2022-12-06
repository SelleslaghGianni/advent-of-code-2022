X = [line.strip() for line in open('input4.txt')]

p1 = 0
p2 = 0

for line in X:
    first_range, second_range = line.split(",")
    first, second = first_range.split("-")
    first_set = set(range(int(first), int(second)+1))
    first, second = second_range.split("-")
    second_set = set(range(int(first), int(second)+1))
    result = first_set.intersection(second_set)
    if len(result) == len(first_set) or len(result) == len(second_set):
        p1 += 1
    if len(result) > 0:
        p2 += 1

print(p1)
print(p2)
