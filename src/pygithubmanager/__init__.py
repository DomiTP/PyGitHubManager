# read version from installed package
import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from pygithubmanager.githubmanager import GitHubManager
from importlib.metadata import version
__version__ = version("pygithubmanager")

from pygithubmanager.utils import LOGO


def start():
    """
    Starts the main program.
    """
    app = QApplication([])
    app.setWindowIcon(QIcon(LOGO))
    widget = GitHubManager()
    sys.exit(app.exec())
