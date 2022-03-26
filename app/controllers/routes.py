from app import app, render_template

@app.route('/add-user')
def addUser():
    return render_template('addUser.html')

@app.route('/add-vehicle')
def addVehicle():
    return render_template('addVehicle.html')
