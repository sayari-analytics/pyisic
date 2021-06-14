******
Pyisic
******
.. image:: https://github.com/sayari-analytics/pyisic/actions/workflows/main.yaml/badge.svg?branch=main

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

TODO: Publish to PyPi

.. code-block:: bash

    pip install pyisic


Documentation
#############

TODO: Publish and link to rtd

Contributing
############
Issues and pull requests are welcome!

Refer to `CONTRIBUTING.rst <https://github.com/sayari-analytics/pyisic/blob/main/CONTRIBUTING.rst>`_ for more details about the workflow and hints on how to prepare your pull request.
