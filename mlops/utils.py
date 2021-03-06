import json


def save_dict(d: dict, filepath: str) -> None:
    """
    Save dictionary as a json file.

    Convert dictionary to a json file and save in ``filepath``.

    Parameters:
        d (dict):
            Dictionary.
        filepath (str):
            Path to save the json file.
    """
    with open(filepath, "w") as fp:
        json.dump(d, fp=fp, indent=2)


def load_dict(filepath: str) -> dict:
    """
    Load json file as dictionary.

    Open a json file and convert to a dictionary.

    Parameters:
        filepath (str):
            Path to load the json file.

    Returns:
        Dictionary.
    """
    with open(filepath, "r") as fp:
        d = json.load(fp)
    return d
