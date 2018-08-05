from flask import Flask, render_template, request, redirect, session, flash
import re
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "AD555C03B3B8892327A7D8E58F5BD133734A67CDEDDFAF600E86C7A3EBD2EBCC"

@app.route('/')
def index(): 
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create():
# store session, should probably store in flash?? could use a loop here?
    arr =["'lang'", "'loc'", "'name'", "'message'"]
    for i in (request.form):
        session[i] = request.form[i]

# check that all fields are filled out
    session['redo'] = 0
    if len(request.form) < 4:
        flash("please complete entire form")
        session['redo'] =1
    if len(request.form['name']) < 1:
        flash("Please input a name")
        session['redo'] =1
    if not NAME_REGEX.match(request.form['name']):
        flash("Please use only english characters")
        session['redo'] =1
    if len(request.form['message']) >119:
        flash("Comments have a 120 character limit")
        session['redo'] =1
        
# return to valhala!
    if session['redo'] == 1:
        return redirect('/')
# clear each session until we master flash!
    session.clear();
    return render_template("result.html")

@app.route('/back')
def default():
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)

