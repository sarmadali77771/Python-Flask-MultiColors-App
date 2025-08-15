from flask import Flask, render_template
import random
import os

app = Flask(__name__)

def random_color():
    # Generate a random hex color
    return f"#{random.randint(0, 0xFFFFFF):06x}"

@app.route('/')
def index():
    color = random_color()
    return render_template('index.html', bg_color=color)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=os.getenv('FLASK_DEBUG', False))
