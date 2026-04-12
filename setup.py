from setuptools import find_packages, setup
from typing import List
HYPHEN_E_DOT = "-e ."
#note that we cant write every packages manually when there are 100s of them so we create a function
def get_requirements(file_path:str)-> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n"," ")for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
name='mlproject',
version = '0.0.1',
author = 'Ayush Singh',
author_email = 'ayushsingh20112004@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')


)