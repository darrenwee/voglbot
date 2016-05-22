#!/usr/bin/python

import sys
import time
import datetime
import pprint
import logging
import telepot
import re
#from fuzzywuzzy import fuzz # for fuzzy string matching

# load auxiliary data
from voglogger import * 		# logger management
from settings_secret import * 	# telegram bot API token
from authorized import * 		# authorized user management
from helper import *			# /help documentation

from pymongo import *
# establish connection to mongodb server
try:
	connection = MongoClient('monty', 27017)
	logger.info("Successfully connected to MongoDB daemon")
except pymongo.errors.ConnectionFailure, e:
	logger.error("Failed to connect to MongoDB: %s" % e)
	logger.error("VOGLBot exiting!")
	sys.exit(1)

db = connection['primary']
students = db['students']

"""
	$ python voglbot.py <telegram-bot-token>

	VOGLBot: Every VOGL's favorite assistant

	accepted commands:
		/add <name>,<house>
		/remove <name>,<house>

	kill program with Ctrl-C
"""

def report(message):
	for admin in getIDs(admins):
		bot.sendMessage(admin, '[Admin] ' + message)
		logger.warning('Sent \'%s\' to admin %s' % (message, admin))
	return

def deny(chat_id):
	# print to console log
	logger.error('Chat ID %s was denied access.' % chat_id)

	# scold unauthorized user
	bot.sendMessage(chat_id, "You are not authorized to use this bot; this incident has been reported. Contact Darren at 92328340 if this is a mistake.")

	# report incident to admins (listed in authorized.py)
	report("WARNING: chat ID %s was denied access" % chat_id)
	return

def helper(requester):
	bot.sendMessage(requester, "/add")

def add(house, name, requester):
	# add new person to database
	timestamp = str(datetime.datetime.now())

	# return feedback
	logger.info('%s: Adding %s from %s' % (whoIs(requester), name, house))
	student = {
		"name": name,
		"house": house,
		"status": "present",
		"statuslog": ["initial registration at "+timestamp],
		"medical": "",
		"addedby": whoIs(requester) + "(" + chat_id + ")"
	}

	students.insert_one(student)
	bot.sendMessage(requester, 'Successfully added \'%s\' of \'%s\' house into database.' % (name, house))
	return

def remove(house, name, requester):
	logger.info('Removing %s from %s' % (name, house))
	report('WARNING: %s from %s house was removed from database.' % (name, house))
	return

def getStrength(house, mode):
	logger.info('Returning strength for %s house' % house)
	return

def enumerate(house, mode):
	logger.info('Enumerating %s for %s house' % (mode, house))
	return

def update(house, direction, name):
	# update database
	return

def fuzzyMatch(name):
	# only used when a query fails to find a name
	# returns suggestions to user for close name matches
	return

def find(house, name, requester):
	logger.info('%s: Finding \'%s\'' % (whoIs(requester), name))
	target = students.find_one( {"name": name, "house": house} )

	# decide what info to send back
	details = ['name', 'house', 'status']
	reply = ""
	for detail in details:
		reply += detail + ": " + target[detail] + "\n"
	bot.sendMessage(requester, reply)
	return

def toString(student):
	return

# command groups
register_type = ['/add', '/remove', '/find']
register_re = re.compile('(/[a-z]+)\s+([a-z]+)\s+(.+)', re.IGNORECASE) # /<command> <house> <name>

help_re = re.compile('(/help)\s+(.+)', re.IGNORECASE)

houses = ['green', 'black', 'purple', 'blue', 'red', 'orange', 'all']

def handle(msg):
	#pprint.pprint(msg)
	msg_type, chat_type, chat_id = telepot.glance(msg)

	command = msg['text'].strip().lower()
	logger.info('Received message: \'%s\' from %s' % (command, whoIs(chat_id)))

	if msg_type != 'text':
		bot.sendMessage(chat_id, "I can only receive text messages. Try /help")
		return
	
	if chat_id not in getIDs(authorized):
		deny(chat_id)
		return

	if command == '/hello':
		bot.sendMessage(chat_id, "Hi!")
	elif command.startswith('/help'):
		help_command = re.match(help_re, command)
		bot.sendMessage(chat_id, getHelp(help_command.group(2)))
	elif any(command.startswith(reg) for reg in register_type):
		##################################
		### command is a register type ###
		##################################
		reg_command = re.match(register_re, command)
		commandword = reg_command.group(1)
		house = reg_command.group(2)
		name = reg_command.group(3)

		# input sanitization for house field
		if house not in houses:
			bot.sendMessage(chat_id, 'No such house.')
			return

		if commandword == '/add':
			add(house, name, chat_id)
		elif commandword == '/remove':
			# remove existing person from database
			reply = 'Removing \'%s\' of \'%s\' house from database.' % (name, house)
			logger.info(reply)
			bot.sendMessage(chat_id, reply)
		elif commandword == '/find':
			find(house, name, chat_id)
	else:
		bot.sendMessage(chat_id, "Try /help for a list of commands")

# start the bot
bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
logger.info('VOGLBot is listening ...')

while 1:
	time.sleep(5)
