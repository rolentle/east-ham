from flask import Flask, render_template
from name_generator import Corpus, NameGenerator
app = Flask(__name__)

@app.route('/')
def names():
    town_name_corpus = Corpus(file_name="./corpora/town_names.txt")
    names = [ name for name in NameGenerator(town_name_corpus).generate_times(20)]

    welsh_town_name_corpus = Corpus(file_name="./corpora/welsh_town_names.txt")
    welsh_names = [ welsh_name for welsh_name in NameGenerator(welsh_town_name_corpus).generate_times(20)]

    npc_name_corpus = Corpus(file_name="./corpora/names.txt")
    npc_names = [ npc_name for npc_name in NameGenerator(npc_name_corpus).generate_times(20)]

    return render_template("names.html", names=names, welsh_names=welsh_names,npc_names=npc_names)

if __name__ == "__main__":
    app.run()
