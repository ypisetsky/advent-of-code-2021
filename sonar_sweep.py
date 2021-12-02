
# day 1
def solve(lines, window):
    count = 0
    nums = []
    for line in lines:
        nums.append(int(line.strip()))
    for i in range(len(nums) - window):
        if nums[i + window] > nums[i]:
            count += 1
    return count

f = open('data/day1.txt')
lines = f.readlines()
print(f"Solution 1 is {solve(lines, 1)}")
print(f"Solution 2 is {solve(lines, 3)}")
