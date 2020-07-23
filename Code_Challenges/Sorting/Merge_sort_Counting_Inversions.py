#first solution 3/13

def countInversions(arr):
    inv_count = 0
    n = len(arr)
    for i in range(n): 
        for j in range(i + 1, n): 
            if (arr[i] > arr[j]): 
                inv_count += 1
  
    return inv_count 

    #best solution I Had 10/13


def countInversions(arr):
    n = len(arr)
    temp_arr = [0]*n 
    return _mergeSort(arr, temp_arr, 0, n-1) 
  
def _mergeSort(arr, temp_arr, left, right): 
  
    inv_count = 0
  
    if left < right: 
        mid = (left + right)//2
        inv_count += _mergeSort(arr, temp_arr, left, mid) 
        inv_count += _mergeSort(arr, temp_arr, mid + 1, right) 
        inv_count += merge(arr, temp_arr, left, mid, right) 
    return inv_count 
  
def merge(arr, temp_arr, left, mid, right): 
    i = left    
    j = mid + 1
    k = left
    inv_count = 0

    while i <= mid and j <= right: 
  
        # There will be no inversion if arr[i] <= arr[j] 
  
        if arr[i] <= arr[j]: 
            temp_arr[k] = arr[i] 
            k += 1
            i += 1
        else: 
            # Inversion will occur. 
            temp_arr[k] = arr[j] 
            inv_count += (mid-i + 1) 
            k += 1
            j += 1
  
    # Copy the remaining elements of left subarray into temporary array 
    while i <= mid: 
        temp_arr[k] = arr[i] 
        k += 1
        i += 1
  
    # Copy the remaining elements of right subarray into temporary array 
    while j <= right: 
        temp_arr[k] = arr[j] 
        k += 1
        j += 1
  
    # Copy the sorted subarray into Original array 
    for loop_var in range(left, right + 1): 
        arr[loop_var] = temp_arr[loop_var] 
          
    return inv_count 