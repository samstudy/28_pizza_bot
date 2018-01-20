from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from create_db import URI, Pizza, Option


class AuthException():
    def __init__(self, message):
        super().__init__(message, Response(
            "You could not be authenticated. Please refresh the page.", 401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'}))


class MyModelView(ModelView):
    def check_auth(self, username, password):
        return username == os.getenv('username') and
        password == os.getenv('password')

    def is_accessible(self):
        auth = request.authorization
        if not auth or not self.check_auth(auth.username, auth.password):
            raise AuthException('Not authenticated.')
        return True


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = URI
app.config['SECRET_KEY'] = 'mysecret'
db = SQLAlchemy(app)
admin = Admin(app)
admin.add_view(ModelView(Pizza, db.session))
admin.add_view(ModelView(Option, db.session))


if __name__ == '__main__':
    app.run()
