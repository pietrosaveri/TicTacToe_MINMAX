def minimax(state, max_turn):
    if state == 0:
        return 1 if max_turn else -1
    
    possible_new_states = [state - take for take in (1, 2, 3) if take <= state]
    #print("possible: ", possible_new_states)

    if max_turn:
        scores = [minimax(new_state, max_turn=False)for new_state in possible_new_states]
        #print("scores max", scores)
        return max(scores)
    else:
        scores = [minimax(new_state, max_turn=True)for new_state in possible_new_states]
        #print("scores min", scores)
        return min(scores)
    

print(minimax(4, max_turn=False))