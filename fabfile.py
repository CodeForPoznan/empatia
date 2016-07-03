# -*- coding: utf-8 -*-

u"""
.. module:: fabfile
Be aware, that becaus fabric doesn't support py3k You need to execute this
particular script using Python 2.
"""

import contextlib

from fabric.api import cd
from fabric.api import env
from fabric.api import prefix
from fabric.api import run

env.user = 'root'
env.hosts = ['bankempatii.pl']
env.forward_agent = True


def update():
    u"""Function defining all steps required to properly update application."""

    with contextlib.nested(
        cd('/var/www/bankempatii_pl'),
        prefix('nvm use v6.2.0')
    ):
        run('git pull')
        run('npm install')
        run('gulp')

    run('service apache2 restart')
