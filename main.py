from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///datebase/bode.db'
db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200))
    referencia = db.Column(db.String(200))
    ubicacion = db.Column(db.String(200))
    done = db.Column(db.Boolean)




@app.route("/login", methods=['POST'])
def login():
    user = request.form['user']
    password = request.form['pass']

    return render_template('dashboard.html')

    #if (user == 'admin' and password =='1234'):
        #render_template('dashoard.html')

@app.route("/")
def dashboard():
    tasks = Task.query.all()
    return render_template('dashboard.html', tasks=tasks)

@app.route("/create" , methods=['POST'])
def createproduct():
    task = Task(nombre=request.form['nombre'], referencia=request.form['referencia'], ubicacion=request.form['ubicacion'], done=False)
    db.session.add(task)
    db.session.commit()
    return redirect(url_for('dashboard'))


   

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80, debug=False)