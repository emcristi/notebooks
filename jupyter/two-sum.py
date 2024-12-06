import random
import time

def generateArray(l=10000, target=8):
    a=[]
    for i in range(l):
        a.append(random.randrange(1000) + 10000)
    a[-2] = 2
    a[-1] = target - 2
    print(f"Generated an array with length = {len(a)}")
    return a


def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target:
                print(f"{target} is a sum of indexes {i} and {j}")
                return

target=9
start = time.perf_counter()
arr = generateArray(6000,target)
twoSum(arr, target)
elapsed = time.perf_counter() - start
print(f"----Done in {elapsed:.3f} seconds----")