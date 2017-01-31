from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route('/')
def register():
    return render_template('index.html')


def main():
    app.run(host='localhost', port=8080)

if __name__ == "__main__":
    main()
