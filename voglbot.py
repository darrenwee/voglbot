#!/usr/bin/python

import sys
import time
import random
import threading
import telepot
import pymongo

import re

from telepot.delegate import per_chat_id, create_open

# voglbot modules
from settings_secret import TOKEN   # telegram API key
from authorized import *            # user management
from manager import *               # database management
from voglogger import logger        # logger object
import helper                       # /help documentation

# regular expressions for commands
register_re = re.compile('(/[a-z]+)\s+([a-z]+)\s+(.+)', re.I)
updater_re = re.compile('(/[a-z]+)\s+([a-z+)\s+([a-z]+)\s+(.+)', re.I)

class VOGLBot(telepot.Bot):
    def __init__(self, *args, **kwargs):
        super(VOGLBot, self).__init__(*args, **kwargs)
        self._answerer = telepot.helper.Answerer(self)
        self._message_with_inline_keyboard = None
        self._previous = ''

#    def __init__(self, seed_tuple, timeout):
#        super(VOGLBot, self).__init__(seed_tuple, timeout)
#        self._previous = ''

    # message handler
    def on_chat_message(self, message):
        content_type, chat_type, chat_id = telepot.glance(message)
        
        # check for message type
        if content_type != 'text':
            self.sendMessage(chat_id, 'This bot can only receive text messages!')
            return

        command = message['text'].lower()
        logger.info('Received \'%s\' from %s' % (command, whoIs(chat_id)) )

        # message for /start
        if command == '/start':
            self.sendMessage(chat_id, 'Hi! I\'m VOGLBot, a friendly robot assistant for USC FOP 2016.')
            self.sendMessage(chat_id, 'You are \'%s\'. If you do not see your name displayed, you cannot use this bot.' % whoIs(chat_id))
            return

        # deny unauthorized user access
        if chat_id not in getIDs(authorized):
            logger.warning('Attempted unauthorized access by %s.' % whoIs(chat_id))
            self.sendMessage(chat_id, 'You are not authorized to use this bot. Contact Darren at 92328340 or @ohdearren if this is a mistake.')
            return

        # do stuff
        if command == '/help':
            self.sendMessage(chat_id, helper.naiveHelp())
        elif command.startswith('/help'):
            matches = re.match('/help ([a-z]+)', command)
            self.sendMessage(chat_id, helper.getHelp(matches.group(1)))

        # registration-type commands
        elif command.startswith('/add'):
            matches = re.match(register_re, command)
            self.sendMessage(chat_id, add(matches.group(2), matches.group(3), chat_id))
        elif command.startswith('/remove'):
            matches = re.match(register_re, command)
            self.sendMessage(chat_id, remove(matches.group(2), matches.group(3), chat_id))
        elif command.startswith('/strength'):
            matches = re.match(register_re, command)
            self.sendMessage(chat_id, getStrength(matches.group(2), matches.group(3), chat_id))
        elif command.startswith('/enum'):
            house = re.match('\s*/enum\s+([a-z]+)', command).group(1)
            self.sendMessage(chat_id, getEnumerate(house, chat_id))
        elif command.startswith('/find'):
            matches = re.match(register_re, command)
            self.sendMessage(chat_id, find(matches.group(2), matches.group(3), False, chat_id))
        elif command.startswith('/vfind'):
            matches = re.match(register_re, command)
            self.sendMessage(chat_id, find(matches.group(2), matches.group(3), True, chat_id))
        elif command.startswith('/in'):
            matches = re.match('(/[a-z]+)\s+([a-z]+)\s+(.+)', command)
            if matches != None:
                self.sendMessage(chat_id, updater(matches.group(2), matches.group(3), 'status', 'present', chat_id))
            else:
                self.sendMessage(chat_id, 'Update failed. No such house/person.')
        elif command.startswith('/out'):
            matches = re.match('(/[a-z]+)\s+([a-z]+)\s+(.+)', command)
            if matches != None:
                self.sendMessage(chat_id, updater(matches.group(2), matches.group(3), 'status', 'absent', chat_id))
            else:
                self.sendMessage(chat_id, 'Update failed. No such house/person.')

        self._previous = command
        return
    

logger.info('VOGLBot is listening ...')

# the timeout here refers to when a delegator starts over
#bot = telepot.DelegatorBot(TOKEN, [
#    (per_chat_id(), create_open(VOGLBot, timeout=120)),
#])
#bot.message_loop(run_forever=True)

bot = VOGLBot(TOKEN)
bot.message_loop()

while 1:
    time.sleep(10)
