import sys
sys.path.append("d:\\Projects\\princeton-university-algorythms-by-sedgewick\\")

from sorts import quick_sort
import random

def main():
    bolts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    screws = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    random.shuffle(bolts)
    random.shuffle(screws)
    quick_sort(bolts, 0, len(bolts)-1)
    quick_sort(screws, 0, len(screws)-1)
    print(bolts)
    print(screws)        
    

if __name__ == "__main__":
    main()