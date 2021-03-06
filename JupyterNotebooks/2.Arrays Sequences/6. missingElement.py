# Find the missing element which is deleted from the array

def finder(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1

    return arr1[-1]


if __name__ == '__main__':
    arr1 = [1, 2, 3, 4, 5, 6, 7]
    arr2 = [3, 7, 2, 1, 4, 6]

    finder(arr1, arr2)
