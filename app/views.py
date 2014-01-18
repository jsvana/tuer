from flask import render_template, flash, redirect, request
from app import app
from db import connect
import copy

links = [
    {'title': 'Home', 'view': 'index'},
    {'title': 'Map', 'view': 'map'},
]

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}
    return render_template('index.html',
            title = 'Home',
            links = links,
            user = user
    )

@app.route('/maps')
def map():
    return render_template('maps/index.html',
        title = 'Map',
        links = links,
    )

@app.route('/pictures/new', methods=['POST'])
def addpicture():
    query = 'INSERT INTO `pictures` (`position`, `bearing`, `focus`) VALUES (GeometryFromText(%s), %s, %s);'
    vals = ('POINT(' + request.form['lat'] + ' ' + request.form['lng'] + ')', request.form['bearing'], request.form['focus'])
    connect.execute(query, vals)
    return render_template('common/picture_response.html')
