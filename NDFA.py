class NDFA:
    def __init__(self, states, alphabet, transitions, initial_state, final_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.final_states = final_states

    def is_string_valid(self, string):
        def dfs(state, index):
            if index == len(string):
                return state in self.final_states
            if state not in self.transitions:
                return False
            letter = string[index]
            next_states = self.transitions[state].get(letter, [])
            return any(dfs(s, index + 1) for s in next_states)

        return dfs(self.initial_state, 0)
