from flask import Flask, render_template, request, redirect, url_for, flash
import os
import json
import random


# initialise Users database
app = Flask(__name__)
usersdb = {}
with open('users.json') as fp:
    usersdb = json.load(fp)


# initialise Items dtabase
app = Flask(__name__)
itemsdb = {}
with open('items.json') as fp:
    itemsdb = json.load(fp)


# Secret key for flash messages
app = Flask(__name__)
app.secret_key = b'laksdfoi323d'

# function to save users
def save_users():
    with open('users.json', 'w') as fp:
        json.dump(usersdb, fp)

# function to save items
def save_items():
    with open('items.json', 'w') as fp:
        json.dump(itemsdb, fp)


@app.route('/')
def home():
    return render_template('home.template.html')


@app.route('/register')
def register():
    return render_template('register.template.html')


@app.route('/login')
def login():
    return render_template('login.template.html')


@app.route('/browse-items')
def browse_items():
    return render_template('browse_items.template.html', all_items=itemsdb)


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            # only one program can run on one port, therefore flask gives error if it is run 2nd time
            port=int(os.environ.get('PORT')),
            debug=True)
