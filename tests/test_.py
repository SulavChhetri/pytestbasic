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
    # Pass case
    test_value = 'Sulav'
    test_rule = str
    input = "name"

    # Fail case
    test_value1 = True
    test_rule1 = str
    input1 = "name"

    assert Validator.type1(test_value,test_rule,input)==None
    assert Validator.type1(test_value1,test_rule1,input1)==False

def test_minlength():
    # Pass case
    test_value = "Putalibazar"
    test_min_length = 5
    input = 'city'

    # Fail case
    test_value1 = "Puta"
    test_min_length1 = 5
    input1 = 'city'

    # Check if the length of the value is greater than or equal to test_min_length
    assert Validator.minlength(test_value,test_min_length,input)==None
    assert Validator.minlength(test_value1,test_min_length1,input1)==False

def test_maxlength():
    # Pass case
    test_value = "Putalibazar"
    test_max_length = 25
    input = 'city'

    # Fail Case
    test_value1 = "Putalibazarsadajkjsdkjasdkasd"
    test_max_length1 = 25
    input1 = 'city'


    # check if the length of the value is less than or equal to the test_max_length
    assert Validator.maxlength(test_value,test_max_length,input)==None
    assert Validator.maxlength(test_value1,test_max_length1,input1)==False

def test_minimum():
    #Pass case
    test_value = 22
    test_min = 0
    input = "age"

    #Fail case
    test_value1 = -22
    test_min1 = 0
    input1 = "age"

    # check if the test_value is greater than or equal to the test_min
    assert Validator.minimum(test_value,test_min,input)==None
    assert Validator.minimum(test_value1,test_min1,input1)==False

def test_maximum():
    #Pass case
    test_value = 22
    test_max = 150
    input = 'age'

    #Fail case
    test_value1 = 220
    test_max1 = 150
    input1 = 'age'

    # check if the test_value is less than or equal to the test_min
    assert Validator.maximum(test_value,test_max,input)==None
    assert Validator.maximum(test_value1,test_max1,input1)==False

def test_validator(input_dictionary_data):
   assert input_dictionary_data[0].keys()==input_dictionary_data[1].keys()
   #None case
   assert Validator.type1("Sulav",str,"name")==None
   assert Validator.minlength("Sulav",4,"name")==None
   assert Validator.maxlength("Sulav",10,"name")==None
   assert Validator.minimum(22,0,"age")==None
   assert Validator.maximum(22,150,"age")==None
   
   #Fail Case
   assert Validator.type1(True,str,"name")== False
   assert Validator.minlength("Sul",4,"name")==False
   assert Validator.maxlength("SulavThapaChhetri",10,"name")==False
   assert Validator.minimum(-22,0,"age")==False
   assert Validator.maximum(220,150,"age")==False