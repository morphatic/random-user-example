"""Unit tests for using the random users API"""

# import functions to be tested
from random_user import dob2age

def describe_functions_for_playing_with_random_user_data():
    """Random user unit tests"""
    # pylint: disable=unused-variable
    def can_blow_smoke():
        assert True

    def that_can_convert_dob_to_age():
        """Converts date string in ISO 8601 format to an age rounded to the nearest year"""
        assert dob2age('1974-02-17T19:30:00.000-4:00') == 46
        assert dob2age('2000-03-22T23:00:00Z') == 20
