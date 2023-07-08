from app import app
from model.user_model import use_model
obj = use_model()
@app.route("/add")
def user_signup_controller():
    return obj.user_sign_up()