test_array = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]

def result(array):
    for i in array:
        if i % 3 == 0:
            print(i)

result(test_array)