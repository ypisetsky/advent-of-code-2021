from util import tokenedlines
data = [x[0] for x in tokenedlines("old9")]
print(f"{data}")

def is_good(prevs, current):
    for i in range(len(prevs)):
        for j in range(i + 1, len(prevs)):
            if current == prevs[i] + prevs[j]:
                return True
    return False

def find_violator(nums, stride):
    for i in range(stride, len(nums)):
        if not is_good(nums[i - stride:i], nums[i]):
            print(f"i: {i} num: {nums[i]} violates")
            for j in range(i):
                k = j
                s = nums[k]
                while s < nums[i]:
                    k += 1
                    s += nums[k]
                if s == nums[i]:
                    print(f"range is {j} - {k}")
                    print(f"min is {min(nums[j:k+1])} max is {max(nums[j:k+1])}")
                    print(f"{min(nums[j:k+1])+max(nums[j:k+1])}")

find_violator(data, 25)
