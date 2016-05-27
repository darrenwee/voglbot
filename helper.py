#!/usr/bin/python

"""
	stores command documentation for /help queries
	
	##### do not terminate the description, examples and parameters dictionaries with newlines ######
"""

# command description list (do not terminate with newlines)
description = {
	'add': 'usage: /add house name\n-- add a new freshman name from house',
	'remove': 'usage: /remove house name\n-- removes a freshman name from house',
	'find': 'usage: /find house name\n-- finds a freshman name from house and replies with his/her details (name, house and status). name need not be exact.',
	'vfind': 'usage: /vfind house name\n-- finds a freshman name from house and replies with his/her details (name, house, status, diet, medical declaration, addedby). name need not be exact.',
	'enumerate': 'usage: /enumerate house mode\n-- enumerates all the members of house with status mode',
    'check': 'usage: /check house name status\n-- updates a freshmen\'s status',
    
	#'sos': 'usage: /sos message\n-- sends an SOS to all first aiders along with a message message; the message is optional. do not misuse this command',
}

# example usage (do not terminate with newlines)
examples = {
	'add': 'e.g. /add black john doe augustus lim xiao hua\n-- adds \'john doe augustus lim xiao hua\' to black house',
	'remove': 'e.g. /remove black john doe augustus lim xiao hua\n-- removes \'john doe augustus lim xiao hua\' to black house',
	'find': 'e.g. /find black john doe\n-- finds every entry with the name containing \'john doe\' in black house',
	'vfind': 'e.g. /vfind black john\n-- finds every entry with name containing \'john\' in black house',
	'enumerate': 'e.g. /enumerate green present\n-- gives a list of all students from green house who are present',
    'check': 'e.g. /check black darren wee absent\n--change status of \'darren wee\' from black house to \'absent\'',
	#'sos': 'e.g. /sos FRESHIE KENNA HEATSTROKE\n-- (if sent by Darren) sends the following:\n\nSOS by Darren: freshie kenna heatstroke\n\nto all first aiders',
}

# argument list
parameterDict = {
	'group': 'group -- \'freshmen\', \'ogls\', \'fopcomm\'',
	'house': 'house -- \'green\', \'black\', \'purple\', \'blue\', \'red\', \'orange\', \'all\'',
	'mode': 'mode -- \'present\', \'absent\', \'total\'',
    'status': 'status -- \'present\' or \'absent\'',
}

# relevant parameter list
relevantParameters = {
	'add': ['house'],
	'remove': ['house'],
	'find': ['house'],
	'vfind': ['house'],
	'enumerate': ['house', 'mode'],
    'check': ['house', 'status']
}

def getHelp(command):
	reply = ''

	# check if basic doc exists
	if description.has_key(command):
		reply += description.get(command) + '\n\n'

		# append the example if there is one
		if examples.has_key(command):
			reply += examples.get(command) + '\n\n'

		# append parameters if there are any
		if relevantParameters.has_key(command):
			reply += 'Parameters\n'
			for param in relevantParameters.get(command):
				reply += '%s\n' % (parameterDict.get(param))
	else:
		return 'Command not found.'

	return reply

def naiveHelp():
	reply = 'Commands available:\n'
	for command in description.keys():
		reply += command + '\n'
	reply += '\nUse \'/help command\' for more info'
	return reply
