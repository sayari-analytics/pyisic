******
Pyisic
******
.. image:: https://github.com/sayari-analytics/pyisic/actions/workflows/main.yaml/badge.svg?branch=main

.. image:: https://img.shields.io/codecov/c/github/sayari-analytics/pyisic/master.svg
   :target: https://codecov.io/github/sayari-analytics/pyisic?branch=master
   :alt: Coverage report

.. image:: https://img.shields.io/pypi/v/pyisic.svg
   :target: https://pypi.python.org/pypi/pyisic
   :alt: PyPI Version

.. image:: https://img.shields.io/pypi/pyversions/pyisic.svg
   :target: https://pypi.python.org/pypi/pyisic
   :alt: Supported Python Versions

.. image:: https://img.shields.io/pypi/l/pyisic.svg
   :target: https://github.com/sayari-analytics/pyisic/blob/main/LICENSE
   :alt: License

Overview
########
Pyisic defines industrial classification standards and concordances between standards.

.. pull-quote::
    The `International Standard Industrial Classification of All Economic Activities (ISIC) <https://unstats.un.org/unsd/classifications/Econ/ISIC.cshtml>`_ is the international reference classification of productive activities. Its main purpose is to provide a set of activity categories that can be utilized for the collection and reporting of statistics according to such activities. Since the adoption of the original version of ISIC in 1948, the majority of countries around the world have used ISIC as their national activity classification or have developed national classifications derived from ISIC.

Usage
+++++

.. code-block:: python

    >>> import pyisic
    >>> pyisic.NAICS2017['927110']
    {'code': '927110', 'description': 'Space Research and Technology', 'category': None}

    >>> pyisic.NAICS2017_to_ISIC4.concordant("927110")
    {(<Standard.ISIC4: 'ISIC4'>, '5120'), (<Standard.ISIC4: 'ISIC4'>, '8413')}

Install
#######

.. code-block:: bash

    pip install pyisic


Documentation
#############

The official documentation is hosted on readthedocs.org: `pyisic.readthedocs.io <https://pyisic.readthedocs.io>`_

Contributing
############
Issues and pull requests are welcome!

Refer to `CONTRIBUTING.rst <https://github.com/sayari-analytics/pyisic/blob/main/CONTRIBUTING.rst>`_ for more details about the workflow and hints on how to prepare your pull request.
