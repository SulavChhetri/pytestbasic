from setuptools import setup

setup(
    name="dictionaryvalidator",
    version="1.0.0",
    description="This is a dictionary validator package.",
    long_description="This package invokes a dictionary validator function which takes both input dictionary and it's validation dictionary and determines whether the dictionary is valid or not",
    author="Sulav",
    packages=['dictionaryvalidator'],
    install_requrires=['pytest']
    )