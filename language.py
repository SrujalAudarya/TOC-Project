class Language:
    def __init__(self, language=None, alphabets=None, rules=None):
        self.language = language if isinstance(language, list) else []
        self.alphabets = alphabets if isinstance(alphabets, list) else []
        self.rules = rules if isinstance(rules, list) else []

    def define(self, strings):
        if isinstance(strings, list):
            self.language.extend(strings)
        else:
            self.language.append(strings)

    def define_alphabets(self, element):
        if isinstance(element, list):
            self.alphabets.extend(element)
        else:
            self.alphabets.append(element)

    def define_rules(self, rule):
        if isinstance(rule, list):
            self.rules.extend(rule)
        else:
            self.rules.append(rule)

    def show(self):
        output = "----------------\n"
        output += "Language: " + str(self.language) + "\n\n"
        output += "Alphabets: " + str(self.alphabets) + "\n\n"
        output += "Rules: " + str(self.rules) + "\n"
        output += "----------------"
        return output

    def show_alphabet(self):
        return self.alphabets

    def get_words(self):
        return self.language