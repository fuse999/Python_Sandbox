lst_of_array = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
min_val = []
for i in lst_of_array:
    min_val.append(min(i))

print(sum(min_val))