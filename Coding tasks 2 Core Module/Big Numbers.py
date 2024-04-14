array_sizes = list(map(int, input().split()))
array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))

numbers = [0] * max(array_sizes)

carrier = 0
result = 0
a = 0
b = 0

for i in range(max(array_sizes)):
    if i < len(array1):
        a = array1[i]
    else:
        a = 0

    if i < len(array2):
        b = array2[i]
    else:
        b = 0

    result = a + b + carrier

    if result >= 10:
        result %= 10
        numbers[i] = result
        carrier = 1
    else:
        numbers[i] = result
        carrier = 0

print(" ".join(map(str, numbers)))