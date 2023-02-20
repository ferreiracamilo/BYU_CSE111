answers = (True, False, True)
selection = answers[2:]
#selection1 = answers[2]
#print(selection)
#print(selection1)
points = 0
for answer in selection[-1:]:
    if answer:
        points += 1
print(points)