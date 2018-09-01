from flask import Blueprint, request, session, render_template, url_for
from src.models.users.user import User
from werkzeug.utils import redirect
import src.models.users.errors as UserErrors


user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        # Check that login is valid
        email = request.form['email']
        password = request.form['password']

        try:
            if User.is_login_valid(email, password):
                session['email'] = email # session 3:30 = temp store of data (we're putting the email in the session)
                return redirect(url_for(".user_alerts"))
        except UserErrors.UserError as e:
            return e.message

    return render_template("users/login.html") # Send user an error if login is invalid


@user_blueprint.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            if User.register_user(email, password):
                # recap: if the 'register_user' method works, we log them in
                # ... by adding their email to the session -> then redirect to alerts page
                session['email'] = email  # session 3:30 = temp store of data (we're putting the email in the session)
                return redirect(url_for(".user_alerts"))
        except UserErrors.UserError as e:
            return e.message

    return render_template("users/register.html") # Send user an error if login is invalid



@user_blueprint.route('/alerts')
def user_alerts():
    user = User.find_by_email(session['email'])
    alerts = user.get_alerts()
    return render_template('users/alerts.html', alerts=alerts)


@user_blueprint.route('/logout')
def logout_user():
    session['email'] = None
    return redirect(url_for('home'))


@user_blueprint.route('/check_alerts/<string:user_id>')
def check_user_alerts(user_id):
    pass

