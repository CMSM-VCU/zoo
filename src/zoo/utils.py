from pathlib import Path

from colorcet import all_original_names, get_aliases
from matplotlib.pyplot import colormaps

# fmt: off
EXTENSIONS_GOOD = {
    "h5": (".h5", ".hdf5"),
    "grid": (".csv", ".grid"),
}
EXTENSIONS_BAD = {
    "known_bad": (
            ".in", ".his", ".0",
            ".png", ".gif", ".jpg",
            ".exe", ".py",
            ".zip", ".tar", ".gz", ".7z",
            ".docx", ".xlsx", ".pptx",
    ),
}
EXTENSIONS = EXTENSIONS_GOOD | EXTENSIONS_BAD
# fmt: on

# Filtering colorcet colormaps
# We want only the colormaps that have a given name and are not categorical/qualitative
# colorcet.holoviz.org/user_guide/Continuous.html#named-colormaps
colorcet_colormaps = [
    get_aliases(name).split(", ")[0]
    for name in all_original_names(only_aliased=True, not_group="glasbey")
]

# Filtering matplotlib colormaps
# matplotlib includes CET colormaps, named `cet_*` and `cet_CET_*`
# These names give no description and should also be avoided
# All or most of the colormaps have a corresponding reversed version named `*_r`
# These are redundant and should also be avoided
matplotlib_colormaps = [
    name for name in colormaps() if "cet_" not in name and not name.endswith("_r")
]

COLORMAPS = (
    sorted(colorcet_colormaps) + sorted(matplotlib_colormaps) + ["rainbow (legacy)"]
)


def has_known_extension(file: Path, exclude_known_bad: bool = True) -> bool:
    check = EXTENSIONS_GOOD if exclude_known_bad else EXTENSIONS
    return file.suffix in [ext for group in check.values() for ext in group]


def truncate_int8_to_int4(val: int) -> int:
    return int.from_bytes(val.to_bytes(8, "big")[4:], "big", signed=True)
