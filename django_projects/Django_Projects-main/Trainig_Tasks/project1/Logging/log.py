from.models import logging
from serializer import LoggingSerializer
from views import log
import logging

logging.basicConfig(filename='demo.log', level=logging.DEBUG, filemode='w')


def NameCheck(name):
    if len(name)<10:
        logging.debug('check for name length')
        return 'invalid name'
    elif name.isspace():
        logging.info('check if name is space')
        return 'invalid name'
    elif name.isalpha():
        logging.warning('check if name is alphabet')
        return 'invalid name'
    elif name.isalpha():
        logging.error('This is ERROR message')
        return 'invalid name'
    else:
        logging.critical('THIS IS SUCCESSFULL CHECK ALL MESSAGES')

print(NameCheck("VASU"))





