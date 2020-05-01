'''
Write a Python program to push all zeros to the end of a list. Go to the editor
Input : [0,2,3,4,6,7,10]
Output : [2, 3, 4, 6, 7, 10, 0]
'''

input = [0,2,3,4,6,7,10]

# Function to append all zeros at the end  
# of array 
def move_Zeros_end(x): 
    return [nonZero for nonZero in x if nonZero!=0] + [Zero for Zero in x if Zero==0] 
  
print(move_Zeros_end(input))