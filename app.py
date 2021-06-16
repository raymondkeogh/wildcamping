import os
import requests
import json
import cloudinary
import cloudinary.uploader
import cloudinary.api
import logging
from flask import Flask, render_template, request, jsonify
from cloudinary.utils import cloudinary_url
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for, jsonify)
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv
from bson import ObjectId
from itertools import tee

if os.path.exists("env.py"):
    import env

load_dotenv()
app = Flask(__name__)
CORS(app)
logging.basicConfig(level=logging.DEBUG)
app.logger.info('%s', os.getenv('CLOUD_NAME'))
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
app.api_key = os.environ.get("GOOGLE_MAP_KEY")
app.geocode_api_key = os.environ.get("GEOCODE_API_KEY")
mongo = PyMongo(app)

# details for picture upload service
cloudinary.config(
    cloud_name=os.environ.get('CLOUD_NAME'),
    api_key=os.environ.get('CLOUD_API_KEY'),
    api_secret=os.environ.get('CLOUD_API_SECRET'))

# Home page


@app.route("/")
@app.route("/home_page")
def home_page():
    locations = mongo.db.locations.find().limit(6)
    location_api = f"https://maps.googleapis.com/maps/api/js?key={app.api_key}&callback=searchResultMap&libraries=&v=weekly"
    random_location = mongo.db.locations.aggregate(
        [{"$sample": {"size": 1}}])
    return render_template(
        "index.html", random_location=random_location,location_api=location_api, locations=locations)

# Search results page / locations.html
@app.route("/get_locations", methods=["GET", "POST"])
def get_locations():
    location_api = f"https://maps.googleapis.com/maps/api/js?key={app.api_key}&callback=searchResultMap&libraries=&v=weekly"

    locations = mongo.db.locations.find()
    # Code used to get coordinates from search address
    # https://developer.here.com/documentation/geocoding-search-api/dev_guide/topics/endpoint-geocode-brief.html
    URL = "https://geocode.search.hereapi.com/v1/geocode"
    api_key = {app.geocode_api_key}  # Acquire from developer.here.com
    errors = []
    geosearch_data = {}
    nearpoints = mongo.db.locations.find()

    if request.method == "POST":
        # get url that the user has entered
        search = request.form['search']
        PARAMS = {'apikey': api_key, 'q': search}
        r = requests.get(url=URL, params=PARAMS)
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
                            [longitude, latitude]}, "$maxDistance": 100000}}})

        search_count = nearpoints.count()
        return render_template(
            "locations.html", search_count=search_count, locations=locations, location_api=location_api, nearpoints=nearpoints, geosearch_data=geosearch_data)

    search_count = locations.count()
    return render_template("locations.html", search_count=search_count, nearpoints=nearpoints, locations=locations, location_api=location_api)


# Renders Json data of locations from Database
# https://stackoverflow.com/questions/49718569/multiple-markers-in-flask-google-map-api
@app.route("/api/coordinates")
def coordinates(addresses=mongo.db.locations.find()):
    all_coords = []  # initialize a list to store addresses
    for add in addresses:
        address_details = {
            "lng": add["location"]["coordinates"][0],
            "lat": add["location"]["coordinates"][1]
        }
        all_coords.append(address_details)

    return jsonify({'coordinates': all_coords})


# Sign up funtion
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
        user = mongo.db.users.find_one(
            {"username": session["user"]})
        return render_template(
            "profile.html", user=user)
        flash("Registration Successful!")
    return render_template("signup.html")


# Login function
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
                return redirect(url_for("profile_page", user=existing_user))
            else:
                # incorrect passord
                flash("Username or Password incorrect, Please try again")
                return redirect(url_for("login"))
        else:
            flash("Username or Password incorrect, Please try again")
            return redirect(url_for("login"))
    return render_template("login.html")


# Profile page
@app.route("/profile_page", methods=["GET", "POST"])
def profile_page():
    user = mongo.db.users.find_one(
        {"username": session["user"]})
    liked_locations = mongo.db.locations.find({"liked_by": session["user"]})
    posted_locations = mongo.db.locations.find({"posted_by": session["user"]})
    popularity = mongo.db.locations.aggregate(
        [{"$match": {
            "posted_by": session["user"]}}, {
            "$group": {
                "_id": "null",
                "sum": {"$sum": "$liked_count"}}}])
    posted_count = posted_locations.count()
    my_liked_count = liked_locations.count()
    return render_template("profile.html", user=user, liked_locations=liked_locations, popularity=popularity, posted_locations=posted_locations, posted_count=posted_count, my_liked_count=my_liked_count)


@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))

@app.route("/map_search", methods=["POST"])
def map_search():
    
    return ('', 204)



