#Activate the virtual environment if there's one for this project
from settings import UNDER_VIRTUALENV, VIRTUALENV
if UNDER_VIRTUALENV is True:
    activate_this = '/usr/local/share/python-environments/{}/bin/activate_this.py'.format(
        VIRTUALENV)
    execfile(activate_this, dict(__file__=activate_this))

from settings import RESTORE_PERMISSIONS
from sh import chmod, chown

for perm in RESTORE_PERMISSIONS:
    chmod(perm['mode'], perm['path'])
    chown('{}:{}'.format(perm['owner'], perm['group']), perm['path'])
