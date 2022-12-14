import sys

n = int(input())
biggest_num = -sys.maxsize
nums_sum = 0

for number in range(n):
    num = int(input())
    nums_sum += num
    if num > biggest_num:
        biggest_num = num

other_nums = nums_sum - biggest_num
if biggest_num == other_nums:
    print("Yes")
    print(f"Sum = {biggest_num}")
else:
    print("No")
    print(f"Diff = {abs(biggest_num - other_nums)}")