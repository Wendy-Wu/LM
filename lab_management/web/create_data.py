'''
Created on Aug 31, 2015

@author: wuw7
'''

from IM import db
from IM.model.models import *

#db.create_all()
#
#user1 = User('admin3', 'admin3@emc.com', 'admin3')
#user2 = User('wendy3', 'wendy3@emc.com', 'wendy3')
##
#inv1 = Inventory( '2000', 'Oberon cDVT system', '100-542-897-03', 'CF2ED142300019', 'FedEx hawb: 609011623649', 'Expense', 'Arrived on 6/27/2014', 'ok', 'wendy')
#inv2 = Inventory( '2000.1', 'Oberon cDVT SP', '110-297-000A-03', 'CF2CT142300028', 'FedEx hawb: 609011623649', 'Expense', 'Arrived on 6/27/2016', 'ok', 'wendy')
#inv3 = Inventory( '2000.2', 'Oberon cDVT SP', '110-297-000A-03', 'CF2CT142300034', 'FedEx hawb: 609011623649', 'Expense', 'Arrived on 6/27/2017', 'ok', 'wendy')
#
#db.session.add(inv1)
#db.session.add(inv2)
#db.session.add(inv3)
#db.session.commit()
#
#db.session.add(user1)
#db.session.add(user2)
#db.session.commit()
invs = Inventory.query.all()
print invs[2].id

users = User.query.all()
print users
