#!/usr/bin/python

from fdnagios import *
if __name__ == '__main__':
   """setting of nagios account proprieties"""
   resource="public_name"	
   username="jabberuser"
   server="jabberserver"
   
   """Jabber URI is username@server (sometimes referred to as a "bare JID") prepended by 'xmpp:'"""
   me=username+'@'+server+'/'+resource
   password="jabberpassword"
   staff=[]	
	
   if len(sys.argv)!=3:
	print("usage: %s <jabber account> <message>" % sys.argv[0])
	sys.exit(1)
   if sys.argv[1].find(',')>0:
        account=sys.argv[1].split(',')
   else:
       	account=[sys.argv[1]]
   message=sys.argv[2].lower()
   for i in account:
	i=str(i)+'/'+resource
	staff.append(i)
   s=nagiosBot(me, password, staff, message)	
   s.start()	
