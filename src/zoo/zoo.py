import sys
from importlib import resources
from pathlib import Path

from qtpy import QtCore, QtWidgets

from . import ui
from .MainWindow import MainWindow


def run():
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, on=True)
    app = QtWidgets.QApplication(sys.argv)
    with resources.open_text(ui, "style.qss") as stylefile:
        stylesheet = stylefile.read()
        app.setStyleSheet(stylesheet)
    try:
        file_to_load = Path(sys.argv[1])
        assert file_to_load.is_file()
    except IndexError:
        file_to_load = None
    except:
        print(f"Could not find a file at {sys.argv[1]}")
        file_to_load = None
    finally:
        window = MainWindow(file_to_load=file_to_load)
    sys.exit(app.exec_())


if __name__ == "__main__":
    run()
