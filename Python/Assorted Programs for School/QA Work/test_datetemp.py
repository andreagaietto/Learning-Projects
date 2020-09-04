from datetemp import *
import datetime
import pytest


@pytest.fixture()
def date_temp_setup():
    # create a set up function to use as needed to avoid code
    # duplication
    valid_date = datetime.date(1987, 6, 20)
    test1 = DateTemp(valid_date, 98)
    return test1


def test_class_with_no_params():
    # verify that an object cannot be created without the necessary
    # arguments passed in
    with pytest.raises(TypeError):
        date_temp = DateTemp()


def test_class_with_two_valid_params():
    # test that a class can be constructed with acceptable inputs.
    # Any two inputs could be provided here as no verification is
    # being done at this point, but a valid date format is provided
    valid_date = datetime.date(1965, 5, 21)
    test1 = DateTemp(valid_date, 67)
    assert test1


def test_class_with_one_valid_param():
    # test that a class cannot be constructed if only one acceptable
    # input is provided
    valid_date = datetime.date(1987, 6, 20)
    with pytest.raises(TypeError):
        test1 = DateTemp(valid_date)


def test_date_property_returns_correct_information(date_temp_setup):
    # test that calling the date property returns correct information
    assert date_temp_setup.date == datetime.date(1987, 6, 20)


def test_date_setter_fails_with_nonexistent_date(date_temp_setup):
    # test that the date setter returns an error if valid numbers
    # are provided, but the date does not exist (date itself is
    # invalid)
    with pytest.raises(ValueError):
        date_temp_setup.date = datetime.date(2020, 8, 32)


def test_date_setter_updates_with_correct_date(date_temp_setup):
    # test that the date setter updates the date appropriately with
    # a valid date
    test_date = datetime.date(2020, 8, 31)
    date_temp_setup.date = test_date
    assert date_temp_setup.date == test_date


def test_temp_property_returns_correct_information(date_temp_setup):
    # verify that the temperature @property returns the correct
    # information
    assert date_temp_setup.temperature == 98


def test_temp_setter_with_valid_int(date_temp_setup):
    # test that temp setter updates input of an int to appropriate
    # float
    date_temp_setup.temperature = 95
    assert date_temp_setup.temperature == 95.0


def test_temp_setter_with_valid_float(date_temp_setup):
    # test that temp setter updates properly if a float is passed
    date_temp_setup.temperature = 99.0
    assert date_temp_setup.temperature == 99.0


def test_temp_setter_with_string(date_temp_setup):
    # verify that a ValueError is raised if a string is passed
    with pytest.raises(ValueError):
        date_temp_setup.temperature = "test"


def test_temp_setter_with_no_value(date_temp_setup):
    # test that a TypeError is raised if null value is passed
    with pytest.raises(TypeError):
        date_temp_setup.temperature = None


def test_date_from_ints_with_valid_inputs(date_temp_setup):
    # verify that function properly sets date with valid inputs
    date_temp_setup.set_date_from_ints(2020, 9, 2)
    assert date_temp_setup.date == datetime.date(2020, 9, 2)


def test_date_from_ints_with_all_strings(date_temp_setup):
    # verify that error is returned if all values are invalid
    with pytest.raises(ValueError):
        date_temp_setup.set_date_from_ints("a", "b", "c")


def test_date_from_ints_with_first_arg_invalid(date_temp_setup):
    # verify that error is returned if only first argument is invalid
    with pytest.raises(ValueError):
        date_temp_setup.set_date_from_ints("a", 8, 9)


def test_date_from_ints_with_second_arg_invalid(date_temp_setup):
    # verify that error is returned if only second argument is invalid
    with pytest.raises(ValueError):
        date_temp_setup.set_date_from_ints(2020, "a", 9)


def test_date_from_ints_with_third_arg_invalid(date_temp_setup):
    # verify that error is returned if only third argument is invalid
    with pytest.raises(ValueError):
        date_temp_setup.set_date_from_ints(2020, 8, "a")


def test_str_method():
    # verify that __str__ method returns correct information
    valid_date = datetime.date(1987, 6, 20)
    test1 = DateTemp(valid_date, 98)
    assert str(test1) == 'The temperature on 1987-06-20 was 98 F'


def test_repr_method():
    # verify that the __repr__ method returns correct information
    valid_date = datetime.date(1987, 6, 20)
    test1 = DateTemp(valid_date, 98)
    assert repr(test1) == 'The temperature on 1987-06-20 was 98 F'


def test_date_sorting():
    # verify that function sorts by date properly
    test1 = DateTemp((datetime.date(1987, 6, 20)), 98)
    test2 = DateTemp((datetime.date(1965, 8, 5)), 85)
    items = [test1,test2]
    result = sorted_by_date(items)
    assert result == [test2, test1]


def test_temp_sorting():
    # verify that function sorts by temp properly
    test1 = DateTemp((datetime.date(1987, 6, 20)), 98)
    test2 = DateTemp((datetime.date(1965, 8, 5)), 85)
    items = [test1,test2]
    result = sorted_by_date(items)
    assert result == [test2, test1]


"""
Identification of at least 5 tests that are not necessary because 
they are in a equivalence class that is already being tested:
1. You would not need to test the addition of strings of various 
lengths or capitalization, etc., as if one string passed in fails, 
they should all fail.
2. A negative temperature does not need to be tested, since all 
ints/floats are accepted and an int and float are already tested.
3. Testing temp sorting with extra objects and temps is likely not 
necessary as they have already been tested once.
4. Same as above with dates.
5. Testing with additional invalid dates is not necessary, as an 
invalid date has already been shown to have been rejected as expected.
6. * bonus answer - testing negative numbers for datetime.date 
would not be necessary, as it has already been shown to reject 
invalid dates


"""



















