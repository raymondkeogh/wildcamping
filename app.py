import os
import requests
import json
import cloudinary
import cloudinary.uploader
import cloudinary.api
import logging
from flask import Flask,render_template, request, jsonify
from cloudinary.utils import cloudinary_url
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for, jsonify)
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv

if os.path.exists("env.py"):
    import env

load_dotenv()

app = Flask(__name__)
CORS(app)
logging.basicConfig(level=logging.DEBUG)
app.logger.info('%s',os.getenv('CLOUD_NAME'))
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
app.api_key = os.environ.get("GOOGLE_MAP_KEY")
app.geocode_api_key = os.environ.get("GEOCODE_API_KEY")
mongo = PyMongo(app)

cloudinary.config(
    cloud_name = os.environ.get('CLOUD_NAME'),
    api_key=os.environ.get('CLOUD_API_KEY'), 
    api_secret=os.environ.get('CLOUD_API_SECRET'))


@app.route("/")
@app.route("/home_page")
def home_page():
    return render_template("index.html")


@app.route("/get_locations", methods=["GET", "POST"])
def get_locations():
    location_api = f"https://maps.googleapis.com/maps/api/js?key={app.api_key}&callback=initMap&libraries=&v=weekly"
    locations = mongo.db.locations.find()
    # reverse_geo = f"https://maps.googleapis.com/maps/api/geocode/json?latlng=40.714224,-73.961452&key={app.api_key}" 
    # Code used to get coordinates from search address 
    # https://developer.here.com/documentation/geocoding-search-api/dev_guide/topics/endpoint-geocode-brief.html

    URL = "https://geocode.search.hereapi.com/v1/geocode"
    api_key = {app.geocode_api_key} # Acquire from developer.here.com
    errors = []
    geosearch_data = {}
    nearpoints = {}

    if request.method == "POST":
        # get url that the user has entered
        search = request.form['search']
        PARAMS = {'apikey': api_key, 'q': search}
        r = requests.get(url = URL, params = PARAMS) 
        # r = request.POST.get(url = URL, params = PARAMS) 
        geosearch_data = r.json()
        latitude = geosearch_data['items'][0]['position']['lat']
        longitude = geosearch_data['items'][0]['position']['lng']
        mongo.db.locations.create_index([("location", "2dsphere")])
        nearpoints = mongo.db.locations.find(
            {"location":
                {"$near":
                    {"$geometry":
                        {"type": "Point", "coordinates":
                            [longitude, latitude]}, "$maxDistance": 50000}}})
        # coordinates(nearpoints)
        return render_template(
        "locations.html", locations=locations, location_api=location_api, nearpoints=nearpoints, geosearch_data=geosearch_data)
      
    return render_template(
        "locations.html", locations=locations, location_api=location_api, nearpoints=nearpoints)


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
                return render_template("profile.html")
            else:
                # incorrect passord
                flash("Username or Password incorrect, Please try again")
                return redirect(url_for("login"))
        else:
            flash("Username or Password incorrect, Please try again")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/profile_page/<username>", methods=["GET", "POST"])
def profile_page(username):
    # grab the session user's username from db
    user = mongo.db.users.find_one(
        {"username": session["user"]})
    print(username)
    # locations = mongo.db.locations.find(
    #     {"username": session["user"]})
    if session["user"]:
        return render_template(
            "profile.html", user=user)
    else:
        return redirect(url_for("login"))


@app.route("/edit_profile", methods=["GET", "POST"])
def edit_profile():
    user = mongo.db.users.find_one(
        {"username": session["user"]})
    if request.method == 'POST':
        # Upload file to Cloudinary
        app.logger.info('in upload route')
        cloudinary.config(
            cloud_name=os.getenv('CLOUD_NAME'),
            api_key=os.getenv('CLOUD_API_KEY'),
            api_secret=os.getenv('CLOUD_API_SECRET'))
        upload_result = None
        if request.method == 'POST':
            file_to_upload = request.files['file']
            app.logger.info('%s file_to_upload', file_to_upload)
            if file_to_upload:
                upload_result = cloudinary.uploader.upload(file_to_upload)
                app.logger.info(upload_result)
                app.logger.info(type(upload_result))
        profile_update = {
            "username": session["user"],
            "bio": request.form.get("bio"),
            "file": upload_result["url"],
        }
        mongo.db.users.update({"username": session["user"]}, profile_update)

        flash("Profile updated")


        return render_template(
            "profile.html", user=user)
    return render_template("edit_profile.html", user=user)


@app.route("/profile_page/<username>/user_locations")
@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/user_location", methods=["GET", "POST"])
def user_location():
    user_location_api = f"https://maps.googleapis.com/maps/api/js?key={app.api_key}&callback=initUserMap&libraries=&v=weekly"
    if request.method == "POST":
        # Upload file to Cloudinary
        app.logger.info('in upload route')
        cloudinary.config(
            cloud_name=os.getenv('CLOUD_NAME'),
            api_key=os.getenv('CLOUD_API_KEY'),
            api_secret=os.getenv('CLOUD_API_SECRET'))
        upload_result = None
        if request.method == 'POST':
            file_to_upload = request.files['file']
            app.logger.info('%s file_to_upload', file_to_upload)
            if file_to_upload:
                upload_result = cloudinary.uploader.upload(file_to_upload)
                app.logger.info(upload_result)
                app.logger.info(type(upload_result))

        lat = float(request.form.get("lat"))
        lng = float(request.form.get("lng"))
        new_location = {
            "name": request.form.get("location_name"),
            "description": request.form.get("location_description"),
            "rating": request.form.get("rating"),
            "location": {"type": "Point", "coordinates": [lng, lat]},
            "file": upload_result["url"],
            "posted_by": session["user"]
        }
        mongo.db.locations.insert_one(new_location)

        flash("Location Added, Thanks for you input")
        return render_template("profile.html")
    return render_template(
        "user_location.html", user_location_api=user_location_api)

# https://stackoverflow.com/questions/49718569/multiple-markers-in-flask-google-map-api
@app.route("/api/coordinates")
def coordinates():
    addresses = mongo.db.locations.find()
    all_coords = []  # initialize a list to store addresses
    for add in addresses:
        address_details = {
            "lng": add["location"]["coordinates"][0],
            "lat": add["location"]["coordinates"][1] 
        }
        all_coords.append(address_details)
    return jsonify({'coordinates': all_coords})

# Attempt to get like button to update the db with locaiton id
# @app.route("/likes", methods=['GET', 'POST'])
# def result():
#     if request.method == "POST":
#         likes = request.get_json()
#         mongo.db.users.update({"username": session["user"]}, {"$push": {"locations": likes}})
#         return jsonify({likes})

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
