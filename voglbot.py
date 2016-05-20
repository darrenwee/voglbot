#!/usr/bin/python

import sys
import time
import pprint
import logging
import telepot

import redis
db = redis.Redis(
	host = 'localhost',
	port = 6379
)

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(message)s')
logger = logging.getLogger()

"""
	$ python voglbot.py <telegram-bot-token>

	VOGLBot: Every VOGL's favorite assistant

	accepted commands:
		/add <name>,<house>
		/remove <name>,<house>

	kill program with Ctrl-C
"""

# load auxiliary data
from settings_secret import * 	# telegram bot API token
from authorized import * 		# authorized user management

def report(message):
	for admin in admins:
		bot.sendMessage(admin, message)
	return

def deny(chat_id):
		# print to console log
		print 'WARNING: chat ID %s was denied access.' % chat_id

		# scold unauthorized user
		bot.sendMessage(chat_id, "You are not authorized to use this bot; this incident has been reported. Contact Darren at 92328340 if this is a mistake.")
		
		# report incident to admins (listed in authorized.py)
		report("WARNING: chat ID %s was denied access" % chat_id)
		return

def add(name, house):
	print 'Adding %s from %s' % (name, house)

def handle(msg):
	#pprint.pprint(msg)
	msg_type, chat_type, chat_id = telepot.glance(msg)

	command = msg['text'].strip().lower()
	print 'Received command: %s from %s' % (command, chat_id)

	if msg_type != 'text':
		return
	
	if chat_id not in authorized:
		deny(chat_id)
		return

	if command == '/hello':
		bot.sendMessage(chat_id, "Hi!")

# start the bot
bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print ('Listening ...')

while 1:
	time.sleep(5)
