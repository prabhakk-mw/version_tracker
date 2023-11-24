===============
version-tracker
===============


.. image:: https://img.shields.io/pypi/v/version_tracker.svg
        :target: https://pypi.python.org/pypi/version_tracker

.. image:: https://img.shields.io/travis/prabhakk-mw/version_tracker.svg
        :target: https://travis-ci.com/prabhakk-mw/version_tracker

.. image:: https://readthedocs.org/projects/version-tracker/badge/?version=latest
        :target: https://version-tracker.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




Query PyPI for critical updates available available for your users installation of your package.

Details
---------

Import this Python package into your Python packages to query PyPI for critical updates to your package.

This is particularly useful when you would like to notify your users that the version of your package, 
that they have installed has critical updates that they should update their package.

Requirements
-------------
Your package must follow Semantic Versioning.

Given a version number MAJOR.MINOR.PATCH, increment the:

#. MAJOR version when you make incompatible API changes
#. MINOR version when you add functionality in a backward compatible manner
#. PATCH version when you make backward compatible bug fixes

How to use version-tracker
--------------------------
.. code-block:: python

    import version_tracker
    
    # Get the name of your own package
    package_name = str(__name__).split(".")[0]
    
    # Returns a pre-formatted string for use with any logging information, that can be used to warn users of available updates.
    logger.info("HIGH SEVERITY LEVEL log:")
    logger.info(
        version_tracker.get_update_notification(
            package_name, version_tracker.HIGH_SEVERITY_LEVEL
        )
    )

    logger.info("MEDIUM SEVERITY LEVEL log:")
    logger.info(
        version_tracker.get_update_notification(
            package_name, version_tracker.MEDIUM_SEVERITY_LEVEL
        )
    )

    logger.info("LOW SEVERITY LEVEL log:")
    logger.info(
        version_tracker.get_update_notification(
            package_name, version_tracker.LOW_SEVERITY_LEVEL
        )
    
    # Low Level API:

    # Returns version information about the current package.
    version_info = version_tracker.query(package_name)

    # version_info is a Dictionary with the following information:
    #  "latest": latest_version,
    #  "is_major": str(major_update),
    #  "is_minor": str(minor_update),
    #  "is_patch": str(patch_update),
    #  "commit_messages": commit_msg,
    
    # Shows the latest version of your package that is available on PyPI
    print(version_info['latest'])
    
    # Shows whether the updates on PyPI are major in Nature. ie: Update found in the MAJOR portion of the Semantic version.
    print(version_info['is_major'])
    
    # Shows any available commit messages related the updates between installed version and latest version.  
    print(version_info['commit_messages'])

* Free software: MIT license
* Documentation: https://version-tracker.readthedocs.io.



