from flask import Flask, render_template
from waitress import serve
import random

app = Flask(__name__)

# List of dynamic texts
texts = [
    "Logic will get you from A to B. Imagination will take you everywhere.",
    "There are 10 kinds of people. Those who know binary and those who don't.",
    "There are two ways of constructing a software design. One way is to make it so simple that there are obviously no deficiencies and the other is to make it so complicated that there are no obvious deficiencies.",
    "It's not that I'm so smart, it's just that I stay with problems longer.",
    "It is pitch dark. You are likely to be eaten by a grue."
]

@app.route('/')
def index():
    # Get a random dynamic text from the list
    dynamic_text = random.choice(texts)
    return render_template('index.html', dynamic_text=dynamic_text)

if __name__ == '__main__':
    app.run()
    # serve(app, port=8080)
