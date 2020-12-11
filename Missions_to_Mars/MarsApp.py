# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 18:46:48 2020

@author: Rob Bowen
"""

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import pymongo
import scrape_mars

app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

MarsData = client

@app.route("/")
def index():
    MarsData = mongo.db.MarsData.find_one()
    return render_template("index.html", MarsData=MarsData)


@app.route("/scrape")
def scraper():
    MarsData = mongo.db.MarsData
    mars_data = scrape_mars.scrape()
    MarsData.update({}, mars_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)