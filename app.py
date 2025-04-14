from flask import Flask, render_template, request
from DFA import DFA
from NDFA import NDFA
from Mealy import Mealy
from Moore import Moore
from language import Language

app = Flask(__name__)

# Initialize Automata
dfa = DFA(
    ['q0', 'q1'], ['a', 'b'],
    {'q0': {'a': 'q1', 'b': 'q0'}, 'q1': {'a': 'q0', 'b': 'q1'}},
    'q0', ['q1']
)

ndfa = NDFA(
    ['q0', 'q1'], ['a', 'b'],
    {'q0': {'a': ['q0', 'q1'], 'b': ['q1']}, 'q1': {'a': ['q0'], 'b': ['q1']}},
    'q0', ['q1']
)

mealy = Mealy(
    ['a', 'b', 'c', 'd'], ['a', 'b'], ['0', '1'],
    {
        'a': {'a': ('d', '1'), 'b': ('b', '0')},
        'b': {'a': ('a', '1'), 'b': ('d', '1')},
        'c': {'a': ('c', '0'), 'b': ('c', '0')},
        'd': {'a': ('b', '0'), 'b': ('a', '1')}
    }, 'a'
)

moore = Moore(
    ['q0', 'q1', 'q2', 'q3'], ['a', 'b'], ['0', '1'],
    {
        'q0': {'a': 'q1', 'b': 'q3'},
        'q1': {'a': 'q3', 'b': 'q1'},
        'q2': {'a': 'q0', 'b': 'q3'},
        'q3': {'a': 'q3', 'b': 'q2'}
    }, 'q0',
    {'q0': '1', 'q1': '0', 'q2': '0', 'q3': '1'}
)

# Create a global Language instance
lang = Language()

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    word = ""
    selected_fa = ""
    alphabet = []
    language_summary = ""

    if request.method == "POST":
        word = request.form.get("word")
        selected_fa = request.form.get("fa_type")

        if word:
            alphabet = sorted(list(set(word)))
            lang.define(word)
            lang.define_alphabets(alphabet)

            if selected_fa == "dfa":
                result = dfa.is_string_valid(word)
            elif selected_fa == "ndfa":
                result = ndfa.is_string_valid(word)
            elif selected_fa == "mealy":
                try:
                    result = mealy.get_output_from_string(word)
                except:
                    result = "Invalid input for Mealy"
            elif selected_fa == "moore":
                try:
                    result = moore.get_output_from_string(word)
                except:
                    result = "Invalid input for Moore"

            language_summary = lang.show()

    return render_template("index.html", word=word, fa_type=selected_fa, result=result,
                           alphabet=alphabet, language_summary=language_summary)

if __name__ == "__main__":
    app.run(debug=True)
