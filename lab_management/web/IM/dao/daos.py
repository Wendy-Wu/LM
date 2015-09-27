'''
Created on Aug 31, 2015

@author: wuw7
'''
from IM import db
from model.models import User, Inventory, Borrows

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
    def add_inventory(tag, name, PN, SN, shipping, capital, disposition, status):
        inv = Inventory(tag, name, PN, SN, shipping, capital, disposition, status)
        db.session.add(inv)
        db.session.commit()
        return Inventory.query.filter_by(SN=SN).first()
        
    