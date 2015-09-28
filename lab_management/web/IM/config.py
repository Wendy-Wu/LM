'''
Created on Aug 31, 2015

@author: wuw7
'''
import os

# DB setting.
CONFIG_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(CONFIG_DIR, 'data', 'imported_files')
EXPORT_FOLDER = os.path.join(CONFIG_DIR, 'static', 'export_file')
#print CONFIG_DIR
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(CONFIG_DIR, 'data', 'IM.db')
