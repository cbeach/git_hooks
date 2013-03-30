"""
    The hook scripts will iterate through their respective lists, executing the names scripts
"""

POST_COMMIT = ['restore_permissions']
RESTORE_PERMISSIONS = [
    {
        'path': '',
        'mode': '',
        'owner': '',
        'group': '',
    }
]
POST_MERGE = []
