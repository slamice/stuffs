
# #!/usr/bin/env python
# coding=utf-8
#
# Script Name:  stuff
# Description:  Takes a csv, does stuff to it
#
######

import sys
import csv
import os
import optparse
from datetime import datetime
import logging
import json

# Builds the sql and executes to reinser the job meta
def build_insert():
    try:
        logging.info('Updating stuff %s' % 1)
    except Exception as e:
        logging.info('Update failed for stuff %s...' % 1)

if __name__ == '__main__':

    usage = 'Usage: %prog -D <database>'
    cmdline = optparse.OptionParser(usage,
        version="example 0.1",
        description="""Takes CSV, outputs stuffs""")
    cmdline.add_option('-C', '--CSV',
        help = 'Make sure your CSV is correctly formatted', action='store', type='string', dest='csv')

    (options, args) = cmdline.parse_args()

    if not options or (len(args) < 1 and len(args)) > 4:
        print "Please type -h to see the parameters to enter for this script."
        exit(1)

    if options.csv is None:
        sys.exit('You must enter a user id')

    logger.info('** Finished updating... **')