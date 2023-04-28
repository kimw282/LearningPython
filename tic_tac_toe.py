row1 = [" ", "|", " ", "|", " ", "\n-----\n"]
row2 = [" ", "|", " ", "|", " ", "\n-----\n"]
row3 = [" ", "|", " ", "|", " "]

tic_tac_toe = [row1, row2, row3]


i = 0
stop_flag = False
while not stop_flag:
    player_input = input("Input [x y] coordinates in the range [0-2]: ").split()
    n = 0
    while n < len(player_input):
        player_input[n] = int(player_input[n])
        n += 1

    if i % 2 == 0:
        if tic_tac_toe[player_input[1]][player_input[0]*2] == " ":
            tic_tac_toe[player_input[1]][player_input[0]*2] = "X"
        else:
            print("\nAlready filled :(\n")
            continue
    else:
        if tic_tac_toe[player_input[1]][player_input[0]*2] == " ":
            tic_tac_toe[player_input[1]][player_input[0]*2] = "O"
        else:
            print("\nAlready filled :(\n")
            continue
    n = 0
    while n < 3:
        if tic_tac_toe[0][n*2] == tic_tac_toe[1][n*2] == tic_tac_toe[2][n*2] != " ":
            print(f"\n{tic_tac_toe[0][n*2]} wins!")
            stop_flag = True
            break
        elif tic_tac_toe[n][0] == tic_tac_toe[n][2] == tic_tac_toe[n][4]!= " ":
            print(f"\n{tic_tac_toe[n][0]} wins!")
            stop_flag = True
            break
        elif tic_tac_toe[0][0] == tic_tac_toe[1][2] == tic_tac_toe[2][4] != " ":
            print(f"\n{tic_tac_toe[0][0]} wins!")
            stop_flag = True
            break
        elif tic_tac_toe[0][4] == tic_tac_toe[1][2] == tic_tac_toe [2][0] != " ":
            print(f"\n{tic_tac_toe[0][4]} wins!")
            stop_flag = True
            break
        elif ((" " not in tic_tac_toe[0]) and (" " not in tic_tac_toe[1]) and 
              (" " not in tic_tac_toe[2])):
            print("\nDraw")
            stop_flag = True
            break
        n += 1
    i += 1
    tic_tac_toe_joined = [''.join(row1), ''.join(row2), ''.join(row3)]
    print("\n", ''.join(tic_tac_toe_joined), "\n", sep='')