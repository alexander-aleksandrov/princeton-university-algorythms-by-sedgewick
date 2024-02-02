import sys 
from randomized_queue import RandomizedQueue

def main():
    rq = RandomizedQueue()
    if len(sys.argv) != 3:
        print("Usage: python permutation.py <int> <path>")
        return
    else:
        k = int(sys.argv[1])
        path = sys.argv[2]
        with open(path, 'r') as file:
            data = file.read()
            data = data.split()
        for item in data:
            rq.enqueue(item)
        for i in range(k):
            print(rq.dequeue())

if __name__ == "__main__":
    main()              