from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'
@app.route('/dojo')
def dojo():
    return 'Dojo!'
@app.route('/say/<name>')
def hi(name):
    print(name)
    return f'Hi  {name.capitalize()}! '
@app.route('/repeat/<int:int>/<string:word>')
def repeat(int, word):
    return f"{word * int}"

if __name__ == "__main__":
    app.run(debug=True)