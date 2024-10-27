#!/bin/bash

####################################################################################################
# This script is used to run python with sudo. It is used to run the python script with sudo
# without requiring a password. This is useful when the python script needs to run as root.
#
# Don't require a password running sudo python
#   sudo visudo -f /etc/sudoers.d/python
#
# Add a line of the form:
#   <user> <host> = (root) NOPASSWD: <full path to python>
# For example:
#   brk brk.local = (root) NOPASSWD:/Users/brk/_private/repos/tools/unreal/tools-python-unreal-cli/.venv/bin/python
#
# Set this script as the python interpreter in pycharm
#   File -> Settings -> Project -> Project Interpreter -> Gear Icon -> Add -> Existing Environment -> Interpreter
#   -> /path/to/python-sudo.sh
#
# Run your python script in pycharm
####################################################################################################

sudo .venv/bin/python "$@"

####################################################################################################
# How To