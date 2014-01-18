from flask import render_template, flash, redirect
from app import app
#from forms import *
#from db import dbUtils
import copy

links = [
	{'title': 'Home', 'view': 'index'},
]

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Miguel'}
	return render_template("index.html",
		title = 'Home',
		links = links,
		user = user
	)
