def quicksort(arr, level=0):
    indent = "  " * level
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        # 印出目前排序狀態
        print(f"{indent}Level {level}: pivot={pivot}, left={left}, middle={middle}, right={right}")
        sorted_left = quicksort(left, level + 1)
        sorted_right = quicksort(right, level + 1)

        return sorted_left + middle + sorted_right

# 需排序數字列表
numbers = [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]

# 排序並印出過程
sorted_numbers = quicksort(numbers)
print("Sorted numbers:", sorted_numbers)
