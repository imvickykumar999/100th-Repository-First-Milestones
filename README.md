# >>> [PYPI Uploader](https://github.com/imvickykumar999/100th-Repository-Morsetor-python-Package/tree/main/PYPI%20python%20package)

    >>> import vixuploader as vix
    >>> help(vix)
    Help on package vixuploader:

    NAME
        vixuploader - # when you import package for the first time, this __init__.py file runs automatically.

    PACKAGE CONTENTS
        github
        morse
        pypi
        vixtor

    FILE
        c:\users\vicky\desktop\python\package_python\pypi python package\100th-repository-morsetor-python-package\pypi python package\vixuploader\__init__.py

    >>>

## Open CMD and type python, [then write below code](https://github.com/imvickykumar999/100th-Repository-Morsetor-python-Package/blob/master/RUNME.py)...

                import os

                os.system('git clone https://github.com/imvickykumar999/100th-Repository-Morsetor-python-Package.git')

                # =========( DO IT MANUALLY )============
                
                # os.system('cd 100th-Repository-Morsetor-python-Package')
                #
                # os.system('cd "PYPI python package"')
                #
                # os.system('python "100th-Repository-Morsetor-python-Package\PYPI python package\RUNME.py"')
                #
                # ======================================



# vixuploader package is in [Master Branch](https://github.com/imvickykumar999/100th-Repository-Morsetor-python-Package/tree/master) of this Repository.

[![pypi](https://github.com/imvickykumar999/100th-Repository-Morsetor-python-Package/blob/main/screenshot.png?raw=true)](https://pypi.org/project/vixuploader/)


## ...uploading on github using, 

    `from vixuploader import github as g`
    `g.upload()`

## Direction to Publish Package on Python Package Index...

### [Open this Folder (contain all files required for publishing)](https://github.com/imvickykumar999/100th-Repository-Morsetor-python-Package/tree/master)
### Delete following Folders : 

    `hidden file = .git`
    `dist`
    `your_module.egg-info`

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
