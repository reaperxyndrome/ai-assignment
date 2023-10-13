import math
import copy

def check_winner(state):
    # check rows
    for i in range(3):
        if state[i][0] == state[i][1] == state[i][2] and state[i][0] != 0:
            if state[i][0] == 1:
                return 10
            elif state[i][0] == -1:
                return -10
            
    # check columns
    for j in range(3):
        if state[0][j] == state[1][j] == state[2][j] and state[0][j] != 0:
            if state[0][j] == 1:
                return 10
            elif state[0][j] == -1:
                return -10

    # check diagonals
    if state[0][0] == state[1][1] == state[2][2] and state[0][0] != 0:
        if state[0][0] == 1:
            return 10
        elif state[0][0] == -1:
            return -10
    if state[0][2] == state[1][1] == state[2][0] and state[0][2] != 0:
        if state[0][2] == 1:
            return 10
        elif state[0][2] == -1:
            return -10
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
                child = [i,j]
                children.append(child)
    # print(children)
    return children


def minimax(state, depth, isMaxPlayer):
    global count_terminal
    if depth == 0 or terminal_node(state)["gameover"]: 
        count_terminal += 1 
        return terminal_node(state)["result"], None, count_terminal

    if isMaxPlayer:
        v_max = -math.inf
    else:
        v_min = math.inf

    children = expand_state(state)
    best_move = None

    for pos in children:
        child = copy.deepcopy(state)
        child[pos[0]][pos[1]] = 1 if isMaxPlayer else -1
        # child[pos[1]][pos[0]] = 1 if isMaxPlayer else -1
        
        v, _, count_terminal = minimax(child, depth - 1, not isMaxPlayer)

        if isMaxPlayer and v > v_max:
            v_max = v
            best_move = pos
        elif not isMaxPlayer and v < v_min:
            v_min = v
            best_move = pos

    return (v_max, best_move, count_terminal) if isMaxPlayer else (v_min, best_move, count_terminal)

def output_state(state):
    print(f"This is the state:")
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
        print("Please input the your play in x-coordinate and y-coordinate.")
        print("The range of the input is (0-2), (0-2). For example, (0,0) is the top left corner.")

    while True:
        notify_player(state)

        move_x = get_valid_input("Please input the x-coordinate: ")
        move_y = get_valid_input("Please input the y-coordinate: ")
        
        if state[move_y][move_x] != 0:
            print("Invalid move, cell is occupied. Please try again.")
        else:
            state[move_y][move_x] = 1
            print(f"Player chooses the move {move_x, move_y}")
            break
    
    return depth - 1

def bot_ply(depth):
    global count_terminal
    v, move, count_terminal = minimax(state, depth, isMaxPlayer)
    output_state(state)
    print(f"The bot computes {count_terminal} ways this game could end.")
    result = "a tie" if v == 0 else "a win" if v == -10 else "a defeat"
    print(v)
    print(f"The bot chooses {move} as the current move, with expected result: {result}")
    state[move[1]][move[0]] = -1
    count_terminal = 0

    return depth - 1

count_terminal = 0
state = [[0,0,0],[0,0,0],[0,0,0]]
depth = 9
isMaxPlayer = True

while True:
    print(check_winner(state))
    if check_winner(state) == 10:
        print("Player wins!")
        break
    elif check_tie(state):
        print("It's a tie!")
        break
    else:
        depth = player_ply(depth)
    print(check_winner(state))
    if check_winner(state) == -10:
        print("Bot wins!")
        break
    elif check_tie(state):
        print("It's a tie!")
        break
    else:
        depth = bot_ply(depth)
