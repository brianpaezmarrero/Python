from flask_app import app
from flask_app.controllers import dojos_controller
from flask_app.controllers import ninjas_controller


if __name__ == '__main__':
    app.run(debug=True)