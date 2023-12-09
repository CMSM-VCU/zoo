import os
import sys
from argparse import ArgumentParser
from pathlib import Path

os.environ["QT_API"] = "pyside6"

from loguru import logger
from PySide6 import QtCore, QtWidgets

from . import config
from .gui.MainWindow import MainWindow


def path_is_file(path: str) -> Path | None:
    """Convert the string to a path only if it is a path to a file. Not using
    `argparse.FileType` because we don't want to actually use the file yet.

    Args:
        path (str): Path string to be checked

    Returns:
        Path | None: Path to file, if it exists
    """
    return Path(path) if Path(path).is_file() else None


def positive_or_none(num: str) -> int | None:
    return int(num) if int(num) >= 0 else None


def run():
    parser = ArgumentParser()
    parser.add_argument("file", nargs="?", help="The file to open", type=path_is_file)
    parser.add_argument(
        "--cache-size",
        action="store",
        help="Number of timesteps to cache in memory, for each file. -1 for unlimited, 0 to disable",
        type=positive_or_none,  # Actual "unlimited" value is None. Convert negatives to that
        default=config.cache_size,
    )
    parser.add_argument(
        "-v", "--verbose", help="increase output verbosity", action="count", default=0
    )

    args = parser.parse_args()

    config.cache_size = args.cache_size
    if args.verbose > 1:
        logger.remove()
        logger.add(sys.stderr, level="TRACE")
    elif args.verbose > 0:
        logger.remove()
        logger.add(sys.stderr, level="DEBUG")
    else:
        logger.remove()
        logger.add(sys.stderr, level="INFO")

    logger.debug(f"Command line arguments: {args}")

    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, on=True)
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(file_to_load=args.file)
    sys.exit(app.exec_())


if __name__ == "__main__":
    run()
