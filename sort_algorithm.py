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











if __name__ == '__main__':
    main()