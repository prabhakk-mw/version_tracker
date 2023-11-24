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

APIs
-----

#. High Level API

    .. code-block:: python

        def get_update_notification(pkg_name: str, severity_level: int = 2) -> str:

#. Low Level API

    .. code-block:: python

        def query(pkg_name: str) -> dict[str, str]:


How to use version-tracker
--------------------------

#. Add version-tracker to the list of your package's dependencies.

    .. code-block:: python

        # Update your SETUP.PY to include version-tracker as shown:
        INSTALL_REQUIRES = [
                "aiohttp>=3.7.4",
                "psutil",
                "aiohttp_session[secure]",
                "version-tracker",
                ]

#. Include the module from your source code and use the APIs provided. See example below:

    .. code-block:: python
    
        import version_tracker
        
            logger.info("==============")
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
            print(version_info["latest"])

            # Shows whether the updates on PyPI are major in Nature. ie: Update found in the MAJOR portion of the Semantic version.
            print(version_info["is_major"])

            # Shows any available commit messages related the updates between installed version and latest version.
            print(version_info["commit_messages"])
            logger.info("==============")

#. Sample output from a package that is using the Above APIs and run on an installation which has version 0.1.0, but PyPI has version 0.10.0 installed

    .. code-block:: bash
    
                INFO:MATLABProxyApp:HIGH SEVERITY LEVEL log:
                severity_level requested: 2
                Local version found for [matlab_proxy] is: [0.1.0]
                fetching: https://api.github.com/repos/mathworks/matlab-proxy/releases/tags/v0.10.0
                INFO:MATLABProxyApp:
                ====!!!! ATTENTION !!!!====
                Major Update required for matlab_proxy.
                Consider updating to v0.10.0.
                Commit message of v0.10.0: 
                        Contains multiple bug fixes and critical vulnerability patches.
                Also introduces the ability to control the time for which matlab-proxy waits before timing out. See MWI_PROCESS_START_TIMEOUT in [Advanced-Usage.md](https://github.com/mathworks/matlab-proxy/blob/main/Advanced-Usage.md).
                **Full Changelog**: https://github.com/mathworks/matlab-proxy/compare/v0.9.1...v0.10.0
                ====!!!! ATTENTION !!!!====

                INFO:MATLABProxyApp:MEDIUM SEVERITY LEVEL log:
                severity_level requested: 1
                Local version found for [matlab_proxy] is: [0.1.0]
                fetching: https://api.github.com/repos/mathworks/matlab-proxy/releases/tags/v0.10.0
                INFO:MATLABProxyApp:
                ====!!!! ATTENTION !!!!====
                Major Update required for matlab_proxy.
                Consider updating to v0.10.0.
                Commit message of v0.10.0: 
                        Contains multiple bug fixes and critical vulnerability patches.
                Also introduces the ability to control the time for which matlab-proxy waits before timing out. See MWI_PROCESS_START_TIMEOUT in [Advanced-Usage.md](https://github.com/mathworks/matlab-proxy/blob/main/Advanced-Usage.md).
                **Full Changelog**: https://github.com/mathworks/matlab-proxy/compare/v0.9.1...v0.10.0
                ====!!!! ATTENTION !!!!====

                INFO:MATLABProxyApp:LOW SEVERITY LEVEL log:
                severity_level requested: 0
                Local version found for [matlab_proxy] is: [0.1.0]
                fetching: https://api.github.com/repos/mathworks/matlab-proxy/releases/tags/v0.10.0
                INFO:MATLABProxyApp:
                ====!!!! ATTENTION !!!!====
                Major Update required for matlab_proxy.
                Consider updating to v0.10.0.
                Commit message of v0.10.0: 
                        Contains multiple bug fixes and critical vulnerability patches.
                Also introduces the ability to control the time for which matlab-proxy waits before timing out. See MWI_PROCESS_START_TIMEOUT in [Advanced-Usage.md](https://github.com/mathworks/matlab-proxy/blob/main/Advanced-Usage.md).
                **Full Changelog**: https://github.com/mathworks/matlab-proxy/compare/v0.9.1...v0.10.0
                ====!!!! ATTENTION !!!!====

                Local version found for [matlab_proxy] is: [0.1.0]
                fetching: https://api.github.com/repos/mathworks/matlab-proxy/releases/tags/v0.10.0
                0.10.0
                False
                Contains multiple bug fixes and critical vulnerability patches.
                Also introduces the ability to control the time for which matlab-proxy waits before timing out. See MWI_PROCESS_START_TIMEOUT in [Advanced-Usage.md](https://github.com/mathworks/matlab-proxy/blob/main/Advanced-Usage.md).
                **Full Changelog**: https://github.com/mathworks/matlab-proxy/compare/v0.9.1...v0.10.0
                INFO:MATLABProxyApp:==============

* Free software: MIT license
* Documentation: https://version-tracker.readthedocs.io.



