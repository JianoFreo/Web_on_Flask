from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form #form has all the data that the user sent as a login
    print(data)
    return render_template("login.html")

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 20:
            flash('Email must be more than 20 characters', category='error' )
        elif len(firstName) < 2:
            flash('Email must be more than 2 characters', category='error' )
        elif password1 != password2:
            flash('your passwords dont match', category='error' )
        elif len(password1 or password2) < 7:
            flash('password must be more than 7 characters', category='error' )
        else:
            #add user to the database
            flash('account created', category='success' )

        
    return render_template("sign-up.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"




