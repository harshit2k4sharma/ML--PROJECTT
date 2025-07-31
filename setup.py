from setuptools import find_packages, setup
from typing import List


HYPHEN_E_DOT = '-e .' # -e indicates that
def get_requirements(file_path: str) -> List[str]: # file_path str mein hai aur ek list retrun karego jo str mein hogi
    '''
    this function will return the list of requirements 
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines() # requirements wali mein se ek ek line read karega one one element
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name="mlproject",
    version='0.0.1',
    author="Harshit",
    author_email="harshitsharma2k4@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)


# setup.py file for the ML project 
# the -e . indicates that the package is editable, meaning changes to the source code will be reflected without needing to reinstall the package.# This is useful during development.
# The requirements.txt file contains the dependencies needed for the project,