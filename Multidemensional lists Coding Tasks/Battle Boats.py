# output --> print when there is hit "Booom"
# print "Missed" when the target has been missed
# print "You already shot there!" when the target has already been hit.
import sys

command = ""
while True:
    # read the demension of the game
    parameters = list(map(int, input().split(" ")))
    # read only the rows
    first_player_positions = int(parameters[0])
    matrix_player_1 = []
    for i in range(first_player_positions):
        # reading each row and adding it to the nested list
        coordinates_player_1 = list(map(int, input().split(" ")))
        matrix_player_1.append(coordinates_player_1)

    #same here but we reverse the contetn of each row and then the order of all of the rows inside the matrix
    second_player_position = int(parameters[0])
    matrix_player_2 = []
    for j in range(second_player_position):
        coordinates_player_2 = list(map(int, input().split(" ")))
        coordinates_player_2.reverse()
        matrix_player_2.append(coordinates_player_2)
    matrix_player_2.reverse()

    #deciding the turn based on even or odd number
    turn = 0
    # the coordinates of the shot
    first_player_shot = []
    second_player_shot = []

    while True:

        command = input().split(" ")
        if command[0] == "END":
            first_player_lives_remaining = 0
            second_player_lives_remaining = 0

            # going through the matrix to count the 1's
            for first_matrix_row in matrix_player_1:
                for live in range(len(first_matrix_row)):
                    if first_matrix_row[live] == 1:
                        first_player_lives_remaining += 1

            for second_matrix_row in matrix_player_2:
                for live in range(len(second_matrix_row)):
                    if second_matrix_row[live] == 1:
                        second_player_lives_remaining += 1

            print(f"{first_player_lives_remaining}:{second_player_lives_remaining}")
            sys.exit()

        if turn % 2 == 0:
            first_player_shot.append(int(command[1]))
            first_player_shot.append(int(command[2]))

            # checking if the fired shot match with a coordinate of the other player that has a 1,2 or 0
            attempt_player_one = matrix_player_2[first_player_shot[0]][first_player_shot[1]]

            if attempt_player_one == 1:
                matrix_player_2[first_player_shot[0]][first_player_shot[1]] = 2
                first_player_shot.clear()
                print("Booom")
            elif attempt_player_one == 0:
                matrix_player_2[first_player_shot[0]][first_player_shot[1]] = 2
                first_player_shot.clear()
                print("Missed")
            elif attempt_player_one == 2:
                first_player_shot.clear()
                print("You already shot there!")

            turn += 1

        else:
            second_player_shot.append(int(command[1]))
            second_player_shot.append(int(command[2]))

            attempt_player_two = matrix_player_1[second_player_shot[0]][second_player_shot[1]]

            if attempt_player_two == 1:
                matrix_player_1[second_player_shot[0]][second_player_shot[1]] = 2
                second_player_shot.clear()
                print("Booom")
            elif attempt_player_two == 0:
                matrix_player_1[second_player_shot[0]][second_player_shot[1]] = 2
                second_player_shot.clear()
                print("Missed")
            elif attempt_player_two == 2:
                second_player_shot.clear()
                print("You already shot there!")

            turn += 1
