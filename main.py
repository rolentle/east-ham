from nltk.tokenize.sonority_sequencing import SyllableTokenizer
import random
import re
from flask import Flask, render_template

class Corpus():
    def __init__(self, tokenizer=SyllableTokenizer):
        self.file_name = "./town_names.txt"
        self.tokenizer = tokenizer()

    def generate_corpus(self):
        f = open(self.file_name, "r")
        return [self.tokenize(x) for x in f]

    def tokenize(self, name):
        return self.tokenizer.tokenize(name.strip())

class EnglishTownNameGenerator():
    def __init__(self, corpus=Corpus):
        self.corpus = Corpus().generate_corpus()

    def generate_times(self, n=10):
        return [self.generate() for _ in range(n)]

    def generate(self, recursive=True):
        town_name_syllables = []
        current_syllable_index = 0
        random_town = random.choice(self.corpus)
        while len(random_town) > current_syllable_index:
            syllable = random_town[current_syllable_index]
            town_name_syllables.append(syllable)
            if re.search("\W+", syllable) and recursive:
                town_name_syllables.append(self.generate(recursive=False))
            elif syllable == random_town[-1]:
                break

            current_syllable_index += 1
            random_town = random.choice(self.corpus)

        return "".join(town_name_syllables)


app = Flask(__name__)

@app.route('/')
def names():
    names = [ name for name in EnglishTownNameGenerator().generate_times(100)]
    return render_template("names.html", names=names)

