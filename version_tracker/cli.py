"""Console script for version_tracker."""
import argparse
import sys

import version_tracker


def main():
    """Console script for version_tracker."""
    parser = argparse.ArgumentParser(
        description="Enter the name of the package you want to track."
    )
    parser.add_argument("-n", "--name", metavar="NAME-OF-PACKAGE-TO-TRACK")
    args = parser.parse_args()

    print("Getting information for the PyPI package [" + str(args.name) + "]")
    print(version_tracker.get_local_version(str(__name__).split(".")[0]))

    print(version_tracker.check_for_updates("matlab-proxy"))

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
