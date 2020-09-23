"""Unit tests for using the random users API"""

def describe_functions_for_playing_with_random_user_data():
    """Random user unit tests"""
    # pylint: disable=unused-variable
    def can_blow_smoke():
        assert True

    def can_convert_dob_to_age():
        assert dob2age('1974-02-17T19:30:00.000-4:00') == 46
