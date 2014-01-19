from flask import render_template, flash, redirect, request
from app import app
from db import connect
import copy
import utils

links = [
    {'title': 'Home', 'view': 'index'},
]

@app.route('/')
@app.route('/index')
def index():
    #top = utils.getTopNHits({'lat': 42, 'lon': -80}, 15, 10)
    #print top
    return render_template('index.html',
            title = 'Home',
            links = links
    )

@app.route('/pictures/new', methods=['POST'])
def addpicture():
    query = 'INSERT INTO `pictures` (`position`, `bearing`, `focus`) VALUES (GeometryFromText(%s), %s, %s);'
    vals = ('POINT(' + request.form['lat'] + ' ' + request.form['lng'] + ')', request.form['bearing'], request.form['focus'])
    connect.execute(query, vals)
    return render_template('common/picture_response.html')
