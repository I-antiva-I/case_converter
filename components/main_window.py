import os
from typing import Dict

from PyQt5.QtGui import QFontDatabase, QIcon
from PyQt5.QtWidgets import QMainWindow, QPushButton, QTabWidget, QFrame, QVBoxLayout

from models.conversion_model import ConversionModel
from models.information_model import InformationModel
from models.shared_data_model import SharedDataModel
from views.conversion_view import ConversionView
from views.information_view import InformationView
from viewmodels.conversion_viewmodel import ConversionViewModel
from viewmodels.information_viewmodel import InformationViewModel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Path constants
        self.PATH_TO_STYLES = "assets/css/styles.css"
        self.PATH_TO_FONTS = "assets/fonts/titillium_web"
        
        # Models
        conversion_m = ConversionModel()
        information_m = InformationModel()
        shared = SharedDataModel()

        # Viewmodels
        conversion_vm = ConversionViewModel(conversion_m, shared)
        information_vm = InformationViewModel(information_m, shared)

        # Views
        conversion_v = ConversionView(conversion_vm)
        information_v = InformationView(information_vm)

        tabs = QTabWidget()
        tabs.addTab(conversion_v, "Conversion")
        tabs.addTab(information_v, "Information")
        tabs.setCurrentIndex(0)

        # Central Widget
        central_frame = QFrame()
        central_frame.setLayout(QVBoxLayout())
        central_frame.layout().addWidget(tabs)
        self.setCentralWidget(central_frame)

        # Window
        self.resize(640, 480)
        self.setMaximumWidth(int(640*1.5))
        self.setWindowTitle("Case Converter")
        self.setWindowIcon(QIcon("assets/images/logo.svg"))

        # External Margins, Spacing and Size Policies
        central_frame.layout().setContentsMargins(0, 0, 0, 0)
        central_frame.layout().setSpacing(0)

        # Style Settings
        self.setObjectName("main-window")
        tabs.setObjectName("tabs")

        # Fonts and Styles
        self.load_fonts()
        self.set_styles()


        # DEBUG
        """
        refresh_stylesheets = QPushButton("CSS")
        refresh_stylesheets.clicked.connect(self.set_styles)
        central_frame.layout().addWidget(refresh_stylesheets)
        """
        
    def set_styles(self):
        styles = open(self.PATH_TO_STYLES, "r").read()
        self.setStyleSheet(styles)

    def load_fonts(self):
        for font_file in os.listdir(self.PATH_TO_FONTS):
            QFontDatabase.addApplicationFont(self.PATH_TO_FONTS+"/"+font_file)
