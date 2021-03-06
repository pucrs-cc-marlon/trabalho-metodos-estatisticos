#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":

    if os.environ.get('AMBIENTE') == 'dev':
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "trabalho_me_i.settings.dev_settings")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "trabalho_me_i.settings.server_settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
