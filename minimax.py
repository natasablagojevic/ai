def evaluate(current_state):
    pass

def Min(current_state):
    if end(current_state):
        return evaluate(current_state), current_state

    current_best_value = float('inf')
    best_move = None

    for next_state in get_next_states(current_state):
        opponent_best_value = Max(current_state)

        if opponent_best_value < current_best_value:
            current_best_value = opponent_best_value
            best_move = next_state

    return current_best_value, next_state

def Max(current_state):
    if end(current_state):
        return evaluate(current_state), current_state

    current_best_value = float('-inf')
    best_move = None

    for next_state in get_next_states(current_state):
        opponent_best_value = Max(current_state)

        if opponent_best_value > current_best_value:
            current_best_value = opponent_best_value
            best_move = next_state

    return current_best_value, next_state
