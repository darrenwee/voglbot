#!/usr/bin/python

import datetime
from voglogger import logger
from authorized import whoIs
from pymongo import *

# establish connection to mongodb server
try:
    connection = MongoClient('monty', 27017)
    logger.info('Successfully connected to MongoDB daemon')
except pymongo.errors.ConnectionFailure, e:
    logger.error('Failed to connect to MongoDB: %s' % e)
    logger.error('VOGLBot exiting!')
    sys.exit(1)

db = connection['primary']
students = db['students']

### helper functions ###
def houseIsValid(house):
    return house in ['green', 'black', 'purple', 'blue', 'red', 'orange', 'all']

def statusIsValid(status):
    return status in ['present', 'absent', 'total']

def enumerator(cursor, fields):
    reply = ''

    # catch size 0 cursor
    if cursor.count() == 0:
        return 'No records found.'

    i = 1
    for person in cursor:
        reply += str(i) + '.\n'
        for field in fields:
            reply += '%s: %s\n' % (field.title(), person[field].title())
        i += 1
        reply += '\n'

    return reply

### executive functions ###
def add(house, name, requester):

    if houseIsValid(house):
        timestamp = str(datetime.datetime.now())
    
        logger.info('%s: Adding \'%s\' from \'%s\'' % (whoIs(requester), name, house))
        student = {
            'name': name,
            'type': 'freshman',
            'house': [house, 'all'],
            'status': 'present',
            'statuslog': ['initial registration at ' + timestamp],
            'diet': '',
            'medical': '',
            'addedby': whoIs(requester)
        }

        students.insert_one(student)
        logger.info('%s: Added \'%s\' to \'%s\' house' % (whoIs(requester), name, house))
        return 'Successfully added \'%s\' of \'%s\' house into database.' % (name, house)
        
    logger.info('%s: /add query failed (invalid parameters)' % whoIs(requester))
    return 'Invalid house name. See \'/help add\''

def remove(house, name, requester):
    reply = 'Removed \'%s\' of \'%s\' house from database.' % (name, house)
    logger.info(whoIs(requester) + ': ' + reply)
    report(whoIs(requester) + ': ' + reply)

    # perform remove
    return reply

def getStrength(house, status, requester):
    reply = ''

    if houseIsValid(house) and statusIsValid(status):
        # get total house strength (status-independent)
        house_strength = students.count( {'house': house} )

        # get modal house strength (status-dependent) and build reply
        if status in ['present', 'absent']:
            status_strength = students.count( {'house': house, 'status': status} )
            reply += 'Strength for \'%s\' in \'%s\': %d/%d' % (status, house, status_strength, house_strength)
        else:
            reply += 'Total strength for \'%s\' house is %d' % status_strength
    else:
        # catch shitty parameters
        logger.info('%s: /strength query failed (invalid parameters)' % whoIs(requester))
        return 'Invalid house or status. See \'/help strength\''

    logger.info('%s: Returning strength for \'%s\' house' % (whoIs(requester), house))
    return reply

def getEnumerate(house, status, requester):

    if houseIsValid(house) and statusIsValid(status):
        reply = 'Enumerating \'%s\' in \'%s\'\n\n' % (status, house)

        # query for database cursor
        if status in ['present', 'absent']:
            results = students.find( {'house': house, 'status': status} )
        else:
            results = students.find( {'house': house} )

        # sort results
        results.sort( [ ('status', -1), ('name', 1) ] )

        # catch empty house/mode query
        if results.count() == 0:
            return reply + 'No records found.'

        # build the reply message
        i = 1
        reply += 'Enumerating \'%s\' in \'%s\'\n\n' % (status, house)
        for person in results:
            reply += '%d. %s: %s, %s\n' % (i, person['name'].title(), person['house'].title(), person['status'].title())
            i += 1
    else:
        # catch invalid parameters
        logger.info('%s: /enumerate query failed (invalid parameters)' % whoIs(requester))
        return 'Invalid house or status. See \'/help enumerate\''

    logger.info('%s: Returning enumeration for \'%s\' in \'%s\'' % (whoIs(requester), status, house))
    return reply

def find(house, pattern, verbose, requester):
    reply = ''

    if houseIsValid(house):
        # query for database cursor
        if house == 'all':
            results = students.find( {'name': { '$regex': '.*' + pattern + '.*'} } )
        else:
            results = students.find( {'name': { '$regex': '.*' + pattern + '.*'}, 'house': house } )
    
        # sort results
        results.sort( [ ('house', -1), ('name', 1) ] )

        # what info to send back (determined by verbose flag)
        if verbose is True:
            details = ['name', 'house', 'status', 'dietary', 'medical', 'addedby']
        else:
            details = ['name', 'house', 'status']
    
        # build the reply
        reply += 'Finding any patterns with \'%s\' for \'%s\'\n\n' % (pattern, house)
        reply += enumerator(results, details)
    else:
        # catch shitty parameters
        logger.info('%s: /find query failed (invalid parameters)' % whoIs(requester))
        return 'Invalid house. See \'/help find\''

    logger.info('%s: Returning find query for pattern \'%s\' for \'%s\'' % (whoIs(requester), pattern, house))
    return reply