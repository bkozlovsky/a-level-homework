men = ("John", "Charles", "Mike")

women = ("Jenny", "Christy", "Monica", "Vicky")

age = (30, 45, 18, 24, 55)

def zippy(*args):
    shortest_item = len(sorted(args, key=len)[0])
    final_result = []
    for i in range(shortest_item):
        first_combination = []
        for counter, arg in enumerate(args):
            first_combination.append(args[counter][i])
        final_result.append(tuple(first_combination))
    return tuple(final_result)

print("Result from a custom zip function:\n\n")
for item in zippy(men, women, age):
    print(item)

print("\n\nResult from the original ZIP function:\n\n")

for z in zip(men, women, age):
    print(z)