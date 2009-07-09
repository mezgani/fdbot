#!/usr/bin/python

"""fdbot is free software; you can redistribute it and/or modify it 
under the terms of the GNU General Public License as published
by the Free Software Foundation; either version 2 of the License,
or (at your option) any later version.See the GNU General Public License for more details"""

# Twisted Imports
from twisted.words.protocols.jabber import client, jid
from twisted.words.xish import domish, xmlstream
from twisted.internet import reactor
import sys, time

class nagiosBot:
	def __init__(self, me, password, staff, message):
	   self.me=me
	   self.password=password
	   self.message=message
	   self.staff=staff	
	   if me is not None:
	      self.server=me.split('@')[1].split('/')[0]
	      self.xmlstream = None

	def authd(self, xmlstream):
	   presence = domish.Element(('jabber:client', 'presence'))
	   presence.addElement('status').addContent('up !!!')
	   self.xmlstream = xmlstream
	   self.xmlstream.send(presence)
	   self.xmlstream.addObserver('/*', self.debug)
	   for user in self.staff:
	 	self.alert(user, self.message)


	def alert(self, user, msg):
	   message = domish.Element(('jabber:client','message'))
	   message["to"] = user
	   message["from"] = jid.JID(self.me).full()
	   message["type"] = "chat"
	   message.addElement("body", "jabber:client", msg)
	   self.xmlstream.send(message)

	def debug(self, elem):
	   print elem.toXml().encode('utf-8')
	   print "="*20

	def stop(self):
	   reactor.stop()

	def start(self):
           myJid = jid.JID(self.me)
	   factory = client.basicClientFactory(myJid, self.password)
       	   factory.addBootstrap('//event/stream/authd',self.authd)
	   reactor.connectTCP(self.server, 5222, factory)
       	   reactor.callLater(5, self.stop)  
 	   reactor.run()	
