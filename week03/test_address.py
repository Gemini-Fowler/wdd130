from address import extract_city, extract_state, extract_zipcode
import pytest

def test_extract_city():
    assert extract_city("123 Main Street, Chicago, IL 12345") == "Chicago"

def test_extract_state():
    assert extract_state("123 Main Street, Chicago, IL 12345") == "IL"

def test_extract_zipcode():
    assert extract_zipcode("123 Main Street, Chicago, IL 12345")== "12345"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])