from flask_app import app
from flask import redirect, request
from flask_app.models.ninja import Ninja


# method to make a new ninja and redirect to that dojo's page
@app.route('/add_ninja', methods=['POST'])
def new_ninja():
    data = {
        'dojo_id': request.form['dojo_id'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age']
    }
    Ninja.save(data)
    return redirect('/dojos/' + str(data['dojo_id']))
