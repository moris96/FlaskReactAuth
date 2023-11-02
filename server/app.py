from flask import Flask, request, abort
from flask.json import jsonify
from flask_bcrypt import Bcrypt
from config import ApplicationConfig
from models import db, User

app = Flask(__name__)
app.config.from_object(ApplicationConfig)

bcrypt = Bcrypt(app)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/register")
def registerUser():
    email = request.jsion["email"]
    password = request.json["password"]

    userExists = User.query.filter_by(email=email).first() is not None 

    if userExists:
        abort(409)
    hashedPassword = bcrypt.generate_password_hash(password)
    newUser = User(email=email)
    db.session.add(newUser)
    db.session.commit()

    return jsonify({
        "id": newUser.id,
        "email": newUser.email
    })


if __name__ == "__main__":
    app.run(debug=True)