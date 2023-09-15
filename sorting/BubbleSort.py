def bubble_sort(elements):
    size = len(elements)

    for i in range(size-1):
        swapped = False   #if the array is already sorted, this will make the TC O(n)
        for j in range(size-1-i): # -i will make sure that it does not travers the sorted elements
            if elements[j] > elements[j+1]:
                temp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = temp
                swapped = True
        if not swapped:
            break


if __name__ == '__main__':
    elements = [2,5,7,5,9,1,0]

    bubble_sort(elements)
    print(elements)