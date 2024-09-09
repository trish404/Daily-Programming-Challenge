def dutch_national_flag(arr):
    l, m, h = 0, 0, len(arr) - 1

    while m <= h:
        if arr[m] == 0:
            arr[l], arr[m] = arr[m], arr[l]
            l += 1
            m += 1
        elif arr[m] == 1:
            m += 1
        else:  # arr[m] == 2
            arr[h], arr[m] = arr[m], arr[h]
            h -= 1

    return arr

              
arr = list(map(int, input("Enter the array elements: ").split()))

sorted = dutch_national_flag(arr)
print("Result:", sorted)
