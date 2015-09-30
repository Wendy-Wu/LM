'''
Created on Aug 31, 2015

@author: wuw7
'''
from IM import db
from model.models import User, Inventory, Borrows
import traceback

# User DAO
class UserDao():
    '''
    This class is used to orginaze the User Dao operations.
    '''
    
    @staticmethod
    def get_all_users():
        '''
        Created on 2015-4-24
        @author: wange14
        @summary: Get all users.
        @return: User object list.
        '''
        return User.query.all()
    
    @staticmethod
    def delete_a_user(name):
        return True
        
    @staticmethod
    def search_a_user(name):
        return User.query.filter_by(username = name).first()
    
    @staticmethod
    def login(name, password):
        user = UserDao.search_a_user(name)
        print user
        if user:
            print user.verify_password(password)
            return user.verify_password(password)
        else:
            return False
    

class InvDao():
    
    @staticmethod
    def get_all_invs():
        return Inventory.query.all()
    
    @staticmethod
    def add_inventory(tag, name, PN, SN, shipping, capital, disposition, status, owner=''):
        '''need try catch exception or just check if unique'''
        inv = Inventory(tag, name, PN, SN, shipping, capital, disposition, status, owner)
        try:
            db.session.add(inv)
            db.session.commit()
            return inv
        except:
            return None
        
    @staticmethod
    def delete_inventory(ids):
        invs=[]
        for an_id in ids:
            invs.append(InvDao.search_inventory_by_id(an_id))
        print invs
        try:
            for inv in invs:
                db.session.delete(inv)
                db.session.commit()
            return True
        except:
            return False
        
    @staticmethod
    def search_inventory_by_id(search_id):
        return Inventory.query.filter_by(id = search_id).first()
    
    @staticmethod
    def search_inventory(search_string):
        try:
            results = Inventory.query.whoosh_search('Eruption')
        except Exception:
            traceback.print_exc()

        print results.all()
        return results.all()
        
        
    