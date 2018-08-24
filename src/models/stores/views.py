from flask import Blueprint


store_blueprint = Blueprint('store', __name__)


@store_blueprint.route('/store/<string:name>')
def store_page():
    pass


