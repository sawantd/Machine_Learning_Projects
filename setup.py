from setuptools import setup,find_packages
from typing import List

def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement
    mentioned in requirements.txt file

    return: This function is going to return a list which contains 
    name of libraries mentioned in requirements.txt file
    """
    with open("requirements.txt") as requirement_file:
        return requirement_file.readlines().remove("-e .")
  


setup(
    name="housing-predictor",
    version="0.0.4",
    author="Darshana",
    description="This is a first FSDS NOV Batch ML Project",
    packages=find_packages(),      #returns all the folders as packages where it finds __init__
    install_requires=get_requirements_list())
