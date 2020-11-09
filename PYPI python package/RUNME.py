
import os

os.system('git clone https://github.com/imvickykumar999/100th-Repository-Morsetor-python-Package.git')

os.system('pip install -r requirements.txt')

os.system('python setup.py sdist')

os.system('twine upload dist/*')
