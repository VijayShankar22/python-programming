def permute(nums):
    if len(nums) == 0:
        return [[]]

    result = []
    for i in range(len(nums)):
        remaining = nums[:i] + nums[i+1:]
        for perm in permute(remaining):
            result.append([nums[i]] + perm)

    return result


input_array = list(map(int, input("Enter integers separated by space: ").split()))

output_permutations = permute(input_array)
print(output_permutations)
