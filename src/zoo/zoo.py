import sys
from pathlib import Path

from qtpy import QtWidgets

from MainWindow import MainWindow


def main():
    app = QtWidgets.QApplication(sys.argv)
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
    main()
