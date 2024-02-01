def binary_search(list, a):
    if list[0]>list[-1]:
        list = list[::-1]
    while len(list) > 1:
        if list[len(list)//2] == a:
            return True
        elif list[len(list)//2] > a:
            list = list[:len(list)//2]
        else:
            list = list[len(list)//2:]
    return False

def bitonic_array_search(arr, a):
    left = 0
    right = len(arr)-1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return binary_search(arr[:left], a) or binary_search(arr[left:], a)

def main():
    ...
if __name__ == '__main__':
    main()  