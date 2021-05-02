import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home_page")
def home_page():
    return render_template("index.html")


@app.route("/get_locations")
def get_locations():
    locations = mongo.db.locations.find()
    return render_template("locations.html", locations=locations)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return render_template("signup.html")

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check if username already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        
        if existing_user:
            # Check user password
            if check_password_hash(
                existing_user["password"], request.form.get("password")): 
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
            
            else:
                # incorrect passord
                flash("Username or Password incorrect, Please try again")
                return redirect(url_for("login"))

        else:
            flash("Username or Password incorrect, Please try again")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/profile_page")
def profile_page():
    user = mongo.db.users.find()
    locations = mongo.db.locations.find()
    return render_template("profile.html", locations=locations, user=user)


@app.route("/add_location", methods=["GET", "POST"])
def add_location():
    if request.method == "POST":
        lat = request.form.get("lat")
        lng = request.form.get("lng")
        latlng = lat + ", " + lng
        new_location = {
            "name": request.form.get("location_name"),
            "description": request.form.get("location_description"),
            "rating": request.form.get("rating"),
            "location": latlng
        }
        mongo.db.locations.insert_one(new_location)

        flash("Location Added, Thanks for you input")
        return render_template("profile.html")
    return render_template("add_location.html")

    
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
