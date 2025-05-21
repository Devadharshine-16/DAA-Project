def count_inversions(arr):
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr, 0
        mid = len(arr) // 2
        left, inv_left = merge_sort(arr[:mid])
        right, inv_right = merge_sort(arr[mid:])
        merged, inv_split = merge(left, right)
        total_inv = inv_left + inv_right + inv_split
        return merged, total_inv

    def merge(left, right):
        i = j = inv_count = 0
        merged = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                inv_count += len(left) - i
        merged += left[i:]
        merged += right[j:]
        return merged, inv_count

    _, total = merge_sort(arr)
    return total


# 🌟 USER INPUT SECTION
input_str = input("Enter the elements of the array separated by space: ")
arr = list(map(int, input_str.strip().split()))

inversions = count_inversions(arr)
print("Number of inversions:", inversions)
