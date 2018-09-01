from flask import Blueprint, render_template, request, session
from src.models.alerts.alert import Alert
from src.models.items.item import Item


alert_blueprint = Blueprint('alerts', __name__)


@alert_blueprint.route('/')
def index():
    return "This is the alert index"


@alert_blueprint.route('/new', methods=['GET', 'POST'])
def create_alert():
    if request.method == 'POST':
        name = request.form['name']
        url = request.form['url']
        price_limit = request.form['price_limit']

        item = Item(name, url)
        item.save_item_to_mongo()

        alert = Alert(session['email'], price_limit, item._id)
        alert.load_item_price()  # This already saves to MongoDB

    # GET requests?
    return render_template('alerts/create_alert.html')


@alert_blueprint.route('/deactivate/<string:alert_id>')
def deactivate_alert(alert_id):
    pass


@alert_blueprint.route('/<string:alert_id>') #  /alerts/<alert_id>
def get_alert_page(alert_id):
    alert = Alert.find_by_id(alert_id)
    return render_template('alerts/alert.html', alert=alert)


@alert_blueprint.route('/for_user/<string:user_id>')
def get_alerts_for_user(alert_id):
    pass