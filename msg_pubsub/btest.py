'''
Created on Mar 28, 2016

@author: wuw7
'''
from flask import Flask, request, current_app, render_template, flash
from blinker import Namespace
import logging

app = Flask(__name__)
app.secret_key = 'some_secret'

my_signals = Namespace()
mail_sent_signal = my_signals.signal('mail-sent')
  
@mail_sent_signal.connect_via(app)
def show_msg(self, email):
    logging.warn("sent mail to %s", email)
    flash(u'flash: sent mail to ' + email, 'error')

@app.route("/", methods=['GET'])
def hello():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def send_mail():
    email = request.form['email']
    #send the signal
    mail_sent_signal.send(current_app._get_current_object(),email = email)
    return render_template("index.html", msg = "sent successfully")

@app.route("/hi")
def hi():
    return "hi"   
if __name__ == '__main__':
    app.run(debug=True)
   
