from flask import Blueprint


alert_blueprint = Blueprint('alerts', __name__)


@alert_blueprint.route('/')
def index():
    return "This is the alert index"


@alert_blueprint.route('/new', methods=['POSTS'])
def create_alert():
    pass


@alert_blueprint.route('/deactivate/<string:alert_id>')
def deactivate_alert(alert_id):
    pass


@alert_blueprint.route('/alert/<string:alert_id>')
def get_alert_page(alert_id):
    pass


@alert_blueprint.route('/for_user/<string:user_id>')
def get_alerts_for_user(alert_id):
    pass