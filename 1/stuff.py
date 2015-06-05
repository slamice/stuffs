#    You're given a CSV file ( s3.amazonaws.com/misc-ww/data.csv ) containing office reservation data. 
#    Each line represents a reservation of a unique office. There're four columns in each line:
#    Capacity, Monthly Price, Start Day, and End Day. The fourth column "End Day" could be empty,
#    meaning the office is indefinitely reserved starting from the Start Day.
#     
#    Please fork this script(use the fork button at top left) and write a script using the language 
#    of your choice that answers the following questions.
#    1) Given a month and a year, what is the revenue for the given month?
#    2) Given a month and a year, what is the total capacity of the unreserved offices for the given month?
#     
#    When you are complete please send us the link to your script. We'll use the following inputs to test your code.
#    The input will be in this format: YYYY-MM
#    1) 2000-01 (expected revenue: $0.00, expected total capacity of the unreserved offices: 266)
#    2) 2018-01 (expected revenue: $77,000.00, expected total capacity of the unreserved offices: 135)
#    3) 2013-01
#    4) 2014-08
#     
#    Notes:
#    1) Unreserved offices are the offices that are not reserved for a single day for the given month.
#    2) If an office is partially reserved for a given month, the revenue should be prorated based on the monthly price.
#    For example: 2, 1500, 2014-05-01, 2014-05-15 counts as $750 in revenue for May because the reservation was for half of the month.
#    3) For simplicity sake you can include the CSV file as heredoc in your script.     
#    */



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

def determine_revenue_and_capacity(csvfile, given_date):

    final_capacity = 0
    final_monthly_price = 0

    with open(csvfile) as csv_file:
        for row in csv.reader(csv_file, delimiter=','):
            # Skip first row
            if row[0] == 'Capacity':
                continue

            print 'startDay '+ row[2]
            print 'endDay '+ row[3]

            capacity = row[0]
            monthlyPrice = row[1]
            startDay = datetime.strptime(row[2], '%M/%d/%Y').date()
            endDay = datetime.strptime(row[3], '%M/%d/%Y').date() if row[3] else ''

            # Check if the month and year is between between the reservation times
            print between_dates(startDay, endDay, given_date)

            # Count days until end of the month


    return 

def between_dates(start, end, given_date):
    if type(end) is datetime:
        return True if start < given_date < end else False 
    
    elif start < given_date:
        return True
    
    return False

    


#{MM-YYYY:{day:revenue, capacity}}

#reservation {}


# basically just overlapping reservations, like a calendar
# We define a reservation by a key start and end date. We
# check if each reservation falls within the date range
# specified

#def revenue_and_capacity(month, year, data):
#   return 


# python stuff.py -C data.csv -D 2000-01
if __name__ == '__main__':

    usage = 'Usage: %prog -D <database>'
    cmdline = optparse.OptionParser(usage,
        version="example 0.1",
        description="""Takes CSV, outputs stuffs""")
    cmdline.add_option('-C', '--CSV',
        help = 'Make sure your CSV is correctly formatted', action='store', type='string', dest='csv')
    cmdline.add_option('-D', '--date',
        help = 'The date in the form of YYYY-MM', action='store', type='string', dest='given_date')

    (options, args) = cmdline.parse_args()

    if not options or (len(args) < 1 and len(args)) > 4:
        print "Please type -h to see the parameters to enter for this script."
        exit(1)

    if options.csv is None:
        sys.exit('You must enter a csv file')

    if options.given_date is None:
        sys.exit('You must enter a month you would liek more info about')

    # validate if can be converted to a date
    given_date =  datetime.strptime(options.given_date, '%M/%Y').date()

    determine_revenue_and_capacity(options.csv, given_date)

    logger.info('** Finished updating... **')