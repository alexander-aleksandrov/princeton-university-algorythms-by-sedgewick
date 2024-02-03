import random
from search import bitonic_array_search

def main():
    n = get_bitonic_array(20)
    guess = n[random.randint(0, len(n)-1)]
    print(bitonic_array_search(n, guess))   

def get_bitonic_array(n):
    arr = []
    arr.append(random.randint(1, 10)) 
    while len(arr) < n:
        arr.append(arr[-1]+random.randint(1, 10))
    arr.sort()
    front = arr[1::2]    
    back = arr[::2]
    return front + back[::-1]

if __name__ == '__main__':
    main()