# Input new custom loctions for user
@app.route("/user_location", methods=["GET", "POST"])
def user_location():
    # user_location_api = f"https://maps.googleapis.com/maps/api/js?key={app.api_key}&callback=initAutocomplete&libraries=&v=weekly"


    location_api = f"https://maps.googleapis.com/maps/api/js?key={app.api_key}&callback=initAutocomplete&libraries=places&v=weekly"
    user = mongo.db.users.find_one(
        {"username": session["user"]})
    location = request.args.get("location_id")
    db_location = mongo.db.locations.find_one({"_id": ObjectId(location)})

    if request.method == "POST":
        # Upload file to Cloudinary
        app.logger.info('in upload route')
        cloudinary.config(
            cloud_name=os.getenv('CLOUD_NAME'),
            api_key=os.getenv('CLOUD_API_KEY'),
            api_secret=os.getenv('CLOUD_API_SECRET'))
        upload_result = None
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
            "posted_by": session["user"],
            "liked_by": [],
            "liked_count": 0
        }

        if db_location == None:
            mongo.db.locations.insert_one(new_location)
        else:
            mongo.db.locations.update(
                {"_id": ObjectId(location)}, new_location)
        flash("Location Added, Thanks for you input")

        return redirect(url_for("profile_page", user=user, location_id=db_location))
    else:
        return render_template(
            "user_location.html", location_id=db_location, user=user, location_api=location_api)


# Take location_id and action from location cards and add like/unlike to db
# Inspiration from https://github.com/LigaMoon/swap-clothes-app/blob/main/app.py
@app.route('/liked_item/<location_id>/<action>')
def likes(location_id, action):
    user = session['user']
    if action == 'like':
        mongo.db.locations.update_one({"_id": ObjectId(location_id)},
                                      {'$push': {'liked_by': user},
                                       '$inc': {'liked_count': 1}})

    # Takes user from locations like_by array
    elif action == 'unlike':
        mongo.db.locations.update_one({"_id": ObjectId(location_id)},
                                      {'$pull': {'liked_by': user},
                                       '$inc': {'liked_count': -1}})
    return redirect(request.referrer)


# Delete post from DB
@app.route('/delete_post/<location>')
def delete_post(location):
    user = session['user']
    mongo.db.locations.remove({"_id": ObjectId(location)})
    return redirect(url_for("profile_page"))


# Opens up location in its own window
@app.route('/view_location/<location_id>')
def view_location(location_id):
    location_api = f"https://maps.googleapis.com/maps/api/js?key={app.api_key}&callback=searchResultMap&libraries=&v=weekly"
    location = mongo.db.locations.find_one({"_id": ObjectId(location_id)})
    return render_template("view_location.html", location_id=location, location_api=location_api)


# Allows for seperate uploads of photos whether updating profile or creating new one
@app.route('/upload_image/<location>', methods=["GET", "POST"])
def upload_image(location):
    profile_request = "https://8080-amethyst-crow-u769d91j.ws-eu09.gitpod.io/profile_page"
    profile_request_heroku = "https://wild-camping.herokuapp.com/profile_page"

    if (request.referrer == profile_request or request.referrer == profile_request_heroku):
        db_location = mongo.db.users.find_one({"_id": ObjectId(location)})
    else: 
        db_location = mongo.db.locations.find_one({"_id": ObjectId(location)})
    user = mongo.db.users.find_one(
        {"username": session["user"]})
    user_location_api = f"https://maps.googleapis.com/maps/api/js?key={app.api_key}&callback=initAutocomplete&libraries=&v=weekly"
    if request.method == "POST":
        # Upload file to Cloudinary
        app.logger.info('in upload route')
        cloudinary.config(
            cloud_name=os.getenv('CLOUD_NAME'),
            api_key=os.getenv('CLOUD_API_KEY'),
            api_secret=os.getenv('CLOUD_API_SECRET'))
        upload_result = None
        file_to_upload = request.files['file']
        app.logger.info('%s file_to_upload', file_to_upload)
        if file_to_upload:
            upload_result = cloudinary.uploader.upload(file_to_upload)
            app.logger.info(upload_result)
            app.logger.info(type(upload_result))
        if (request.referrer == profile_request):
            mongo.db.users.update_one({"_id": ObjectId(location)}, {
                                      "$set": {"file": upload_result["url"]}})

            return redirect(url_for("profile_page"))
        else:
            mongo.db.locations.update_one({"_id": ObjectId(location)}, {
                                          "$set": {"file": upload_result["url"]}})
            return ('', 204)

    return render_template("edit_location.html", location_id=db_location, user=user, user_location_api=user_location_api)


# Edit user created locations
@app.route('/edit_location/<location>', methods=["GET", "POST"])
def edit_location(location):
    user = mongo.db.users.find_one(
        {"username": session["user"]})
    # user_location_api = f"https://maps.googleapis.com/maps/api/js?key={app.api_key}&callback=initAutocomplete&libraries=&v=weekly"

    location_api = f"https://maps.googleapis.com/maps/api/js?key={app.api_key}&callback=initAutocomplete&libraries=places&v=weekly"
  
    db_location = mongo.db.locations.find_one({"_id": ObjectId(location)})
    if request.method == "POST":
        lat = float(request.form.get("lat"))
        lng = float(request.form.get("lng"))
        new_location = {
            "name": request.form.get("location_name"),
            "description": request.form.get("location_description"),
            "rating": request.form.get("rating"),
            "location": {"type": "Point", "coordinates": [lng, lat]},
            "posted_by": session["user"]
        }
        mongo.db.locations.update_one(
            {"_id": ObjectId(location)}, {"$set": new_location})
        flash("Location Updated!")
        return redirect(url_for("profile_page"))
    else:
        return render_template("edit_location.html", location_id=db_location, user=user, location_api=location_api)


# 404 Page
# https://stackoverflow.com/questions/29516093/how-to-redirect-to-a-external-404-page-python-flask
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
