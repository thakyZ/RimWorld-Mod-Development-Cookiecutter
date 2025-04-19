#!/usr/bin/env python
# -*- coding: utf-8 -*-

from logging import INFO, basicConfig, getLogger
from os.path import realpath, curdir
from shutil import copytree, rmtree
from pathlib import Path
from subprocess import run

basicConfig(level=INFO)
logger = getLogger("post_gen_project")

PROJECT_DIRECTORY = realpath(curdir)
ALL_TEMP_FOLDERS = ["licenses","load_folder_template"]
ALL_LOAD_FOLDERS = ["{{ cookiecutter.supported_versions }}"]

def make_load_folders(load_folders: list[str]) -> None:
    for load_folder in load_folders:
        copytree(Path(PROJECT_DIRECTORY, "load_folder_template"), Path(PROJECT_DIRECTORY, f"{load_folder}"))


def remove_temp_folders(temp_folders: list[str]) -> None:
    for folder in temp_folders:
        logger.debug("Remove temporary folder: %s", folder)
        rmtree(folder, ignore_errors=True)

if __name__ == "__main__":
    make_load_folders(ALL_LOAD_FOLDERS)
    remove_temp_folders(ALL_TEMP_FOLDERS)
    msg = ""
    # try to run git init
    try:
        run(["git", "init", "-q"])
        run(["git", "checkout", "-b", "main"])
        run(["git", "add", "."])
        run(["git", "commit", "-q", "-m", "initial commit"])
    except Exception:
        msg += """
Your mod template is ready!  Next steps:

1. `cd` into your new directory and initialize a git repo
   (this is also important for version control!)

     cd {{ cookiecutter.mod_name }}
     git init -b main
     git add .
     git commit -m 'initial commit'"""
    else:
        msg +="""
Your mod template is ready!  Next steps:

1. `cd` into your new directory

     cd {{ cookiecutter.mod_name }}"""

{% if cookiecutter.github_repository_url != 'provide later' %}
    msg += """
2. Create a github repository with the name '{{ cookiecutter.mod_name }}':
   https://github.com/{{ cookiecutter.github_repository_url }}.git

3. Add your newly created github repo as a remote and push:

     git remote add origin https://github.com/{{ cookiecutter.github_repository_url }}.git
     git push -u origin main

4. The following default URLs have been added to `setup.cfg`:

    Bug Tracker = https://github.com/{{ cookiecutter.github_repository_url }}/issues
    Documentation = https://github.com/{{ cookiecutter.github_repository_url }}#README.md
    Source Code = https://github.com/{{ cookiecutter.github_repository_url }}
    User Support = https://github.com/{{ cookiecutter.github_repository_url }}/issues

    These URLs will be displayed on your plugin's napari hub page.
    You may wish to change these before publishing your plugin!"""

{% else %}
    msg += """
2. Create a github repository for your plugin:
   https://github.com/new

3. Add your newly created github repo as a remote and push:

     git remote add origin https://github.com/your-repo-username/your-repo-name.git
     git push -u origin main

   Don't forget to add this url to setup.cfg!

     [metadata]
     url = https://github.com/your-repo-username/your-repo-name.git

4. Consider adding additional links for documentation and user support to setup.cfg
   using the project_urls key e.g.

    [metadata]
    project_urls =
        Bug Tracker = https://github.com/your-repo-username/your-repo-name/issues
        Documentation = https://github.com/your-repo-username/your-repo-name#README.md
        Source Code = https://github.com/your-repo-username/your-repo-name
        User Support = https://github.com/your-repo-username/your-repo-name/issues"""
{% endif %}

    print(msg)
