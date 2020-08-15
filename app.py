from flask import Flask, render_template
from town_name_generator import Corpus,EnglishTownNameGenerator
app = Flask(__name__)

@app.route('/')
def names():
    names = [ name for name in EnglishTownNameGenerator().generate_times(20)]
    npc_names = [ name for name in EnglishTownNameGenerator(Corpus(file_name="./names.txt")).generate_times(20)]
    return render_template("names.html", names=names, npc_names=npc_names)

if __name__ == "__main__":
    app.run()
