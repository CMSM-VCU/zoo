from pathlib import Path

from matplotlib.pyplot import colormaps
from colorcet import all_original_names

EXTENSIONS = {"h5": (".h5", ".hdf5"), "grid": (".csv", ".grid")}

COLORMAPS = colormaps() + all_original_names()


def has_known_extension(file: Path) -> bool:
    return file.suffix in [ext for group in EXTENSIONS.values() for ext in group]
