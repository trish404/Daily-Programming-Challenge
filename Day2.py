def find_missing_number(arr):
    n = len(arr) + 1  
    total = n * (n + 1) // 2  
    arr_sum = sum(arr)  
    num = total - arr_sum  
    return num


inp = list(map(int, input("Enter the array elements: ").split()))

result = find_missing_number(inp)
print(f"The missing number is: {result}")
