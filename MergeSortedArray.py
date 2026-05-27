

def reverse_array(arr): # this is a function with "arr: as a parameter
    n = len(arr)
    #means find the number of elements in the array arr and store that value in the variable n
    for i in range(n // 2):  # Loop only halfway
        #When reversing an array, we need to swap the first element with the last element, the second element with the second-last element, and so on.

        arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]  # Swap elements # [n-1] because n - 1 is the index of the last element
                                                        #As i increases in the loop, n - 1 - i accesses the next element from the end, moving backward in the array.
    return arr  # Return the reversed array


def merge_arrays(arr1,arr2):

    return sorted(arr1 + arr2)


def main():
    my_array = [1, 2, 3, 4, 5]
    my_array2 = [6,7,8,9,10]


    reversed_array = reverse_array(my_array)
    print(reversed_array)  # Output: [5, 4, 3, 2, 1]


    reversed_array2 = reverse_array(my_array2)
    print(reversed_array2)  # Output: [5, 4, 3, 2, 1]

    print(merge_arrays(reversed_array, reversed_array2))


main()  # Directly calling main()
