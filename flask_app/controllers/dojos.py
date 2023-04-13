from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo


# main page showing all dojos
@app.route('/dojos')
def show_dojos():
    dojos = Dojo.get_all()
    return render_template('all_dojos.html', dojos=dojos)


# page listing all ninjas in a dojo
@app.route('/dojos/<int:dojo_id>')
def ninjas_by_dojo(dojo_id):
    data = {
        'id': dojo_id
    }
    ninjas = Dojo.get_ninjas_by_dojo(data)
    return render_template('ninjas_by_dojo.html', ninjas=ninjas)


# function for adding new dojo to the db and redirecting to main page
@app.route('/add_dojo', methods=['POST'])
def add_dojo():
    data = {
        'name': request.form['name']
    }
    Dojo.save(data)
    return redirect('/dojos')


# form to create a new ninja
@app.route('/ninjas')
def new_ninja_form():
    dojos = Dojo.get_all()
    print(f"dojos = {dojos}")
    return render_template('new_ninja_form.html', dojos=dojos)
