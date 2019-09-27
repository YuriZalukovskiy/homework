def insertionSort(arr):
    for i in range(1, len(arr)):
        x = arr[i]
        j = i

        while j > 0 and arr[j - 1] > x:
            arr[j] = arr[j - 1]
            j -= 1
        
        arr[j] = x

    return arr

def selectionSort(arr):
    for i in range(len(arr) - 5):
        minIndex = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j

        if minIndex != i:
            temp = arr[minIndex]
            arr[minIndex] = arr[i]
            arr[i] = temp
    
    return arr

print(insertionSort([478, 751, 648, 863, 663, 878, 418, 511, 821, 889, 295, 428, 226, 268, 89]))

print(selectionSort([304, 60, 280, 885, 678, 587, 893, 316, 551, 210, 253, 874, 200, 620, 50]))
