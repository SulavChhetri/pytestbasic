from src.validator import Validator
import pytest

@pytest.fixture
def input_dictionary_data():
    input_dictionary = {
            "name": "Sulav",
            "age": 22,
            "city": "Syangja",
            "isEngineer": True
        }
    validation_dictionary = {
        "name": {
            "type": str,
            'minlength': 4,
            'maxlength': 10
        },
        'age': {
            'type': int,
            'minimum': 0,
            'maximum': 150
        },
        'city': {
            'type': str
        },
        'isEngineer': {
            'type': bool
        }
    }
    return [input_dictionary,validation_dictionary]

def test_type1():
    test_value = 'Sulav'
    test_rule = str
    input = "name"
    assert Validator.type1(test_value,test_rule,input)==None

def test_minlength():
    test_value = "Putalibazar"
    test_min_length = 5
    input = 'city'
    # Check if the length of the value is greater than or equal to test_min_length
    assert Validator.minlength(test_value,test_min_length,input)==None

def test_maxlength():
    test_value = "Putalibazar"
    test_max_length = 25
    input = 'city'
    # check if the length of the value is less than or equal to the test_max_length
    assert Validator.maxlength(test_value,test_max_length,input)==None

def test_minimum():
    test_value = 22
    test_min = 0
    input = "age"
    # check if the test_value is greater than or equal to the test_min
    assert Validator.minimum(test_value,test_min,input)==None

def test_maximum():
    test_value = 22
    test_max = 150
    input = 'age'
    # check if the test_value is less than or equal to the test_min
    assert Validator.maximum(test_value,test_max,input)==None

def test_validator(input_dictionary_data):
   assert input_dictionary_data[0].keys()==input_dictionary_data[1].keys()
   assert Validator.type1("Sulav",str,"name")==None
   assert Validator.minlength("Sulav",4,"name")==None
   assert Validator.maxlength("Sulav",10,"name")==None
   assert Validator.minimum(22,0,"age")==None
   assert Validator.maximum(22,150,"age")==None