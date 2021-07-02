from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object('project.config.Config')
db = SQLAlchemy(app)
ma = Marshmallow(app)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, email):
        self.email = email


class UserSchema(ma.Schema):
    class Meta:
        model = User
        fields = ('id', 'email', 'active')
        # sqla_session = db.session


userSchema = UserSchema()


@app.route("/")
def hello_world():
    return jsonify(hello='world')


@app.route("/users")
def user_list():
    user = User.query.first()
    return userSchema.dump(user)
