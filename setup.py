# -*- coding: utf-8 -*-
import setuptools

with open("README.rst", "r") as infile:
    long_description = infile.read()

setuptools.setup(
    name="pyisic",
    version="0.1.24",
    author="Jordan Vani",
    author_email="tech@sayari.com",
    description="Standard industrial classification standardization",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/sayari-analytics/pyisic",
    project_urls={
        "Documentation": "https://pyisic.readthedocs.io/",
        "Bug Tracker": "https://github.com/sayari-analytics/pyisic/issues",
    },
    packages=setuptools.find_packages(exclude=("tests")),
    install_requires=["networkx>=2.5"],
    extras_require={"dev": ["pytest", "pytest-cov", "black", "pre-commit", "sphinx", "sphinx_rtd_theme"]},
    python_requires=">=3.8",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
)
