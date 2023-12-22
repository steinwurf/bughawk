=======
BugHawk
=======

.. image:: ./icon.png
   :height: 200px
   :align: center


|PyPi| |Waf Python Tests| |Black| |Flake8|


.. |PyPi| image:: https://badge.fury.io/py/bughawk.svg
    :target: https://badge.fury.io/py/bughawk

.. |Waf Python Tests| image:: https://github.com/steinwurf/bughawk/actions/workflows/python-waf.yml/badge.svg
   :target: https://github.com/steinwurf/bughawk/actions/workflows/python-waf.yml

.. |Flake8| image:: https://github.com/steinwurf/bughawk/actions/workflows/flake.yml/badge.svg
    :target: https://github.com/steinwurf/bughawk/actions/workflows/flake.yml

.. |Black| image:: https://github.com/steinwurf/bughawk/actions/workflows/black.yml/badge.svg
      :target: https://github.com/steinwurf/bughawk/actions/workflows/black.yml

BugHawk is a tool for finding common bugs and issues in Steinwurf projects.

Installation
------------

Install the ``bughawk`` tool using ``pip``::

      python -m pip install bughawk

Alternatively you can also use ``pipx`` for the installation (this works in ubuntu 23.04)::

      pipx install bughawk

Usage
-----
You'll now be able to use the `bughawk` command line tool. The following will list
the available sw commands::

      bughawk -l

Update
------
To update BugHawk use pip::

      python -m pip install bughawk

Please make sure to also extend the config file with required information.

Development
-----------
When developing a new feature for BugHawk it can be nice to install
the local version in editable mode. This can done using the following command::

      cd bughawk
      python3 -m pip install -e .

To revert this and use the pip package use this command::

      cd bughawk
      python3 -m pip uninstall bughawk
      python -m pip install bughawk
