X = [line.strip() for line in open('input3.txt')]

p1_items = []
p2_groups = []
p2_items = []
counter = 0

for rucksack in X:
    group_index = X.index(rucksack) % 3
    if group_index == 0:
        p2_groups.append([rucksack])
    else:
        p2_groups[counter].append(rucksack)
    if group_index == 2:
        counter += 1
    first = rucksack[len(rucksack) // 2:]
    second = rucksack[:len(rucksack) // 2]
    for item in first:
        if item in second:
            p1_items.append(item)
            break

for group_idx in range(len(p2_groups)):
    for item in p2_groups[group_idx][0]:
        if item in p2_groups[group_idx][1]:
            if item in p2_groups[group_idx][2]:
                p2_items.append(item)
                break




# Initialize the sum of priorities
sum_of_priorities = 0

# Iterate through each line
for line in X:
    # Split the line into two compartments
    comp1, comp2 = line[:len(line)//2], line[len(line)//2:]

    # Create sets of characters from each compartment
    comp1_chars = set(comp1)
    comp2_chars = set(comp2)

    # Find the intersection of the two sets
    common_chars = comp1_chars.intersection(comp2_chars)

    # Iterate through each common character
    for char in common_chars:
      # Get the priority of the character
      if char.islower():
        priority = ord(char) - 97 + 1
      else:
        priority = ord(char) - 65 + 27

      # Add the priority to the sum
      sum_of_priorities += priority

# Print the sum of priorities
print("ai")
print(sum_of_priorities)


def calc_score(items):
    item_worth = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = 0
    for priority in items:
        result += item_worth.index(priority) + 1
    return result


print(calc_score(p1_items))
print(calc_score(p2_items))
