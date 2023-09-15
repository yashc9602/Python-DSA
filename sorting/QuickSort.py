# Hoare partition - start ele is pivot
# lomuto partition - end ele is pivot

def swap(a,b,arr):
    if a!=b:
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp

def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start<end:
        while start < len(elements)  and elements[start] <= pivot:
            start += 1

        while elements[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)

    return end


def quick_sort(elements, start, end):
    if start< end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi-1)
        quick_sort(elements, pi+1, end)


if __name__ == '__main__':
    elements = [2,5,7,5,9,1,0]

    quick_sort(elements, 0, len(elements)-1)
    print(elements)



# avg TC = O(nlogn)
# worst TC = O(n^2)