class Pown:
    def pown(self, n):
        a = 0
        for i in range(1, n+1):
            a = pow(i, 2) + a
            i = i + 1
        return a


if __name__ == '__main__':
    test: Pown = Pown()
    print(test.pown(int(input('请输入一个整数n：'))))