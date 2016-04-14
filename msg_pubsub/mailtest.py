'''
Created on Apr 9, 2016

@author: wuw7
'''
#!/usr/bin/python

import smtplib
import traceback

sender = 'wendy.wu@emc.com'
receivers = ['wendy.wu@emc.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
    smtpObj = smtplib.SMTP('127.0.0.1', 1025)
    smtpObj.sendmail(sender, receivers, message)         
    print "Successfully sent email"
except Exception:
    print "Error: unable to send email"
    print traceback.print_exc()