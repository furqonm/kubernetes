from flask import Flask
from flask import render_template
import os

app = Flask(__name__)

word = os.environ.get('WORD')

@app.route("/")

def main():
    return render_template('index.html', name=socket.gethostname(), content=word)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")
