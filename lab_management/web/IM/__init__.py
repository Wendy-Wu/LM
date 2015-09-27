'''
Created on Aug 31, 2015

@author: wuw7
'''
import os, sys
from flask import Flask, _app_ctx_stack
from flask.ext.sqlalchemy import SQLAlchemy
from config import CONFIG_DIR

# Create Flask instance.
app = Flask(__name__)

# Loading flask config.
sys.path.append(CONFIG_DIR)
app.config.from_object('config')

# Create DB instance.
db = SQLAlchemy(app)
