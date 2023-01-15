import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

from screens.home_screen import HomeScreen


class App(object):
    widgets = [
        HomeScreen,
    ]

    def initialize(self):
        app = QApplication(sys.argv)
        widget = QtWidgets.QStackedWidget()
        widget.setFixedHeight(900)
        widget.setFixedWidth(1500)
        self.fill_widgets(widget)
        widget.show()
        try:
            sys.exit(app.exec_())
        except Exception as e:
            print("Exiting")

    def fill_widgets(self, stacked_widget):
        for widget in self.widgets:
            stacked_widget.addWidget(widget(stacked_widget))
        stacked_widget.setCurrentWidget(stacked_widget.findChild(self.widgets[0]))

