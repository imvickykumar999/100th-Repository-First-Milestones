# Morsetor Package is in [Master Branch](https://github.com/imvickykumar999/100th-Repository-Morsetor-python-Package/tree/master) of this Repository.

[![tutorial](https://github.com/imvickykumar999/100th-Repository-Morsetor-python-Package/blob/main/pypi%20screenshot.png?raw=true)](https://github.com/imvickykumar999/100th-Repository-Morsetor-python-Package/blob/master/morse%20tutorial.ipynb)

## ...uploaded using, 

    `from morsetor import upload as up`
    `up.github()`

## Direction to Publish Package on Python Package Index...

### [Open this Folder (contain all files required for publishing)](https://github.com/imvickykumar999/100th-Repository-Morsetor-python-Package/tree/master)
### Delete following Folders : 

`hidden file = .git`
[`dist`](https://github.com/imvickykumar999/100th-Repository-Morsetor-python-Package/tree/master/dist)
[`your_module.egg-info`](https://github.com/imvickykumar999/100th-Repository-Morsetor-python-Package/tree/master/morsetor.egg-info)

#### now, ....

        1. creating a folder: any name
        2. creating a sub fodler : is_palindrom_bala
        3. creating a sub folder :is_palindrome_bala
        4. create __init__.py inside 2nd is_palindrome folder
        5. create setup.py inside 1st is_palindrome folder
        6. pip install setuptools
        7. import setuptools
        8. define setup configuration inside setup.py file
        9. include manifest.in
        10. include readme.txt
        11.include license.txt
        13. run `python setup.py sdist` cmd in terminal
        14. install twine package :'pip install twine'
        15. `twine upload dist/*`

## Congratulations !!! ...it's published on your PyPi account.
