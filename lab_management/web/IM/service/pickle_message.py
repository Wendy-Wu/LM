'''
Created on Sep 24, 2015

@author: wuw7
'''
from model.models import *
import cPickle as pickle
import datetime

def add_request_msg(username, inv_id, operation, owner, date):
    file_request_msg = file('data/request_message.pkl', 'ab+')
    req_msg = RequestMessage(username, inv_id, operation, owner, date)
    pickle.dump(req_msg, file_request_msg, True)
    file_request_msg.close()
    

if __name__ == 'main':
    
    add_request_msg('wendy', '2', 'borrow', 'admin', str(datetime.datetime.now()));
    add_request_msg('wendy2', '3', 'borrow', 'admin', str(datetime.datetime.now()));
    

    