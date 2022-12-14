class Validator:
    def __init__(self, input_dictionary, validation_dictionary):
        self.input_dictionary = input_dictionary
        self.validation_dictionary = validation_dictionary

    def type1(value, standard, input):
        if not (type(value) == standard):
            print(
                f'The type of {input} must be {standard} but is {type(value)}')
            return False

    def minlength(value, standard, input):
        if not (len(value) >= standard):
            print(
                f'The minimum length of {input} must be {standard} but is {len(value)}')
            return False

    def maxlength(value, standard, input):
        if not (len(value) <= standard):
            print(
                f'The maxmimum length of {input} must be {standard} but is {len(value)}')
            return False

    def minimum(value, standard, input):
        if not (value >= standard):
            print(
                f'The minimum value of {input} must be {standard} but is {value}')
            return False

    def maximum(value, standard, input):
        if not (value <= standard):
            print(
                f'The maximum value of {input} must be {standard} but is {value}')
            return False

    def validator(self):
        if not self.input_dictionary.keys() == self.validation_dictionary.keys():
            return False
        else:
            for key in self.validation_dictionary.keys():
                value = self.input_dictionary.get(key)
                rule = self.validation_dictionary.get(key)
                for function in rule.keys():
                    if (function == 'type' and Validator.type1(self,value, rule[function], key) == False):
                        return False
                    elif (function == 'minlength' and Validator.minlength(self,value, rule[function], key) == False):
                        return False
                    elif (function == 'maxlength' and Validator.maxlength(self,value, rule[function], key) == False):
                        return False
                    elif (function == 'minimum' and Validator.minimum(self,value, rule[function], key) == False):
                        return False
                    elif (function == 'maximum' and Validator.maximum(self,value, rule[function], key) == False):
                        return False
            return True