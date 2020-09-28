"""Functions for playing with random user data"""

# import python standard libraries
from math import floor
from datetime import datetime

# import useful functions from 3rd party packages
from dateutil import parser
from pytz import timezone

def dob2age(dob):
    """
    Takes a string representing a date and returns
    a number representing the age associated with
    the date.
    """
    # convert `dob` date string into a `datetime` object
    dob = parser.parse(dob)
    # get a datetime object for "now" in the Eastern US timezone
    now = datetime.now(timezone('America/New_York'))
    # calculate the age based on `dob` and `now`
    age = floor((now - dob).days / 365)
    # return the age
    return age
