from flask import Flask, render_template, request, redirect, url_for
from Apartment import Apartment
from Locker import Locker
from Package import Package
from Tenant import Tenant

app = Flask(__name__)

apartments = []
lockers = []

@app.route('/')
def index():
    return render_template('index.html', apartments=apartments, lockers=lockers)

@app.route('/add_apartment', methods=['POST'])
def add_apartment():
    apartment_number = request.form['apartment_number']
    apartments.append(Apartment(apartment_number))
    return redirect(url_for('index'))

@app.route('/add_tenant', methods=['POST'])
def add_tenant():
    apartment_number = request.form['apartment_number']
    tenant_name = request.form['tenant_name']
    phone_number = request.form['phone_number']
    for apt in apartments:
        if apt.apartment_number == apartment_number:
            apt.add_tenant(Tenant(tenant_name, apt, phone_number))
            break
    return redirect(url_for('index'))

@app.route('/add_package', methods=['POST'])
def add_package():
    apartment_number = request.form['apartment_number']
    package_height = request.form['package_height']
    tracking_number = request.form['tracking_number']
    for apt in apartments:
        if apt.apartment_number == apartment_number:
            package = Package(package_height, apt, tracking_number)
            # Store package in a locker (assuming a simple locker logic for now)
            for locker in lockers:
                locker.store_package(package)
                break
    return redirect(url_for('index'))

@app.route('/create_locker', methods=['POST'])
def create_locker():
    num_modules = int(request.form['num_modules'])
    locker_width = float(request.form['locker_width'])
    overall_height = float(request.form['overall_height'])
    column = request.form['column']
    lockers.append(Locker(num_modules, locker_width, overall_height, column))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
