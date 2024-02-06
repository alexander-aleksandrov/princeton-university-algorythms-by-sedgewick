import random

def main():
    # Create a list of unsorted numbers
    #numbers = [i for i in range(11)]
    #random.shuffle(numbers)

    numbers = [2, 6, 12, 15, 18, 1, 5, 9, 14, 20]
    quick_sort(numbers, 0, len(numbers)-1)
    print(numbers)


def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                arr[i], arr[j] = arr[j], arr[i]

def insertion_sort(arr):
    for i in range(len(arr)):
        for j in range(i, 0, -1):
            if arr[j]<arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

def insertion_sort(arr, lo, hi):
    for i in range(lo, hi):
        for j in range(i, lo, -1):
            if arr[j]<arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]


def shell_sort(arr):
    h = 1 
    while h < len(arr)/3: #1, 4, 13, 40, 121 - increments
        h = 3*h + 1
    while h >= 1:    
        for i in range(h, len(arr)):        
            for j in range(i, 0, -h):
                if arr[j]<arr[j-h]:
                    arr[j], arr[j-h] = arr[j-h], arr[j]
        h = int((h-1)/3)

def dutch_flag_sort(arr):
    low = 0
    high = len(arr) - 1
    i = 0
    while i <= high:
        if arr[i] == 1:
            arr[i], arr[low] = arr[low], arr[i]
            i += 1
            low += 1
        elif arr[i] == 2:
            i += 1
        else:
            arr[i], arr[high] = arr[high], arr[i]
            high -= 1
    
def merge_sort(arr):
    if len(arr)>1:      
        mid = int(len(arr)/2)
        left = arr[:mid]
        right = arr[mid:] 
        sorted_left = merge_sort(left)
        sorted_right = merge_sort(right)
        i = 0
        j = 0
        for k in range(len(arr)):
            if i >= len(sorted_left):
                arr[k] = sorted_right[j]
                j += 1
                continue
            elif j >= len(sorted_right):
                arr[k] = sorted_left[i]
                i += 1
                continue
            if sorted_left[i] < sorted_right[j]:
                arr[k] = sorted_left[i]
                i += 1
            else:
                arr[k] = sorted_right[j]
                j += 1                
        return arr
    else:
        return arr 

# can be used for lists with odd number of items    
def merge_sort_bottom_up(arr):  
    size = 1
    while int(len(arr)//size) > 1:
        lower_bound = 0
        upper_bound = 2*size+lower_bound 
        while upper_bound < len(arr):
            if 2*size+lower_bound > len(arr):
                lower_bound -= size*2
                upper_bound = len(arr)
                mid = lower_bound + size*2
            else:
                upper_bound = 2*size+lower_bound 
                mid = lower_bound + size
            merge(arr, lower_bound, mid, upper_bound)          
            lower_bound += size*2
        size *=2

def merge(arr, lo, mid, hi):
    left = arr[lo:mid]
    right = arr[mid:hi]
    i = 0
    j = 0
    for k in range(lo, hi):
        if i >= len(left):
            arr[k] = right[j]
            j += 1
            continue
        elif j >= len(right):
            arr[k] = left[i]
            i += 1
            continue
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1     

def quick_sort(arr, lo, hi):
    if len(arr) == 1:
        return arr
    if lo >= hi:
        return
    k = arr[lo]
    i = lo + 1
    lb = lo 
    ub = hi
    while i <= ub:
        if arr[i] < k:
            arr[i], arr[lb] = arr[lb], arr[i]
            i += 1
            lb += 1
        elif arr[i] > k:
            arr[i], arr[ub] = arr[ub], arr[i]
            ub -= 1
        else:
            i += 1
                
    quick_sort(arr, lo, lb-1)
    quick_sort(arr, ub+1, hi)

            
            
        









if __name__ == "__main__":
    main()