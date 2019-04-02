from flask import render_template
from pkg import app
from pkg.models import Computer

comps = Computer.query.all()



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', comps = comps)

@app.route("/about")
def about():
    return render_template('about.html')