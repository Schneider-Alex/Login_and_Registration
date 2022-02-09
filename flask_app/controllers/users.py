from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import user
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def homepage():
    useraccount=False
    if 'id' in session:
        data={
            'id' : session['id']
        }
        useraccount=user.User.get_one(data)
    return render_template('index.html',all_users=user.User.get_all(),useraccount=useraccount)

@app.route('/saveuser', methods=['POST'])
def adduser():
    if not user.User.validate_account(request.form):
        return redirect('/')
    else:
        if request.form['passwordcheck'] !=  request.form['password']:
            flash('passwords do not match!')
            return redirect('/')
        else:
            user.User.save(request.form)
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    useraccount=user.User.loginuser(request.form)
    if bcrypt.check_password_hash(useraccount.password, request.form['password'] ):
        session['id'] = useraccount.id
    else:
        flash('Username or Password Incorrect!')
    
    return redirect('/')

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/')





    # if user.User.loginuser(request.form)
    #     useraccount = user.User.loginuser(requestform)
    #     session['user'] = useraccount.first_name
    #     return redirect('/')
    # else:
    #     if request.form['passwordcheck'] !=  request.form['password']:
    #         flash('passwords do not match!')
    #         return redirect('/')
    #     else:
    #         user.User.save(request.form)
    return redirect('/')