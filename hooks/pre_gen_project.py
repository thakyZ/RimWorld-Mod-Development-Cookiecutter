#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to hook Cookiecutter's pre gen project script"""

from logging import DEBUG, basicConfig, getLogger

basicConfig(level=DEBUG)
logger = getLogger("pre_gen_project")
