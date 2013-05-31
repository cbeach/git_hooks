
#Activate the virtual environment if there's one for this project
from settings import UNDER_VIRTUALENV, VIRTUALENV
if UNDER_VIRTUALENV is True:
    activate_this = '/usr/local/share/python-environments/{}/bin/activate_this.py'.format(
        VIRTUALENV)
    execfile(activate_this, dict(__file__=activate_this))

from sh import pip
from settings import REQUIREMENTS_PATH

f = open(REQUIREMENTS_PATH, 'w')
f.write(str(pip.freeze()))
