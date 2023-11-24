#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = ["requests"]

test_requirements = []

setup(
    author="Prabhakar Kumar",
    author_email="prabhakk@mathworks.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Query PyPI for critical updates available available for your users installation of your package.",
    entry_points={
        "console_scripts": [
            "version_tracker=version_tracker.cli:main",
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="version_tracker",
    name="version_tracker",
    packages=find_packages(include=["version_tracker", "version_tracker.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/prabhakk-mw/version_tracker",
    version="0.1.1",
    zip_safe=False,
)
