import sys
from argparse import ArgumentParser
from pathlib import Path

from qtpy import QtCore, QtWidgets

from .MainWindow import MainWindow


def path_is_file(path: str) -> Path | None:
    """Convert the string to a path only if it is a path to a file. Not using
    `argparse.FileType` because we don't want to actually use the file yet.

    Args:
        path (str): Path string to be checked

    Returns:
        Path | None: Path to file, if it exists
    """
    return Path(path) if Path(path).is_file() else None


def run():
    parser = ArgumentParser()
    parser.add_argument("file", nargs="?", help="The file to open", type=path_is_file)
    args = parser.parse_args()

    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, on=True)
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(file_to_load=args.file)
    sys.exit(app.exec_())


if __name__ == "__main__":
    run()
