'''
Created on Aug 31, 2015

@author: wuw7
'''
from view import *
from dao.daos import *
from flask import request, jsonify, redirect, url_for, session
from service.import_excel import Parser
from service.export_excel import Writer
from service.pickle_message import Picker
from IM import app

import os
import datetime

@app.route('/hello/<name>')
def hello_name(name = None):
    return render_template('index.html', name=name)

@app.route('/show')
def show():
    return render_template('index.html', name = session.get('username'), invs = InvDao.get_all_invs())

@app.route('/delete-inventory', methods=['POST'])
def delete_inventory():
    delete_ids = request.form.getlist('rows[]')
    print delete_ids
    b = InvDao.delete_inventory(delete_ids)
    return jsonify(result=b)

@app.route('/search-user', methods=['POST'])    
def search_user():
    search_string = request.form.get('search_string')
    print search_string
    users = UserDao.search_a_user(search_string)
    print users
    print users.username
    user_info = users.username+'  '+ users.email
    print user_info
    return jsonify(result=user_info)
    #results = []
    #for item in checked_list:
     #   results.append(UserDao.search_a_user(item.rowID))
    #return jsonify(results)
    
@app.route('/search-inventory', methods=['POST'])    
def search_inventory():
    search_string = request.form.get('search_string')
    print search_string
    invs_list = InvDao.search_inventory(search_string)
    print invs_list
    inv_info = []
    inv_args = []
    for invs in invs_list:
        if invs != []:
            for inv in invs:
                inv_args = [inv.id, inv.tag, inv.name, inv.PN, inv.SN, inv.shipping, inv.capital, inv.disposition, inv.status, inv.owner]
                inv_info.append(inv_args)
                inv_args = []
    print inv_info
    return jsonify(result=inv_info)
        
@app.route('/add-inventory', methods=['POST'])
def add_inventory():
    tag = request.form.get('tag')
    name = request.form.get('name')
    PN = request.form.get('PN')
    SN = request.form.get('SN')
    ship = request.form.get('ship')
    cap = request.form.get('cap')
    dis = request.form.get('dis')
    status = request.form.get('status')
    owner = request.form.get('owner')
    inv = InvDao.add_inventory(tag, name, PN, SN, ship, cap, dis, status, owner)
    if inv:
        inv_info = [inv.id, inv.tag, inv.name, inv.PN, inv.SN, inv.shipping, inv.capital, inv.disposition, inv.status, inv.owner]
        return jsonify(result=inv_info)
    else: return jsonify(result=None)

@app.route('/borrow', methods=['POST'])
def borrow():
    items = request.form.getlist('rows[]')
    print items
    username = session['username']
    print username
    for i in range(len(items)):
        if i%2 == 0:
            Picker.add_request_msg(username, items[i], 'borrow', items[i+1], str(datetime.datetime.now()))

    print Picker.get_msg_list()   
    #notify
    return jsonify(result=True)
        
@app.route('/login' ,methods=['GET','POST'])
def login():
    if request.method == 'POST':
        name = request.form['login-name']
        password = request.form['login-password']
        if UserDao.login(name, password):
            print 'login with: ' + name
            session['username'] = name
            return redirect('/show')
    return render_template('login.html', error = 'wrong login name or password')

@app.route('/hello')
def welcome():
    return render_template('login.html')

@app.route('/import-excel', methods=['POST'])
def import_excel():
    '''needs to check file type == xlsx etc. 
       if file exists, then server will overrides it by default. 
    '''
    file = request.files['choose-excel-file']
    print file.filename
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    print file_path
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    Parser.parse_by_row(file_path)
    # the imported inventories will be added to the database and appended on the page.
    return redirect('/show')  
    
@app.route('/export-excel', methods=['GET'])
def export_excel():
    invs = InvDao.get_all_invs()
    data = []
    inv_args = []
    for inv in invs:
        inv_args.append(inv.tag)
        inv_args.append(inv.name)
        inv_args.append(inv.PN)
        inv_args.append(inv.SN)
        inv_args.append(inv.shipping)
        inv_args.append(inv.capital)
        inv_args.append(inv.disposition)
        inv_args.append(inv.status)
        inv_args.append(inv.owner)
        data.append(inv_args)
        inv_args=[]
    print data
    file_path = os.path.join(app.config['EXPORT_FOLDER'], 'export.xls')
    print file_path
    Writer.export_excel(data, file_path)