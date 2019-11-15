from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "superdupeseeeecret!"

@app.route('/')
def index():
    if 'answer' not in session:
        session['answer'] = random.randint(1,101)
    print("*"*80)
    print(session['answer'])
    print("*"*80)
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    session['user_guess'] = int(request.form['user_guess'])
    if session['answer'] == session['user_guess']:
        session['result'] = "win"
    elif session['answer'] > session['user_guess']:
        session['result'] = "higher"
    else:
        session['result'] = "lower"
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)