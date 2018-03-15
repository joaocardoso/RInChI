from setuptools import setup, find_packages
from itertools import chain

requirements = [
    'numpy>=1.13',
    'scipy>=0.19'
]

setup(
    name='rinchi_tools',
    version=1.0.0,
    packages=find_packages(),
    install_requires=requirements,
    author='C.H.G. Allen, N.A. Parker, B. Hammond, D.F. Hampshire',
    author_email='',
    description='International chemical identifier for reactions',
    license='Apache License Version 2.0',
    url='https://github.com/joaocardoso/RInChI',
    long_description="",
    keywords=['chemoinformatics'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Programming Language :: Python :: 3],
)
