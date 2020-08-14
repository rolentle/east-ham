from nltk.tokenize.sonority_sequencing import SyllableTokenizer
import random


class EnglishTownNameGenerator():
    def __init__(self, file_name="./town_names.txt", tokenizer=SyllableTokenizer):
        self.tokenizer = tokenizer()
        self.file_name = file_name
        self.corpus = self.generate_corpus()

    def generate_times(self, n=10):
        return [self.generate() for _ in range(n)]

    def generate(self):
        town_name = []
        current_syllable = 0
        random_town = random.choice(self.corpus)
        while len(random_town) > current_syllable:
            syllable = random_town[current_syllable]
            town_name.append(syllable)
            current_syllable += 1
            random_town = random.choice(self.corpus)

        return "".join(town_name)

    def generate_corpus(self):
        f = open(self.file_name, "r")
        return [self.tokenize(x) for x in f]

    def tokenize(self, name):
        return self.tokenizer.tokenize(name.strip())


if __name__ == "__main__":
    for name in EnglishTownNameGenerator().generate_times(100):
        print(name)
