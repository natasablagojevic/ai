"""iz intervala [-1, 1]"""
def evaluate(current_state):
    pass
def Max(current_state, alfa=float('-inf'), beta=float('inf')):
    if end(current_state):
        return evaluate(current_state), current_state

    best_value = float('-inf')
    best_move = None

    for next_state in get_next_states(current_state):
        opponent_best_value, _ = Min(current_state, alpha, beta)

        if opponent_best_value > best_value:
            best_value = opponent_best_value
            best_move = next_state

        if opponent_best_value >= beta:
            return best_value, best_move

        if opponent_best_value > alpha:
            alpha = opponent_best_value

    return best_value, best_move

def Min(current_state, alpha=float('-inf'), beta=float('inf')):
    if end(current_state):
        return evaluate(current_state), current_state

    best_value = float('inf')
    best_move = None

    for next_state in get_next_states(current_state):
        opponent_best_value, _ = Max(next_state, alpha, beta)

        if opponent_best_value < best_value:
            best_value = opponent_best_value
            best_move = next_state

        if opponent_best_value <= alpha:
            return best_value, best_move

        if opponent_best_value < beta:
            beta = opponent_best_value

    return best_value, best_move

if __name__ == '__main__':
    pass