#!/usr/bin/python

from voglogger import *

"""
	authorized chat IDs for using VOGLBot

	remember to update parallel comments so that we know which ID is which person!
"""

address_book = {
	'Darren'	: 53558212,
	'Yantyng'	: 112279032,
}

################################################################
## only authorized house and FOP comm members can use the bot ##
##   remember to respect PDPA and need-to-know basis of info  ##
################################################################

# admins receive system reports and logging
admins = ['Darren']

#			Darren	Jiahao	Claire	Khaiqing	Chester		Samantha
vogls = ['Darren']

# 			Xinying	Hongwei	Bryan	Natalya		Changming	Jingshun
cogls = []

# 			Andrea Yuchuan	Yantyng	Shaoyang
fopcomm = []

#			Raag	Lynette	Leon	Dexter	Elisabeth	Zhihao	
safety = []

# all authorized users are stored here
#authorized = admins + vogls + cogls + fopcomm + safety
authorized = []

def getIDs(group):
	logger.info('IDs for %s were requested' % group)
	IDs = []
	for person in group:
		if address_book.has_key(person):
			IDs.append(address_book.get(person))
		else:
			logger.warning('%s was not found in address book.' % person)
	return IDs
