from pathlib import Path

EXTENSIONS = {"h5": (".h5", ".hdf5"), "grid": (".csv", ".grid")}


def has_known_extension(file: Path) -> bool:
    return file.suffix in [ext for group in EXTENSIONS.values() for ext in group]
