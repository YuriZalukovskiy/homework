from datetime import datetime

def mergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
  
        mergeSort(left)
        mergeSort(right)
  
        i = j = k = 0

        while i < len(left) and j < len(right): 
            if left[i] < right[j]: 
                array[k] = left[i] 
                i += 1
            else: 
                array[k] = right[j] 
                j += 1

            k+=1

        while i < len(left): 
            array[k] = left[i] 
            i += 1
            k += 1
          
        while j < len(right): 
            array[k] = right[j] 
            j += 1
            k += 1

def heapify(array, length, i): 
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < length and array[i] < array[left]: 
        largest = left

    if right < length and array[largest] < array[right]: 
        largest = right
  
    if largest != i: 
        array[i], array[largest] = array[largest], array[i]
  
        heapify(array, length, largest) 

def heapSort(array): 
    length = len(array) 

    for i in range(length, -1, -1): 
        heapify(array, length, i) 

    for i in range(length - 1, 0, -1): 
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0) 

def partition(array, low, high):
    i = (low - 1)
    pivot = array[high]
  
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1 
            array[i], array[j] = array[j], array[i] 
  
    array[i + 1], array[high] = array[high], array[i + 1] 

    return (i + 1)

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)

        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)
    
    return array

f = open('file.txt', 'r')

originalArray = []

while True:
    if f.read(1) == '6':
        if f.read(2) == ': ':
            symbol = f.read(1)

            while symbol != '}':
                originalArray.append(int(symbol))
                symbol = f.read(1)
            
            break

f.close()

array = originalArray.copy()
start_time = datetime.now()
mergeSort(array)
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time)) # Duration: 0:00:00.000085

array = originalArray.copy()
start_time = datetime.now()
heapSort(array)
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time)) # Duration: 0:00:00.000070

array = originalArray.copy()
start_time = datetime.now()
quickSort(array, 0, len(array) - 1)
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time)) # Duration: 0:00:00.000044
