'''
Created on Apr 8, 2016

@author: wuw7
'''
import os, sys
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

# Create Flask instance.
app = Flask(__name__)

# Create DB instance.
db = SQLAlchemy(app)

class Inventory(db.Model):
    __searchable__ = ['tag', 'name']
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    tag = db.Column(db.String(64), index=True)
    name = db.Column(db.String(64), index=True)
    PN = db.Column(db.String(64), index=True)
    SN = db.Column(db.String(64), unique=True, index=True)
    shipping = db.Column(db.String(64))
    capital = db.Column(db.String(64))
    disposition = db.Column(db.String(128))
    status = db.Column(db.String(64), index=True)
    owner = db.Column(db.String(64), db.ForeignKey('user.username'))
    user = db.Column(db.String(64))
    
    def __init__(self, tag, name, pn, sn, ship='', cap='', dis='', sta='available', owner='', user=''):
        self.tag = tag
        self.name = name
        self.PN = pn
        self.SN = sn
        self.shipping = ship
        self.capital = cap
        self.disposition = dis
        self.status = sta
        self.owner = owner
        self.user = user
        
    def __repr__(self):
        return '<Inventory %r:%r>' % (self.id, self.tag)
    
        
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    owned_invs = db.relationship('Inventory', backref='ownerinvs', lazy='dynamic')
   
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password_hash = password
        

db.create_all()
#
inv1 = Inventory( '2000', 'Oberon cDVT system', '100-542-897-03', 'CF2ED142300019', 'FedEx hawb: 609011623649', 'Expense', 'Arrived on 6/27/2014', 'available', 'wendy')
inv2 = Inventory( '2000.1', 'Oberon cDVT SP', '110-297-000A-03', 'CF2CT142300028', 'FedEx hawb: 609011623649', 'Expense', 'Arrived on 6/27/2016', 'available', 'wendy')
inv3 = Inventory( '2000.2', 'Oberon cDVT SP', '110-297-000A-03', 'CF2CT142300034', 'FedEx hawb: 609011623649', 'Expense', 'Arrived on 6/27/2017', 'available', 'wendy')

user1 = User('admin', 'admin@emc.com', 'admin')
user2 = User('wendy', 'wendy@emc.com', 'wendy')

db.session.add(inv1)
db.session.add(inv2)
db.session.add(inv3)
db.session.commit()

db.session.add(user1)
db.session.add(user2)
db.session.commit()

inv1.user = 'admin'
inv2.user = 'admin'
db.session.commit()

print inv1.user
invs = user2.owned_invs.all()
for inv in invs:
    print inv.name