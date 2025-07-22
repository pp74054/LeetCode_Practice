# [Better Approach 1] Sorting and Binary Search - O(n*log(n)) time and O(1) space

def binarySearch(arr, left, right, target):
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

def twoSum(arr, target):
    arr.sort()  # Sort the array first
        
    for i in range(len(arr)):
        complement = target - arr[i]
        if binarySearch(arr, i + 1, len(arr) -1, complement):
            return True  # Found a pair that sums to target
    
    return False  # No pair found

if __name__ == "__main__":
    arr = [0, -1, 2, -3, 1]
    target = -2
    result = twoSum(arr, target)
    if result:
        print("True")
    else:
        print("False")