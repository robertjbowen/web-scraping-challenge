# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 18:46:48 2020

@author: Rob Bowen
"""

from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

app = Flask(__name__)

# Create connection to the pymongo instance.
client = pymongo.MongoClient('mongodb://localhost:27017')

# Create a Database
db = client["Mars_db"]


@app.route("/")
def index():
    MarsData = db.MarsData.find_one()
    return render_template("index.html", MarsData=MarsData)


@app.route("/scrape")
def scraper():
    MarsData = db.MarsData
    mars_data = scrape_mars.scrape()
    MarsData.update({}, mars_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)