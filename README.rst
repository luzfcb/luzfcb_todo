========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |requires|
        | |codecov|
        | |landscape|

.. |docs| image:: https://readthedocs.org/projects/luzfcb_todo/badge/?style=flat
    :target: https://readthedocs.org/projects/luzfcb_todo
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/luzfcb/luzfcb_todo.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/luzfcb/luzfcb_todo

.. |requires| image:: https://requires.io/github/luzfcb/luzfcb_todo/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/luzfcb/luzfcb_todo/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/luzfcb/luzfcb_todo/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/luzfcb/luzfcb_todo

.. |landscape| image:: https://landscape.io/github/luzfcb/luzfcb_todo/master/landscape.svg?style=flat
    :target: https://landscape.io/github/luzfcb/luzfcb_todo/master
    :alt: Code Quality Status



.. end-badges

A very, very simple Todo app

* Free software: BSD license

Installation
============

::




Documentation
=============



Development
===========

To run the all tests run::

    export DJANGO_SETTINGS_MODULE=config.settings

    pip install -r requirements.txt

    coverage run manage.py test
    coverage report -m

