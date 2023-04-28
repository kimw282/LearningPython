row1 = [" ", "|", " ", "|", " ", "\n-----\n"]
row2 = [" ", "|", " ", "|", " ", "\n-----\n"]
row3 = [" ", "|", " ", "|", " "]

tic_tac_toe = [row1, row2, row3]

key = '''
Cell Guide:

0 0 | 1 0 | 2 0
---------------
0 1 | 1 1 | 2 1
---------------
0 2 | 1 2 | 2 2

    '''


i = 0
stop_flag = False
print(key)
while not stop_flag:
    player_input = input("Input [x y] coordinates or \"help\": ").split()
    n = 0
    while n < len(player_input):
        try:
            player_input[n] = int(player_input[n])
        except ValueError:
            break
        n += 1

    if isinstance(player_input[0], str):
        if player_input[0].lower() == "help":
            print(key)
            continue
        if player_input[0].lower() == "quit":
            exit()

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
        n += 1
    if ((" " not in tic_tac_toe[0]) and (" " not in tic_tac_toe[1]) and 
              (" " not in tic_tac_toe[2])) and not stop_flag:
            print("\nDraw")
    i += 1
    tic_tac_toe_joined = [''.join(row1), ''.join(row2), ''.join(row3)]
    print("\n", ''.join(tic_tac_toe_joined), "\n", sep='')