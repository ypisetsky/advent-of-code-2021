from util import getlines

lines = getlines("old1")
nums = set()
for line in lines:
    val = int(line)
    nums.add(val)

for num1 in nums:
    for num2 in nums:
        if num2 == num1:
            continue
        if 2020 - num1 - num2 in nums:
            print(f"The answer is {num1} {num2} {2020 - num1 - num2} = {num1*num2*(2020-num1-num2)}")