# @author: Cai Jie
# @Date:   2018/5/7 18:27

from numpy.random import randint, seed


def main():
    seed(1)
    lyst = randint(1, 100, 10)
    print("original list: %s" % lyst)

    # classic O(n^2) sort algorithm
    selection_sort(lyst)
    bubble_sort(lyst)
    insertion_sort(lyst)

    # classic O(nlogn) sort algorithm
    quick_sort(lyst)
    merge_sort(lyst)

    # fibnacci queue
    print(fib(20))

    # binary search
    lyst.sort()
    binary_search(2, lyst)




def swap(lyst, i, j):
    tmp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = tmp


def selection_sort(lyst):
    for i in range(len(lyst)-1):
        lyst_min_index = i
        for j in range(i+1, len(lyst)):
            if lyst[j] < lyst[lyst_min_index]:
                lyst_min_index = j
        if lyst_min_index != i:
            swap(lyst, i, lyst_min_index)
    print("selecton sorted list: %s" % lyst)


def bubble_sort(lyst):
    max_unsorted_index = len(lyst)
    while max_unsorted_index > 0:
        i = 1
        while i < max_unsorted_index:
            if lyst[i-1] > lyst[i]:
                swap(lyst, i-1, i)
            i += 1
        max_unsorted_index -= 1
    print("bubble sorted list: %s" % lyst)


def insertion_sort(lyst):
    n = 1               # 未排序数字下标起始下标
    while n < len(lyst):
        insert_item = lyst[n]
        m = n - 1               # 开始往有序序列插入
        while m >= 0:
            if lyst[m] > lyst[m+1]:
                lyst[m + 1] = lyst[m]
                m -= 1
            else:
                break
        lyst[m+1] = insert_item
        n += 1
    print("insertion sorted list: %s" % lyst)


def quick_sort(lyst):
    quick_sort_helper(lyst, 0, len(lyst)-1)
    print("quicksort sored list: %s" % lyst)


def quick_sort_helper(lyst, left, right):
    if left < right:
        pivot_index = partition(lyst, left, right)
        quick_sort_helper(lyst, left, pivot_index-1)
        quick_sort_helper(lyst, pivot_index+1, right)


def partition(lyst, left, right):
    middle = (left+right)//2
    pivot = lyst[middle]
    lyst[middle] = lyst[right]
    lyst[right] = pivot

    boundary = left
    for i in range(left, right):
        if lyst[i] < pivot:
            swap(lyst, boundary, i)
            boundary += 1
    swap(lyst, boundary, right)
    return boundary


def merge_sort(lyst):
    buffer = [None]*len(lyst)
    merge_sort_helper(lyst, 0, len(lyst)-1, buffer)
    for i in range(len(buffer)):
        lyst[i] = buffer[i]
    print("mergesort sorted list: %s" % lyst)


def merge_sort_helper(lyst, left, right, buffer):
    if left < right:
        middle = (left + right)//2
        merge_sort_helper(lyst, left, middle, buffer)
        merge_sort_helper(lyst, middle+1, right, buffer)
        merge(lyst, left, middle, right, buffer)


def merge(lyst, left, middle, right, buffer):
    i1 = left
    i2 = middle+1
    for i in range(left, right+1):
        if i1 > middle:
            buffer[i] = lyst[i2]
            i2 += 1
        elif i2 > right:
            buffer[i] = lyst[i1]
            i1 += 1
        elif lyst[i1] < lyst[i2]:
            buffer[i] = lyst[i1]
            i1 += 1
        else:
            buffer[i] = lyst[i2]
            i2 += 1


def fib(n):
    if n < 3:
        return 1
    else:
        a1 = 1
        a2 = 1
        count = 3
        while count <= n:
            sum = a1 + a2
            a1 = a2
            a2 = sum
            count += 1
        return sum


def binary_search(target, lyst):
    left = 0
    right = len(lyst) - 1
    while left <= right:
        middle = (left+right)//2
        print(middle, lyst[middle])
        if target == lyst[middle]:
            print("got it , target's index is %s" % middle)
            return middle
        elif target < lyst[middle]:
            right = middle-1
        else:
            left = middle + 1

    print("cannot find the target return -1")









if __name__ == '__main__':
    main()