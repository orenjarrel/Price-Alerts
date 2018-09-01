from src.common.database import Database
from flask import Flask, render_template


app = Flask(__name__)
app.config.from_object('config')
app.secret_key = "123"


@app.before_first_request
def init_db():
    Database.initialize()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/test')
def home2():
    return render_template('home2.html')


from src.models.users.views import user_blueprint
from src.models.alerts.views import alert_blueprint
from src.models.stores.views import store_blueprint

app.register_blueprint(user_blueprint, url_prefix="/users")
app.register_blueprint(alert_blueprint, url_prefix="/alerts")
app.register_blueprint(store_blueprint, url_prefix="/stores")
