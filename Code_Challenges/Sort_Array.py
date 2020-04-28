array1 = [56,349,22,-54,0,5]
 
print(array1)
print("to")
sorted_list = []
while array1:
    check = array1[0]
    for x in array1: 
        if x < check:
            check = x
    sorted_list.append(check)
    array1.remove(check)    

print(sorted_list)