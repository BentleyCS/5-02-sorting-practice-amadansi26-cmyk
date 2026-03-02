import random
def bubbleSort(items):
    swaps = 0
    comparisons = 0
    n = len(items)
    sorted = False
    while not(sorted):
        sorted =True
        for j in range(n - 1):
            comparisons += 1
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swaps += 1
                sorted = False

    return items, swaps, comparisons


def insertionSort(items):
    swaps = 0
    comparisons = 0
    n = len(items)

    for i in range(1, n):
        key = items[i]
        j = i - 1

        while j >= 0:
            comparisons += 1
            if items[j] > key:
                items[j + 1] = items[j]
                swaps += 1
                j -= 1
            else:
                break

        items[j + 1] = key

    return items, swaps, comparisons


def selectionSort(items):
    swaps = 0
    comparisons = 0
    n = len(items)

    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            comparisons += 1
            if items[j] < items[min_index]:
                min_index = j


        items[i], items[min_index] = items[min_index], items[i]
        swaps += 1

    return items, swaps, comparisons


# Test code
y = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(bubbleSort(y.copy()))
print(insertionSort(y.copy()))
print(selectionSort(y.copy()))
print()

x = list(range(50))
random.shuffle(x)
print(bubbleSort(x.copy()))
print(insertionSort(x.copy()))
print(selectionSort(x.copy()))
