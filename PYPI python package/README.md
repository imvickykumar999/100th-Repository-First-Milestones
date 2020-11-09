Run [`py upload.py`](https://github.com/imvickykumar999/Internship-Study/blob/master/upload.py)

[Uploading Files in Existing Repository on github using python script.](https://github.com/imvickykumar999/git-bash/tree/master)

import time

print("Print now")
time.sleep(4.2)
print("Printing after 4.2 seconds")


[C:\Users\Vicky\Desktop\python\My APPs\brython\gitcmd>cd gitbash](https://github.com/imvickykumar999/git-bash/blob/master/upload.py)

C:\Users\Vicky\Desktop\python\My APPs\brython\gitcmd\before gitbash>py upload.py

DEKH LIYA CHAL NIKAL

1). git init
Initialized empty Git repository in C:/Users/Vicky/Desktop/python/My APPs/brython/gitcmd/before gitbash/.git/

2). git add .

Enter files name to Upload selected files (or, Press ENTER to Upload All...) :

3). git commit -m "Adding files"
[master (root-commit) 0534954] Adding files
5 files changed, 232 insertions(+)
create mode 100644 __pycache__/morse.cpython-38.pyc
create mode 100644 index.html
create mode 100644 morse.py
create mode 100644 readme.md
create mode 100644 upload.py

4). git remote add origin https://github.com/...
Enter the github Username : imvickykumar999
Enter Existing Repository : git-bash

5). git pull origin master
warning: no common commits
remote: Enumerating objects: 8, done.
remote: Counting objects: 100% (8/8), done.
remote: Compressing objects: 100% (8/8), done.
remote: Total 8 (delta 0), reused 8 (delta 0), pack-reused 0
Unpacking objects: 100% (8/8), 3.32 KiB | 141.00 KiB/s, done.
From https://github.com/imvickykumar999/git-bash
* branch            master     -> FETCH_HEAD
* [new branch]      master     -> origin/master
fatal: refusing to merge unrelated histories

6). git push origin master
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 8 threads
Compressing objects: 100% (7/7), done.
Writing objects: 100% (8/8), 4.30 KiB | 2.15 MiB/s, done.
Total 8 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), done.
To https://github.com/imvickykumar999/git-bash.git
+ 2e9e533...0534954 master -> master (forced update)

C:\Users\Vicky\Desktop\python\My APPs\brython\gitcmd\before gitbash>
