X = [l.strip() for l in open('input.txt')]

total_cals = []
count = 0
for cal in X:
    print(cal)
    if cal == '':
        total_cals.append(count)
        count = 0
        continue
    count += int(cal)
    print(count)
total_cals = sorted(total_cals, reverse=True)
print("part 1: " + str(total_cals[0]))
print("part 2: " + str(total_cals[0] + total_cals[1] + total_cals[2]))
