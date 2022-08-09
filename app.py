from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

app = Flask(__name__, template_folder='templates', static_folder='static')

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/gun_scrape"
mongo = PyMongo(app)


# @app.route("/")
# def scrape_info():
#     # find one document from our mongo db and return it.    
#     listings = mongo.db.gun_dict.find_one()
#     print(listings)
#     # pass that listing to render_template
#     return render_template("scrape_info.html", listings=listings)

@app.route("/")
def index():
    # find one document from our mongo db and return it.    
    listings = mongo.db.gun_dict.find_one()
    print(listings)
    # pass that listing to render_template
    return render_template("index.html", listings=listings)

@app.route("/index.html")
def index2():
    # find one document from our mongo db and return it.    
    listings = mongo.db.gun_dict.find_one()
    print(listings)
    # pass that listing to render_template
    return render_template("index.html", listings=listings)


@app.route("/map.html")
def map():
    return render_template("map.html")

@app.route("/plots.html")
def plots():
    return render_template("plots.html")


if __name__ == "__main__":
    app.run(debug=True)

