import pytest
from retirement import *


# testing valid inputs and valid boundary values for equivalence
# classes
@pytest.mark.parametrize("test_input, expected", [
    (1900, (65, 0)), # tests lower boundary of first partition
    (1937, (65, 0)), # tests upper boundary of first partition
    (1938, (65, 2)), # tests next partition
    (1939, (65, 4)), # tests next partition
    (1940, (65, 6)), # tests next partition
    (1941, (65, 8)), # tests next partition
    (1942, (65, 10)), # tests next partition
    (1943, (66, 0)), # tests lower boundary of middle ranged partition
    (1954, (66, 0)), # tests upper boundary of middle ranged partition
    (1955, (66, 2)), # tests next partition
    (1956, (66, 4)), # tests next partition
    (1957, (66, 6)), # tests next partition
    (1958, (66, 8)), # tests next partition
    (1959, (66, 10)), # tests next partition
    (1960, (67, 0)), # tests lower boundary of upper partition
    # (2999, (67, 0)) # tests upper boundary of upper partition
    # commented out after discussion with teacher as previous test
    # (1960) is the same
])
def test_good_inputs_retirement_ages(test_input, expected):
    assert calculate_retirement_age(test_input) == expected


# testing invalid edge cases and other invalid inputs for ValueError
@pytest.mark.parametrize("test_input", [
    (1899), # test one lower than lower boundary
    (3000), # test one larger than upper boundary
    ("string"), # test string
    (-10), # test negative number
    (0), # test 0
])
def test_invalid_birth_years(test_input): # wrapper to pass in test
    # input
    with pytest.raises(ValueError):
        calculate_retirement_age(test_input)


# test that verifiers are correctly raising errors with various
# invalid inputs
@pytest.mark.parametrize("birth_year, birth_month, age_years, "
                         "age_months ", [
    (1899, 2, 66, 9), # invalid birth year (one too low)
    (3000, 2, 66, 9), # invalid birth year (one too high)
    ("string", 2, 66, 9), # string passed into birth year
    (-5, 2, 66, 9), # negative passed into birth year
    (1940, 0, 66, 9), # invalid birth month (one too low)
    (1951, -5, 66, 9), # invalid birth month (negative)
    (1951, 13, 66, 9), # invalid birth month (one too high)
    (1951, "string", 66, 9), # invalid birth month (string)
    (1951, 2, 64, 9), # invalid age years (one too low)
    (1939, 2, 68, 9), # invalid age years (one too high)
    (1951, 2, -5, 9), # invalid age years (negative)
    (1957, 2, "string", 9), # invalid age years (string)
    (1951, 2, 66, -1), # invalid age months (one too low as well as
    # negative)
    (1951, 2, 66, 12), # invalid age months (one too high)
    (1951, 2, 66, "string"), # invalid age months (string)
    ("string", "string", "string", "string") # all arguments incorrect
    ])
def test_invalid_inputs_for_calculate_retirement_date_function(
        birth_year, birth_month, age_years, age_months): # wrapper for test
    # info
    with pytest.raises(ValueError):
        calculate_retirement_date(birth_year, birth_month,
                                  age_years, age_months)

# test verifiers with boundary cases for each equivalence class
@pytest.mark.parametrize("birth_year, birth_month, age_years, "
                         "age_months, expected ", [
    (1900, 2, 66, 9, (1966, 11)), # test lower birth year boundary
    (2999, 2, 66, 9, (3065, 11)), # test upper birth year boundary
    (1942, 1, 66, 3, (2008, 4)), # test lower birth month boundary
    (1942, 12, 66, 0, (2008, 12)), # test upper birth month boundary
    (1942, 2, 65, 9, (2007, 11)), # test lower age years boundary
    (1942, 2, 67, 9, (2009, 11)), # test upper age years boundary
    (1942, 2, 66, 0, (2008, 2)), # test lower age months boundary
    (1942, 1, 66, 11, (2008, 12)), # test upper age months boundary

])
def test_edge_cases_for_calculate_retirement_date_function(
        birth_year, birth_month, age_years, age_months, expected):
    assert calculate_retirement_date(birth_year, birth_month,
                                     age_years, age_months) == expected

# test that the if statement properly executes and
# increments/decrements values
def test_if_the_if_statement_executes():
    assert calculate_retirement_date(1955, 11, 66, 2) == (2022, 1)



