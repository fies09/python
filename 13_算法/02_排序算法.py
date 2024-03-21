#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/5/2 20:16
# @Author     : fany
# @Project    : PyCharm
# @File       : 02_排序算法.py
# @description:
'''
python常见的排序算法有:
 1, 冒泡排序: 重复比较相邻的两个元素,如果前一个比后一个大,则交换它们的位置,直到没有任何一对数字需要比较
 2, 选择排序: 每一次选择最小的数字并将其与序列的最前面的数字,直到整个序列排序完毕
 3, 插入排序: 将待排序序列分为已排序和未排序两部分,每次将未排序的第一个元素插入到已排序的序列中,直到未排序序列为空
 4, 快速排序: 通过一趟排序将待排记录分隔成独立的两部分，其中一部分记录的关键字均比另一部分记录的关键字小，继而分别对这两部分记录进行排序，直到整个序列排好序。
 5, 归并排序: 将待排序的序列分为若干个子序列，每个子序列是有序的，然后再将子序列合并为整体有序序列，即先递归分解序列，再合并子序列。
'''
# 冒泡排序
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

# 选择排序
def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

# 插入排序
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    return lst

# 快速排序
def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# 归并排序
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result