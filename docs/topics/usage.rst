*****
Usage
*****

Lookup
======
Standards are implemented as a ``collection.OrderedDict`` to enable classification lookups:

.. code-block::

    >>> import pyisic
    >>> pyisic.ISIC4["0113"]
    {'code': '0115',
     'description': 'Growing of tobacco',
     'category': <Category.CLASS: 4>}

Concordance
===========
Concordances are implemented as ``networkx.DiGraph``. Concordant nodes discovered as DAG descendants.

.. code-block::

    >>> import pyisic
    >>> pyisic.NAICS2017_to_ISIC4.concordant("927110")
    {(<Standard.ISIC4: 'ISIC4'>, '5120'), (<Standard.ISIC4: 'ISIC4'>, '8413')}

Composed Graphs
+++++++++++++++

.. code-block::

    >>> import pyisic
    >>> yisic.ToISIC4("84114", pyisic.Standards.TSIC2552)
    {(<Standards.ISIC4: 'ISIC4'>, '6810'),
     (<Standards.ISIC4: 'ISIC4'>, '6820'),
     (<Standards.ISIC4: 'ISIC4'>, '8411'),
     (<Standards.ISIC4: 'ISIC4'>, '9101')}
