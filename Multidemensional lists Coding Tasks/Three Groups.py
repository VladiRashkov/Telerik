numbers = list(map(int, input().split(" ")))
zero_remainder_nums = []
one_remainder_nums = []
two_remainder_nums = []
matrix = []
for i in range(len(numbers)):
    if numbers[i] % 3 == 0:
        zero_remainder_nums.append(numbers[i])
    elif numbers[i] % 3 == 1:
        one_remainder_nums.append(numbers[i])
    elif numbers[i] % 3 == 2:
        two_remainder_nums.append(numbers[i])

print(*zero_remainder_nums)
print(*one_remainder_nums)
print(*two_remainder_nums)