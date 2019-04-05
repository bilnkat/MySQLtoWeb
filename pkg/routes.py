from flask import render_template, request
from pkg import app
from pkg.models import Computer

comps = Computer.query.all()



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', comps = comps)

@app.route("/", methods=['POST'])
def search():
    search = request.form['search']
    processed_search = search.upper()
    return processed_search