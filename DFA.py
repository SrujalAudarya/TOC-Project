class DFA:
    def __init__(self, states, alphabet, transitions, initial_state, final_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.final_states = final_states

    def is_string_valid(self, string):
        current_state = self.initial_state
        for letter in string:
            if letter not in self.alphabet or letter not in self.transitions[current_state]:
                return False
            current_state = self.transitions[current_state][letter]
        return current_state in self.final_states