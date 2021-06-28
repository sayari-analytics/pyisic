************
Contributing
************

Issues and pull requests are welcome! If a question, defect, or improvement is identified, please create an issue in the `issue tracker <https://github.com/sayari-analytics/pyisic/issues>`_ with relevant tags. To address any raised issue, please create a branch, commit changes, and submit a PR. The goal of the following notes is to outline general standards and processes for contributing.

Workflow
========
The steps below describe how to get a patch into a main development branch. The steps are exactly the same for everyone involved in the project.

#. Create a feature-branch for your work, from which you'll be able to submit a pull request.
#. Once your feature is complete, prepare the commit following `Conventional Commits <https://www.conventionalcommits.org/en/v1.0.0/>`_.
#. If it's a new feature, or a change of behavior, test and document it.
#. Submit a pull request and request a review.
#. After the review you should fix the issues as needed, iterating until the reviewers give their thumbs up.
#. Squash and merge!

Pull requests
=============
A pull request should meet the following requirements before squashing and merging:

#. If the code introduces new features or fixes bugs or regressions, it must have comprehensive tests.
#. The code must be well documented.
#. The commit messages must properly describe the changes.
#. A pull request must indicate (link to) the issue it is aimed to resolve in the description (or comments) of the PR, in order to establish a link between PR and Issue. This can be achieved by writing "Fixes #1234" or similar in PR description.

Setup
=====
To begin developing, testing, and/or documenting, we recommend installing the ``dev`` dependencies in a virtual environment:

.. code-block::

    python -m venv venv
    source venv/bin/activate
    pip install pyisic[dev]
    pre-commit install

Testing
+++++++

Pyisic uses `pytest <https://docs.pytest.org/en/latest/>`_ as a testing framework. New functionality must be fully tested. New standards and/or concordances should extend existing tests.

Documenting
+++++++++++

Pyisic uses `Sphinx <https://www.sphinx-doc.org/en/master/>`_ for documentation. New functionallity must be fully documented. Docstrings must follow the `Google Python Style Guide <https://google.github.io/styleguide/pyguide.html>`_. For additional reference, see examples provided by `napolean <https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html>`_.
