from flask import Flask, render_template
from town_name_generator import Corpus,EnglishTownNameGenerator
app = Flask(__name__)

@app.route('/')
def names():
    town_name_corpus = Corpus(file_name="./town_names.txt")
    npc_name_corpus = Corpus(file_name="./names.txt")
    names = [ name for name in EnglishTownNameGenerator(town_name_corpus).generate_times(20)]
    npc_names = [ npc_name for npc_name in EnglishTownNameGenerator(npc_name_corpus).generate_times(20)]
    return render_template("names.html", names=names, npc_names=npc_names)

if __name__ == "__main__":
    app.run()
