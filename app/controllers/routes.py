from app import app, render_template, request
from app.models.forms import loginForm


@app.route('/', methods = ['GET', 'POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        if request.form.get('email') == 'admin' and request.form.get('admin'):
            return render_template('dashboard.html', form=form)
        else:
            return render_template('login.html', form=form)
    else: 
        return render_template('login.html', form=form)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/add-user')
def addUser():
    return render_template('addUser.html')

@app.route('/add-vehicle')
def addVehicle():
    return render_template('addVehicle.html')

@app.route('/add-passanger')
def addPassanger():
    return render_template('addPassanger.html')

@app.route('/add-driver')
def addDriver():
    return render_template('addDriver.html')

@app.route('/transport')
def transport():
    return render_template('transport.html')

@app.route('/report')
def report():
    return render_template('report.html')