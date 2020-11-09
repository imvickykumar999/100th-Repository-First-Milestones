from setuptools import setup

setup(
    name = 'githubpypiuploader', # while installing pacakge, change name to something unique on pypi.org
    version = '0.0.1', # use different version if updated, like '0.0.2'
    description = 'Website : https://vixportfoliowithflask.herokuapp.com/skills',
    long_description = open('README.md').read(),
    url = 'https://github.com/imvickykumar999',
    author = 'Vicky Kumar',
    keywords = ['GitHub Uploader','Morse','custom','python package','function and class','3D line',
    '3D plane', 'angle bw planes or line', 'distance bw point and plane'],
    license = 'MIT',
    packages = ['githubpypiuploader'], # while importing package
    install_requires = ['']
)
