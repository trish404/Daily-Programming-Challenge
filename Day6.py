def find_zero_sum_subarrays(arr):
    subarrays = []
    prefix_sum = 0
    prefix_sum_map = {}

    for i in range(len(arr)):
        prefix_sum += arr[i]

        if prefix_sum == 0:
            subarrays.append((0, i))

        if prefix_sum in prefix_sum_map:
            for start_index in prefix_sum_map[prefix_sum]:
                subarrays.append((start_index + 1, i))

        if prefix_sum not in prefix_sum_map:
            prefix_sum_map[prefix_sum] = []
        prefix_sum_map[prefix_sum].append(i)

    return subarrays

arr = list(map(int, input("Enter the array elements: ").split()))
print(find_zero_sum_subarrays(arr))
