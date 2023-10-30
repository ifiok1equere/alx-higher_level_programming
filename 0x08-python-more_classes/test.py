def backtrack(nums, path, result):
    if len(path) == len(nums):
        result.append(path[:])
        return

    for num in nums:
        if num in path:
            continue
        path.append(num)
        backtrack(nums, path, result)
        path.pop()  # Backtrack by removing the last choice

nums = [1, 2, 3]
result = []
backtrack(nums, [], result)
print(result)
