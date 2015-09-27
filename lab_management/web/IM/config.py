'''
Created on Aug 31, 2015

@author: wuw7
'''
import os

# DB setting.
CONFIG_DIR = os.path.abspath(os.path.dirname(__file__))
#print CONFIG_DIR
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(CONFIG_DIR, 'data', 'IM.db')