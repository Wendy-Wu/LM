'''
Created on Aug 31, 2015

@author: wuw7
'''
from IM import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    full_name = db.Column(db.String(64), unique=False, index=True)
    group = db.Column(db.Integer, unique=False, index=True)
    active = db.Column(db.Integer, unique=False, index=True)
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password_hash = password
        
    def __repr__(self):
        return '<User %r>' % (self.username)

    def verify_password(self, password):
        if self.password_hash != password:
            return False
        else:
            return True
        
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
    user = db.relationship('User')
    
    
    def __init__(self, tag, name, pn, sn, ship, cap, dis, sta, owner=''):
        self.tag = tag
        self.name = name
        self.PN = pn
        self.SN = sn
        self.shipping = ship
        self.capital = cap
        self.disposition = dis
        self.status = sta
        self.owner = owner
    
    def __repr__(self):
        return '<Inventory %r:%r>' % (self.PN, self.SN)
    
    def to_json(self):
        return{
               'id':self.id,
               'SN':self.SN,
               'PN':self.PN,
               'tag':self.tag
               }
    
class Borrows(db.Model):   
    borrow_id = db.Column(db.Integer, primary_key=True)   
    username = db.Column(db.String(64), db.ForeignKey('user.username'))
    user = db.relationship('User')
    inventory_id = db.Column(db.Integer, db.ForeignKey('inventory.id'))
    inventory = db.relationship('Inventory')
    borrow_date = db.Column(db.String(64))
    return_date = db.Column(db.String(64))
    
class RequestMessage():
    username = ''
    inv_id = ''
    operation = ''
    owner = ''
    date = ''
    message_id = ''

    def __init__(self, username, inv_id, operation, owner, date):
        self.username = username
        self.inv_id = inv_id
        self.operation = operation
        self.owner = owner
        self.date = date
        self.message_id = username+inv_id+date
        
    def __repr__(self):
        return '%r Message: %r %r inventory %r from %r at %r' % (self.message_id, self.username, self.operation, self.inv_id, self.owner, self.date)
    
    
class ResponseMessage():
    message_id = 'Response:'
    owner = ''
    inv_id = ''
    handle_operation = ''
    username = ''
    date = ''
    
    def __init__(self, request_message, handle_operation, date):
        self.message_id += request_message.message_id
        self.owner = request_message.owner
        self.inv_id = request_message.inv_id
        self.handle_operation = handle_operation
        self.username = request_message.username
        self.date = date
        
    def __repr__(self):
        return '%r Message: %r %r %r requested by %r at %r' % (self.message_id, self.owner, self.handle_operation, self.inv_id, self.username, self.date)
    
        