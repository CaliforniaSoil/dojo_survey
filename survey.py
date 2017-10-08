from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def root():
    return render_template("survey.html")

@app.route('/result', methods=['GET', 'POST'])
def process():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    bobo = request.form['bobo']
    return render_template("result.html", name = name, location = location, language = language, bobo = bobo)
    return redirect("/")



app.run(debug = True)
