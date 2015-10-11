'''
Created on Sep 24, 2015

@author: wuw7
'''
from model.models import RequestMessage
import cPickle as pickle
import datetime
import os

class Picker():
    @staticmethod
    def add_request_msg(username, inv_id, operation, owner, date):
        if os.path.isfile('IM/data/request_message.pkl'):
            file_load = file('IM/data/request_message.pkl','rb') 
            try:
                msg_list = pickle.load(file_load)
            except EOFError:
                msg_list = []    
            file_load.close()       
        else:
            msg_list = []
               
        req_msg = RequestMessage(username, inv_id, operation, owner, date)
        msg_list.append(req_msg)
        
        file_request_msg = file('IM/data/request_message.pkl', 'wb+')
        pickle.dump(msg_list, file_request_msg, True)
        file_request_msg.close()

    @staticmethod
    def delete_request_msg(message_id):
        if os.path.isfile('IM/data/request_message.pkl'):
            file_load = file('IM/data/request_message.pkl','rb') 
            try:
                msg_list = pickle.load(file_load)
            except EOFError:
                msg_list = []    
            file_load.close()
            for item in msg_list:
                if item.message_id == message_id:
                    msg_list.remove(item)
            
            file_request_msg = file('IM/data/request_message.pkl', 'wb+')
            pickle.dump(msg_list, file_request_msg, True)
            file_request_msg.close()
            return True
        else:
            return False
    @staticmethod
    def get_msg_list():
        if os.path.isfile('IM/data/request_message.pkl'):
            file_load = file('IM/data/request_message.pkl','rb') 
            try:
                msg_list = pickle.load(file_load)
            except EOFError:
                msg_list = []    
            file_load.close()
            return msg_list
        else:
            return []
        

if __name__ == '__main__':
    
    #add_request_msg('wendy6', '1', 'borrow', 'admin', str(datetime.datetime.now()));
    #add_request_msg('wendy2', '3', 'borrow', 'admin', str(datetime.datetime.now()));
    #print message_queue.get()
      
   list = get_msg_list()
   print list
   delete_request_msg('wendy612015-09-24 17:10:53.467000')
   print get_msg_list()

    