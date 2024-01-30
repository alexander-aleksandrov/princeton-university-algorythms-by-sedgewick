from quiq_union import QU

def main():
    qu = QU(10)
    qu.union(0, 1)
    qu.union(2, 3)
    print(qu.is_connected(2, 0))


if __name__ == '__main__':
    main()