import os

from fabric.api import local, task

hooks_dir = os.path.join(os.path.abspath(__file__), 'hooks')
project_root_dir = local('git rev-parse --show-toplevel')
git_hooks_dir = os.path.join(project_root_dir, '.git/hooks')

@task
def igh():
    """
        igh (install git hooks)
        removes the .git/hooks directory and replaces it with the one in this project

    """
    local('rm -rf {}'.format(git_hooks_dir))
    local('cp -r {} {}'.format(hooks_dir, git_hooks_dir))
