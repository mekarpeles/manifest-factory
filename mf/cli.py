#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    cli.py
    ~~~~~~

    Command line utility for the manifest factory.

    :copyright: (c) 2015 by IIIF.
    :license: see LICENSE for more details.
"""

import argparse
import getpass
from . import __title__, __version__, factory

def argparser():
    """Creates a command line ArgumentParser for mf."""
    parser = argparse.ArgumentParser(description=__title__)
    parser.add_argument('-v', help="Displays the version of mf",
                        action="version", version="%s v%s"
                        % (__title__, __version__))
    return parser

def main():
    parser = argparser()
    args = parser.parse_args()
    # Invoke mf according to parser opts
    fac = factory.ManifestFactory()

if __name__ == "__main__":
    main()
