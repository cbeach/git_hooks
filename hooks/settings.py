"""
    The hook scripts will iterate through their respective lists, executing the names scripts
"""
import os

GIT_DIR = os.environ['GIT_DIR']

#Virtual Environment values
UNDER_VIRTUALENV = True
VIRTUALENV = 'git_hooks'
REQUIREMENTS_PATH = os.path.join(os.environ['GIT_DIR'], 'requirements.txt')

POST_COMMIT = ['restore_permissions', 'refresh_requirements']
RESTORE_PERMISSIONS = [
    {
        'path': os.path.join(GIT_DIR, 'post-commit'),
        'mode': '770',
        'owner': 'mcsmash',
        'group': 'mcsmash',
    }
]
POST_MERGE = []
