from multiprocessing import AuthenticationError
from xml.etree.ElementTree import VERSION
from setuptools import setup
from typing import List

#Declaring variable for setup function
PROJECT_NAME="housing-prediction"
VERSION="0.0.1"
AUTHOR="Gopal Rajpurohit"
DESCRIPTION="this is end to end first ML project"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description : this function is going to return list of requirements 
    that mentioned in requirements.txt file.

    return : this fuction is going to return a list which contain name
    of libraries mentioned in requirements.txt file.
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGES,
    install_requires=get_requirements_list()
)