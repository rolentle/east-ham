from flask import Flask, render_template
from town_name_generator import EnglishTownNameGenerator
app = Flask(__name__)

@app.route('/')
def names():
    names = [ name for name in EnglishTownNameGenerator().generate_times(20)]
    return render_template("names.html", names=names)

if __name__ == "__main__":
    app.run()
