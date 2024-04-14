n = int(input())
isSymmetric = True
if n == 1:
    print("Yes")
else:
    for i in range(n):
        isSymmetric = True
        numbers = list(map(int, input().split(" ")))
        if len(numbers) == 1:
            print("Yes")
            continue
        for j in range(len(numbers) - 1):
            if numbers[j] != numbers[len(numbers) - j - 1]:
                isSymmetric = False
                break
            else:
                continue

        if isSymmetric:
            print("Yes")
        else:
            print("No")