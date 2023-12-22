#! /usr/bin/env python
# encoding: utf-8

import os
import io
import re
import sys

from setuptools import setup, find_packages

cwd = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(cwd, "README.rst"), encoding="utf-8") as fd:
    long_description = fd.read()


def file_find_version(filepath):

    with io.open(filepath, encoding="utf-8") as fd:

        VERSION = None

        regex = re.compile(
            r"""
        (                # Group and match
            VERSION      #    Match 'VERSION'
            \s*          #    Match zero or more spaces
            =            #    Match and equal sign
            \s*          #    Match zero or more spaces
        )                # End group
        "
        (                # Group and match
            \d\.\d\.\d  #    Match digit.digit.digit e.g. 1.2.3
        )                # End of group
        "
        """,
            re.VERBOSE,
        )

        for line in fd:

            match = regex.match(line)
            if not match:
                continue

            # The second parenthesized subgroup.
            VERSION = match.group(2)
            break

        else:
            sys.exit("No VERSION variable defined in {} - aborting!".format(filepath))

    return VERSION


def find_version():

    wscript_VERSION = file_find_version(filepath=os.path.join(cwd, "wscript"))

    return wscript_VERSION


version = find_version()

setup(
    name="bughawk",
    description="A tool for checking a set of source files for common bugs.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    version=version,
    packages=find_packages(),
    install_requires=["gitignorefile==1.1.2"
    ],
    entry_points={"console_scripts": ["bughawk = bughawk.__main__:main"]},
)
