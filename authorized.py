#!/usr/bin/python

from voglogger import *

"""
    authorized chat IDs for using VOGLBot

    remember to update parallel comments so that we know which ID is which person!
"""

address_book = {
    'Darren'    : 53558212,     # black VOGL, admin
    'Yantyng'   : 112279032,    # safety/FOP, black OGL
    'Chester'   : 110971462,    # blue VOGL
    'Samantha'  : 106888349,    # red VOGL
    'Khaiqing'  : 118410662,    # purple VOGL
    'Claire'    : 27374797,     # green VOGL
    'Jiahao'    : 68976391,     # orange VOGL
}

rev_book = dict((v,k) for k,v in address_book.iteritems())

################################################################
## only authorized house and FOP comm members can use the bot ##
##   remember to respect PDPA and need-to-know basis of info  ##
################################################################

# admins receive system reports and logging
admins = ['Darren']

vogls = ['Darren', 'Jiahao', 'Claire', 'Khaiqing', 'Chester', 'Samantha']

#           Xinying Hongwei Bryan   Natalya     Changming   Jingshun
cogls = []

#           Andrea Yuchuan  Yantyng Shaoyang
fopcomm = ['Yantyng']

#           Raag    Lynette Leon    Dexter  Elisabeth   Zhihao  
safety = ['Darren', 'Yantyng']

# all authorized users are stored here
authorized = admins + vogls + cogls + fopcomm + safety
authorized = list(set(authorized)) # get rid of duplicates
#authorized = []

def getIDs(group):
    #logger.info('IDs for %s were requested' % group)
    IDs = []
    for person in group:
        if address_book.has_key(person):
            IDs.append(address_book.get(person))
        else:
            logger.warning('%s was not found in address book.' % person)
    return IDs

def whoIs(target_id):
    if rev_book.has_key(target_id):
        return rev_book.get(target_id)
    else:
        logger.warning('%s was not found in address book.' % target_id)
        return target_id
