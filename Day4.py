import math

def next_gap(gap):
    if gap <= 1:
        return 0
    return math.ceil(gap / 2)

def merge(arr1, arr2, m, n):
    gap = next_gap(m + n)
    
    while gap > 0:
        i = 0
        while i + gap < m:
            if arr1[i] > arr1[i + gap]:
                arr1[i], arr1[i + gap] = arr1[i + gap], arr1[i]
            i += 1
        
        j = gap - m if gap > m else 0  
        while i < m and j < n:
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]
            i += 1
            j += 1
        
        if j < n:
            j = 0
            while j + gap < n:
                if arr2[j] > arr2[j + gap]:
                    arr2[j], arr2[j + gap] = arr2[j + gap], arr2[j]
                j += 1
        
        gap = next_gap(gap)

arr1 = list(map(int, input("Enter the elements of arr1 ").split()))
arr2 = list(map(int, input("Enter the elements of arr2 ").split()))

m = len(arr1)
n = len(arr2)

merge(arr1, arr2, m, n)

print("arr1 after merge:", arr1)
print("arr2 after merge:", arr2)
