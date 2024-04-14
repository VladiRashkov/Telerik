word = input().split()

temp = []
final = []
count = 0

for i in range(len(word)):
    for j in range(len(word)):
        if word[i] == word[j]:
            temp.append(word[i])
            count += 1
            if len(temp) > count:
                final = temp.copy()
            else:
                count = 0
        else:
            temp.clear()

# Print all duplicates found
print(*final)