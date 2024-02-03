import time
from search import binary_search

def main():
    n = [i for i in range(-200, 200)]
    count = 0
    time1 = time.perf_counter()
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            if binary_search(n[j+1:], -(n[i] + n[j])):
                count += 1
    time2 = time.perf_counter()

    print("Excution time:", time2 - time1)
    print(count)




if __name__ == '__main__':
    main()  