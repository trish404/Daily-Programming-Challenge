def find_duplicate(arr):
    slow = arr[0]
    fast = arr[0]
    
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break
    
    slow = arr[0]
    
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    
    return slow

def input_array():
    n = int(input("Enter the value of n: "))
    print(f"Enter {n+1} integers in the range [1, {n}]:")
    arr = list(map(int, input().split()))
    
    if len(arr) != n + 1:
        print(f"Error")
        return None
    
    return arr

def main():
    arr = input_array()
    
    if arr is not None:
        duplicate = find_duplicate(arr)
        print(f"Duplicate number: {duplicate}")

if __name__ == "__main__":
    main()
