def jumpingOnClouds(c):
    index_count = 0
    jumps = []
    while index_count < len(c) - 1:
        if index_count + 2 >= len(c) or c[index_count + 2] == 1:
            index_count += 1
            jumps.append(index_count)
        else:
            index_count += 2
            jumps.append(index_count)
        
    return len(jumps)

list1 = [0, 0, 1, 0, 0, 1, 0]

print(jumpingOnClouds(list1))
