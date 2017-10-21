import math


def node_parent(child):
    return int((child - 1) / 2)


def sift_down(arr, N, root):
    imax = root
    while root <= node_parent(N - 1):
        lchild = 2 * root + 1
        rchild = 2 * root + 2
        if lchild <= (N - 1) and arr[imax] < arr[lchild]:
            imax = lchild
        if rchild <= (N - 1) and arr[imax] < arr[rchild]:
            imax = rchild
        if imax == root:
            return
        else:
            arr[imax], arr[root] = arr[root], arr[imax]
            root = imax


def heapify(arr, N):
    ibegin = node_parent(N - 1)
    while ibegin >= 0:
        sift_down(arr, N, ibegin)
        ibegin -= 1


def heapSort(arr):
    N = len(arr)
    heapify(arr, N)
    unsorted = N
    while unsorted > 1:
        arr[0], arr[unsorted - 1] = arr[unsorted - 1], arr[0]
        unsorted -= 1
        sift_down(arr, unsorted, 0)


def main():
    arr = [12, 11, 13, 5, 6, 7, 1, 1, 2, 2, 2, 2, 100]
    heapSort(arr)
    n = len(arr)
    print ("Sorted array is")
    for i in range(n):
        print ("%d" % arr[i]),
    pass


if __name__ == '__main__':
    main()
