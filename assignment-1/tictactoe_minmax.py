import math
import copy

def check_winner(state):
    # check rows
    for i in range(3):
        if state[i][0] == state[i][1] == state[i][2] and state[i][0] != 0:
            return state[i][0]

    # check columns
    for j in range(3):
        if state[0][j] == state[1][j] == state[2][j] and state[0][j] != 0:
            return state[0][j]

    # check diagonals
    if state[0][0] == state[1][1] == state[2][2] and state[0][0] != 0:
        return state[0][0]
    if state[0][2] == state[1][1] == state[2][0] and state[0][2] != 0:
        return state[0][2]

    return 0

def check_tie(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return False
    return True

def terminal_node(state):
    result = check_winner(state)
    if result != 0:
        return {"gameover": True, "result": result}
    if check_tie(state):
        return {"gameover": True, "result": 0}
    return {"gameover": False, "result": 0}

def expand_state(state):
    children = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                child = [i, j]
                children.append(child)
    return children

def minimax(state, depth, isMaxPlayer):
    if depth == 0 or terminal_node(state)["gameover"]:
        return terminal_node(state)["result"], None

    if isMaxPlayer:
        v_max = -math.inf
        best_move = None
        for pos in expand_state(state):
            child = copy.deepcopy(state)
            child[pos[0]][pos[1]] = 1
            v, _ = minimax(child, depth - 1, not isMaxPlayer)
            if v > v_max:
                v_max = v
                best_move = pos
        return v_max, best_move

    else:
        v_min = math.inf
        best_move = None
        for pos in expand_state(state):
            child = copy.deepcopy(state)
            child[pos[0]][pos[1]] = -1
            v, _ = minimax(child, depth - 1, not isMaxPlayer)
            if v < v_min:
                v_min = v
                best_move = pos
        return v_min, best_move

def output_state(state):
    print("This is the state:")
    for row in state:
        print(row)

def player_ply(depth):
    def get_valid_input(prompt):
        while True:
            user_input = input(prompt)
            if user_input.isdigit() and 0 <= int(user_input) <= 2:
                return int(user_input)
            else:
                print("Invalid input. Please input again.")

    def notify_player(state):
        output_state(state)
        print("Please input your move in x-coordinate and y-coordinate.")
        print("The range of the input is (0-2), (0-2). For example, (0,0) is the top left corner.")

    while True:
        notify_player(state)

        move_x = get_valid_input("Please input the x-coordinate: ")
        move_y = get_valid_input("Please input the y-coordinate: ")

        if state[move_y][move_x] != 0:
            print("Invalid move, cell is occupied. Please try again.")
        else:
            state[move_y][move_x] = 1
            print(f"Player chooses the move {move_x}, {move_y}")
            break

    return depth - 1

def bot_ply(depth):
    v, move = minimax(state, depth, isMaxPlayer)
    output_state(state)
    result = "a tie" if v == 0 else "a win" if v == 1 else "a defeat"
    print(f"The bot chooses {move[1]}, {move[0]} as the current move, with expected result: {result}")
    state[move[0]][move[1]] = -1

    return depth - 1

state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
depth = 9
isMaxPlayer = True

while True:
    player_result = check_winner(state)
    if player_result == 1:
        print("Player wins!")
        break
    elif check_tie(state):
        print("It's a tie!")
        break
    else:
        depth = player_ply(depth)

    bot_result = check_winner(state)
    if bot_result == -1:
        print("Bot wins!")
        break
    elif check_tie(state):
        print("It's a tie!")
        break
    else:
        depth = bot_ply(depth)