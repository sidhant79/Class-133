from flask import Flask
app= Flask(__name__)
@app.route('/')

def first_flask():
    return '1 time using flask Program'

@app.route("/flask2")

def second_flask():
    return "second time using flask program"

@app.route("/flask3")
def third_flask():
    return "Python"

app.run(debug=True)