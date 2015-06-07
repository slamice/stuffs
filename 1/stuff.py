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
import re
import os
import optparse
import decimal
from datetime import datetime, date, timedelta
import calendar
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

            capacity = int(row[0])
            monthlyPrice = int(row[1])
            startDay = datetime.strptime(row[2], '%m/%d/%Y').date()
            endDay = datetime.strptime(row[3], '%m/%d/%Y').date() if row[3] else ''

            # Check if the month and year is between between the reservation times
            if between_dates(startDay, endDay, given_date):
                # For each reservation, find the last day they are paying and teh price per day
                end_of_month = end_of_given_month(given_date)
                print('end of month: ' + str(end_of_month))

                daily_price = price_per_day(end_of_month.day, monthlyPrice)
                print('daily price: ' + str(daily_price))

                # Find all the days people are reserving for
                days_paying = end_of_month.day - startDay.day
                print('days paying: ' + str(days_paying))

                final_monthly_price = capacity * (daily_price * days_paying) # * number of years paying?
                print('Final monthly price: ' + str(final_monthly_price))

                final_monthly_price += final_monthly_price
                #final_capacity += capacity


    print 'expected revenue: ${0}, expected total capacity of the unreserved offices: {1}'.format(str(final_monthly_price), str(final_capacity))


# find number of times a specific month happpens between two dates
#def between_dates(start, end, given_date):
#
#    print '-----------'
#    print start.year
#    print given_date.year
#    print end.year if end != '' else ''
#    print ''
#    print start.month
#    print given_date.month
#    print end.month if end != '' else ''
#    print '-----------'
#
#    if end != '' and (start.year <= given_date.year <= end.year) and (start.month <= given_date.month <= end.month):
#        return True
#    
#    if end == '' and (start.year <= given_date.year) and (start.month <= given_date.month):
#        return True
#    
#    return False

# Give the month and price, how much per day
def price_per_day(days_in_month, monthlyPrice):
    return monthlyPrice / float(days_in_month)

# Find the last calendar day of the given month
def end_of_given_month(given_date):
    last_day = calendar.monthrange(given_date.year, given_date.month)[1]
    return datetime(given_date.year, given_date.month, last_day).date()


def last_day_of_month(end, given_end_date):
    # 1. If the reservation end date is not specified
    # 2. If the month is different, take the last day of the given month
    #
    # return the last day of the given month
    if end == '' or given_date.month != end.month:
        return end_of_month

    # If the month is the same, take the highest last day
    if (given_date.month == end.month):
        return end_of_month if end_of_month.day > end.day else end

    # Otherwise, error like mad
    sys.exit('End of month math is wrong!')


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
        sys.exit('You must enter a month you would like more info about')

    # validate if can be converted to a date
    given_date =  datetime.strptime(options.given_date, '%Y-%m').date()

    print(determine_revenue_and_capacity(options.csv, given_date))