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
    'enum': 'usage: /enum house\n-- enumerates all the members of house',
    'in': 'usage: /in house name\n-- change status of name from house to present',
    'out': 'usage: /out house name\n-- change status of name from house to absent',
    #'sos': 'usage: /sos message\n-- sends an SOS to all first aiders along with a message message; the message is optional. do not misuse this command',
    'medical': 'usage: /medical house name: message\n-- change medical declaration of name from house to message',
    'diet': 'usage: /diet house name: message\n-- change diet declaration of name from house to message',
    'log': 'usage: /log house name\n-- get the status log of name from house',
}

# example usage (do not terminate with newlines)
examples = {
    'add': 'e.g. /add black john doe augustus lim xiao hua\n-- adds \'john doe augustus lim xiao hua\' to black house',
    'remove': 'e.g. /remove black john doe augustus lim xiao hua\n-- removes \'john doe augustus lim xiao hua\' to black house',
    'find': 'e.g. /find black john doe\n-- finds every entry with the name containing \'john doe\' in black house',
    'vfind': 'e.g. /vfind black john\n-- finds every entry with name containing \'john\' in black house',
    'enum': 'e.g. /enum green\n-- gives a list of all present and absent students from green house',
    'in': 'e.g. /in black john doe\n-- change status of \'john doe\' from \'black\' house to present',
    'out': 'e.g. /out black john doe\n-- change status of \'john doe\' from \'black\' house to absent',
    #'sos': 'e.g. /sos FRESHIE KENNA HEATSTROKE\n-- (if sent by Darren) sends the following:\n\nSOS by Darren: freshie kenna heatstroke\n\nto all first aiders',
    'medical': 'e.g. /medical black ningxin: allergic to strawberries',
    'diet': 'e.g. /diet black ningxin: halal, no beef',
    'log': 'e.g. /log black ningxin',
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
    'in': ['house'],
    'out': ['house'],
    'medical': ['house'],
    'diet': ['house'],
    'log': ['house'],
}

def getHelp(command):
    reply = ''

    # check if basic doc exists
    if command in description:
        reply += description.get(command) + '\n\n'

        # append the example if there is one
        if command in examples:
            reply += examples.get(command) + '\n\n'

        # append parameters if there are any
        if command in relevantParameters:
            reply += 'Parameters\n'
            for param in relevantParameters.get(command):
                reply += '%s\n' % (parameterDict.get(param))
    else:
        return 'Command not found.'

    return reply

def naiveHelp():
    reply = 'Commands available:\n\n'
    for command in description.keys():
        reply += command + '\n'
    reply += '\nUse \'/help command\' for more info'
    return reply
