# Berkeleytime-Server
A server for the clean, totally not pornographic, snapchat story for Berkeley students

Alright, so running this is a bit tricky currently.

First go to this link: https://github.com/martinp/pysnap

Clone that git repository, and make sure you have the python "requests" library installed. Then, go into that folder and run 
"python setup.py install". Just follow the instructions given in that repo.

I have a requirements.txt, so I guess you should run "pip -r requirements.txt" as well. If that doesn't work, do the above instructions. 

You'll also need to make a file called "userAuth.py" and populate it with two variables: USERNAME and PASSWORD, which should be the desired snapchat account's username and password. Put this in the same folder as server.py.

Then, to run this script, just do "python server.py" and it should work fine. This is built on Python 2.7, so it should work
on newer versions as well. 
