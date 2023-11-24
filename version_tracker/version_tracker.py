"""Main module."""
import requests

# Take a package and query pypi to find if there is a more recent version available
# Also print the commit message/s with the more recent release from GH

severity_level_str = ["Patch", "Minor", "Major"]

LOW_SEVERITY_LEVEL = 0
MEDIUM_SEVERITY_LEVEL = 1
HIGH_SEVERITY_LEVEL = 2

severity_level_str_to_int = {
    "Patch": 0,
    "Minor": 1,
    "Major": 2,
}


def get_update_notification(pkg_name: str, severity_level: int = 2) -> str:
    """
    pkg_name : Name of your package
    level    : Int (0 = Patch, 1 = Minor, 2 = Major) updates or more
    """
    print(f"severity_level requested: {severity_level}")
    info = query(pkg_name=pkg_name)

    update_message = None
    # Find the most severe vulnerability
    if info["is_patch"]:
        update_message = severity_level_str[0]
    if info["is_minor"]:
        update_message = severity_level_str[1]
    if info["is_major"]:
        update_message = severity_level_str[2]

    highest_severity_found = severity_level_str_to_int[update_message]
    if highest_severity_found < severity_level:
        return ""

    header = "\n====!!!! ATTENTION !!!!====\n"
    message = (
        header
        + f" {update_message} Update required for {pkg_name}.\n Consider updating to v{info['latest']}."
        + header
    )

    return message


def query(pkg_name: str) -> dict[str, str]:
    pypi_url = f"https://pypi.org/pypi/{pkg_name}/json"

    try:
        response = requests.get(pypi_url)
        response.raise_for_status()  # Raise an exception for bad responses (4xx or 5xx)
        data = response.json()

        # Extract the version information
        versions = data["releases"].keys()
        local_version = get_local_version(pkg_name)
        latest_version_list = list(
            sorted(versions, key=lambda x: tuple(map(int, x.split("."))))
        )[-1:]
        latest_version = str(latest_version_list[0])
        commit_msg = get_commit_message("matlab-proxy", latest_version)

        major_update: bool = is_major_update_available(local_version, latest_version)
        minor_update: bool = is_minor_update_available(local_version, latest_version)
        patch_update: bool = is_patch_update_available(local_version, latest_version)

        return {
            "latest": latest_version,
            "is_major": str(major_update),
            "is_minor": str(minor_update),
            "is_patch": str(patch_update),
            "commit_messages": commit_msg,
        }

        # return f"Current version: {local_version}, Latest version: {latest_version}, Is update critical: {critical_update},\nCommit message: {commit_msg}"

    except Exception as e:
        print(f"Got error: {e}")
        return None


def get_local_version(pkg_name: str) -> str:
    import importlib.metadata

    local_version = importlib.metadata.version(pkg_name)
    print(f"Local version found for [{pkg_name}] is: [{local_version}]")
    return local_version


def is_major_update_available(local_version: str, latest_version: str):
    """Checks if the y version is lower than the latest available release, flags it as critical."""

    # compare the minor version between the local version and latest version
    local_major_ver = get_major_version(local_version)
    latest_major_ver = get_major_version(latest_version)

    if int(local_major_ver) < int(latest_major_ver):
        return True
    else:
        return False


def is_minor_update_available(local_version: str, latest_version: str):
    """Checks if the y version is lower than the latest available release, flags it as critical."""

    # compare the minor version between the local version and latest version
    local_minor_ver = get_minor_version(local_version)
    latest_minor_ver = get_minor_version(latest_version)

    if int(local_minor_ver) < int(latest_minor_ver):
        return True
    else:
        return False


def is_patch_update_available(local_version: str, latest_version: str):
    """Checks if the y version is lower than the latest available release, flags it as critical."""

    # compare the minor version between the local version and latest version
    local_minor_ver = get_minor_version(local_version)
    latest_minor_ver = get_minor_version(latest_version)

    if int(local_minor_ver) < int(latest_minor_ver):
        return True
    else:
        return False


def get_major_version(version: str):
    version_list = version.split(".")
    return version_list[0]


def get_minor_version(version: str):
    version_list = version.split(".")
    return version_list[1]


def get_patch_version(version: str):
    version_list = version.split(".")
    return version_list[2]


def get_commit_message(repo_name, release_tag):
    api_url = f"https://api.github.com/repos/mathworks/{repo_name}/releases/tags/v{release_tag}"
    headers = {"Authorization": "token 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"}
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        data = response.json()
        if "body" in data:
            return data["body"]
        else:
            return "No commit messages found for this release."
    except Exception as e:
        print(f"Error while communicating with GH: {e}")
        return "No commit messages found for this release."
