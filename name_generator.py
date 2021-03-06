from nltk.tokenize.sonority_sequencing import SyllableTokenizer
import random
import re

class Corpus():
    def __init__(self, file_name="./town_names.txt", tokenizer=SyllableTokenizer):
        self.file_name = file_name
        self.tokenizer = tokenizer()

    def generate_corpus(self):
        f = open(self.file_name, "r")
        return [self.tokenize(x) for x in f]

    def tokenize(self, name):
        return self.tokenizer.tokenize(name.strip())

class NameGenerator():
    def __init__(self, corpus):
        self.corpus = corpus.generate_corpus()

    def generate_times(self, n=10):
        return [self.generate() for _ in range(n)]

    def generate(self, recursive=True):
        town_name_syllables = []
        current_syllable_index = 0
        random_town = random.choice(self.corpus)

        while len(random_town) > current_syllable_index:
            syllable = random_town[current_syllable_index]
            if current_syllable_index > 0 and re.search(r"^[A-Z]", syllable):
                town_name_syllables.append(" ")

            town_name_syllables.append(syllable)

            if re.search(r"\W+", syllable) and recursive:
                town_name_syllables.append(self.generate(recursive=False))
            elif syllable == random_town[-1]:
                break

            current_syllable_index += 1
            random_town = random.choice(self.corpus)

        return "".join(town_name_syllables)
