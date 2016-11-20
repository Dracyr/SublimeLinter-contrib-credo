#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Per-Victor Persson
# Copyright (c) 2016 Per-Victor Persson
#
# License: MIT
#

"""This module exports the Credo plugin class."""

from SublimeLinter.lint import Linter, util


class Credo(Linter):
    """Provides an interface to credo."""

    syntax = 'elixir'
    cmd = 'mix credo list --all --format=oneline @'
    executable = 'mix credo'
    version_args = 'credo --version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.5.3'
    regex = r'^\[.\].((?P<error>[↗↑])|(?P<warning>.)).(?P<filename>.+?):(?P<line>\d+):?(?P<col>\d+)? (?P<message>.+)$'
    multiline = False
    tempfile_suffix = None
    error_stream = util.STREAM_BOTH

