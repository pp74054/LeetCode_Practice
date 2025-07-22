# [Native Approach] Generating all Possible Pairs Time Complexity: O(n^2) time, Space Complexity: O(1) space
# [Better Approach 1] sorting the array and using two pointers Time Complexity: O(n log n) time, Space Complexity: O(1) space 
# [Better Approach 2] Sorting and Two-Pointer Technique - 0(n *log n) time, O(1) space
# [Expected Approach] Using Hash Set - O(n) time and O(n) space

def twoSum(arr, target):
    n = len(arr)
    for i in range(n):
        # For each Element, arr[i], check every other element arr[j] to find the target sum
        for j in range(i + 1, n):
            # Check if the sum of the current pair
            # equals the target
            if arr[i] + arr[j] == target:
                #return [i, j]
                  return True
    # If no pair is found after checking
    # all possibilities
    return False

if __name__ == "__main__":
    arr = [0, -1, 2, -3, 1]
    target = -2
    result = twoSum(arr, target)
    if result:
        print("True")
    else:
        print("False")
        