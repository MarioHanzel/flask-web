from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "loves contributing to ScoreLab."

if __name__ == "__main__":
    app.run(debug=True)
