#!/usr/bin/python

"""
	stores command documentation for /help queries
"""

commandList = {
	'add': 'usage: /add <house> <name>\nadd a new freshman <name> from <house>',
	'remove': 'usage: /remove <house> <name>\nremoves a freshman <name> from <house>',
	'find': 'usage: /find <house> <name>\nfinds a freshman <name> from <house>',
}

def getHelp(command):
	if command in commandList:
		return commandList.get(command)
	else:
		return 'Command not found.'
