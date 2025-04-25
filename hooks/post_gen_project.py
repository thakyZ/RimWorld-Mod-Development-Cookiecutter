#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to hook Cookiecutter's post gen project script"""

from logging import INFO, basicConfig, getLogger
from os.path import realpath, curdir
from shutil import copytree, rmtree
from pathlib import Path
from subprocess import run, check_output

basicConfig(level=INFO)
logger = getLogger("post_gen_project")

PROJECT_DIRECTORY: str = realpath(curdir)
ALL_TEMP_FOLDERS: list[str] = ["licenses", "load_folder_template"]
MOD_NAME_RAW: str = "{{ cookiecutter.mod_name }}"
MOD_NAME: str = "{{ cookiecutter.mod_name.replace(' ', '_') }}"
ALL_LOAD_FOLDERS: list[str] = "{{ cookiecutter.supported_versions }}".split(',')
GIT_REPOSITORY_URL: str = "{{ cookiecutter.git_repository_url }}"


def make_load_folders(load_folders: list[str]) -> None:
    """Creates a new folder for each supported version.

    Args:
        load_folders (list[str]): The list of supported versions.
    """
    for load_folder in load_folders:
        logger.debug("Created load folder folder: %s", load_folder)
        copytree(
            Path(PROJECT_DIRECTORY, "load_folder_template"),
            Path(PROJECT_DIRECTORY, f"{load_folder}")
        )


def remove_temp_folders(temp_folders: list[str]) -> None:
    """Deletes each temporary folder from the system drive.

    Args:
        temp_folders (list[str]): The list of temporary folders to delete.
    """
    for folder in temp_folders:
        logger.debug("Remove temporary folder: %s", folder)
        rmtree(folder, ignore_errors=True)


if __name__ == "__main__":
    make_load_folders(ALL_LOAD_FOLDERS)
    remove_temp_folders(ALL_TEMP_FOLDERS)
    msg: str = ""
    # try to run git init
    try:
        run(["git", "init", "-q"], check=True)
        run(["git", "checkout", "-b", "main"], check=True)
        run(["git", "add", "."], check=True)
        ret: list[str] = str(
            check_output(" ".join(["git", "config", "user.signingkey"]), shell=True)
        ).split('\\n')
        if len(ret) >= 1 and ret[0] != '':
            run(["git", "commit", "-Ss", "-q", "-m", "initial commit"], check=True)
        else:
            run(["git", "commit", "-q", "-m", "initial commit"], check=True)
    except Exception as error:  # pylint: disable=W0718
        logger.debug(error)
        msg += f"""
Your mod template is ready!  Next steps:

1. `cd` into your new directory and initialize a git repo
    (this is also important for version control!)

    cd RimWorld-{MOD_NAME}
    git init -b main
    git add .
    git commit -m 'initial commit'"""
    else:
        msg += """
Your mod template is ready!  Next steps:

1. `cd` into your new directory

    cd {MOD_NAME_RAW}"""

    if not GIT_REPOSITORY_URL.startswith("https://"):
        msg += """
2. Create a github repository with the name 'RimWorld-{MOD_NAME}':
    {GIT_REPOSITORY_URL}.git

3. Add your newly created github repo as a remote and push:

    git remote add origin {GIT_REPOSITORY_URL}.git
    git push -u origin main

4. The following default URLs have been added to `setup.cfg`:

    Bug Tracker = {GIT_REPOSITORY_URL}/issues
    Documentation = {GIT_REPOSITORY_URL}#README.md
    Source Code = {GIT_REPOSITORY_URL}
    User Support = {GIT_REPOSITORY_URL}/issues

    These URLs will be displayed on your plugin's napari hub page.
    You may wish to change these before publishing your plugin!"""

    else:
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

    print(msg)
