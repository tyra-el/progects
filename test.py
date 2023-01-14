row = [0, 1, 4, 6, 4, 1, 0]

new = [0] + [row[i]+row[i+1] for i in range(len(row)-1)] + [0]
print(new)