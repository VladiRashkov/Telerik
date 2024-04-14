# size 1 -> takes the argument from the number it has steped on, skiping a single number
# size 2 -> same, but skipping two numbers
# if the array ends, start from the beginning
# calculate the sum when stepping forward, and seperarately when stepping backawards

start = int(input())

numbers = list(map(int, input().split(",")))

command = ""

sum_forward = 0
sum_backwards = 0

current_position = start

while command != "exit":
    entry = input().split(" ")
    if entry[0] == "exit":
        command = "exit"
        continue
    move_times = int(entry[0])
    direction = entry[1]
    size_step = int(entry[2])


    for _ in range(move_times):
        if direction == "forward":
            current_position = (current_position + size_step) % len(numbers)
            sum_forward += numbers[current_position]

        elif direction == "backwards":
            current_position = (current_position - size_step) % len(numbers)
            sum_backwards += numbers[current_position]

print(f"Forward: {sum_forward}")
print(f"Backwards: {sum_backwards}")