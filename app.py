from flask import Flask, render_template, jsonify, redirect, session, url_for, request , flash, make_response
from os import environ as env
from pymongo import MongoClient
import pymongo
import requests
from flask_pymongo import PyMongo

# Database
client = pymongo.MongoClient(
    ""
)
database = client["Main"]
db_test = database["Test_sites"]
db_food = database["Food_distribution"]
db_book = database["Book"]
db_anime = database["Anime"]
db_manga = database["Manga"]
db_games = database["Games"]
db_youtube = database["Youtube"]

app = Flask(__name__, static_url_path="")
app.debug = True

@app.route("/")
def home():
    return render_template("/index.html")

@app.route("/testsites")
def test_sites():
    testsites = db_test.find()
    return render_template("/testsites.html", testsites=testsites)

@app.route("/fooddistribution")
def food():
    food = db_food.find()
    return render_template("/food.html", food=food)

@app.route("/book")
def book():
    book = db_book.find()
    return render_template("/book.html", book=book)

@app.route("/anime")
def anime():
    anime = db_anime.find()
    return render_template("/anime.html", anime=anime)

@app.route("/manga")
def manga():
    manga = db_manga.find()
    return render_template("/manga.html", manga=manga)

@app.route("/games")
def games():
    games = db_games.find()
    return render_template("/games.html", games=games)

@app.route("/youtube")
def youtube():
    youtube = db_youtube.find()
    return render_template("/youtube.html", youtube=youtube)

