number = int(input())

count = 0
temp = 0
max_count = 0
for i in range(number):
    current_number = int(input())

    if temp != current_number:
        temp = current_number
        count = 1
    else:
        count += 1
        if count > max_count:
            max_count = count

print(max_count)
