from src.app import app

__author__ = 'orenj'


app.run(debug=app.config['DEBUG'], port=5000)
