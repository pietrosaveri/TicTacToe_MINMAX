
def possible_new_states(state):
    return [state - take for take in (1, 2, 3) if take <= state]

def evaluate(state, is_maximizing):
    if state == 0:
        return 1 if is_maximizing else -1


def minimax(state, is_maximizing):
    if (score := evaluate(state, is_maximizing)) is not None:
        return score

    if is_maximizing:
        scores = [minimax(new_state, is_maximizing=False) for new_state in possible_new_states(state)]
        return max(scores)
    else:
        scores = [minimax(new_state, is_maximizing=True) for new_state in possible_new_states(state)]
        return min(scores)

def best_move(state):
    return max(
        (minimax(new_state, is_maximizing=False), new_state)
        for new_state in possible_new_states(state)
    )


print(best_move(6))