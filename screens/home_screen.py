import numpy as np
from PyQt5.QtWidgets import QDialog, QTreeWidget, QTreeWidgetItem, QPushButton
from PyQt5.uic import loadUi
import pandas as pd

from screens.utils import generate_tree


def fill_item(item, value):
    if not value:
        return
    item.setExpanded(True)
    for key, val in value.items():
        child = QTreeWidgetItem()
        child.setText(0, key)
        child.setText(1, val['description'])
        item.addChild(child)
        fill_item(child, val['children'])
    item.setExpanded(False)


class HomeScreen(QDialog):
    NAME = 'home'

    def __init__(self, stacked_widget):
        super(HomeScreen, self).__init__()
        loadUi('screens_ui/home.ui', self)
        self.stacked_widget = stacked_widget

        self.tree_widget = self.findChild(QTreeWidget, 'tree_widget')
        self.generate_report_button = self.findChild(QPushButton, 'generate_report_button')
        self.generate_report_button.clicked.connect(self.generate_report)

        self.tree_dict, self.data_dict, self.df = generate_tree('D:/Pre.xlsx', 'D:/Schedule Data.xlsx')
        self.fill_widget()
        self.tree_widget.resizeColumnToContents(0)

    def fill_widget(self):
        self.tree_widget.clear()
        fill_item(self.tree_widget.invisibleRootItem(), self.tree_dict)
        self.tree_widget.setHeaderLabels(['Activity ID', 'Description'])

    def generate_report(self):
        getSelected = self.tree_widget.selectedItems()
        print("HERE")
        if getSelected:
            baseNode = getSelected[0]
            getChildNode = baseNode.text(0)
            column_number = self.data_dict.get(getChildNode)
            df1 = self.df.iloc[:, column_number]
            df1 = df1.tail(-3)
            df = pd.DataFrame([[np.nan]] * 4, columns=[''])
            df_merged = pd.concat([df, df1], ignore_index=True, sort=False)
            del df_merged[df_merged.columns[0]]
            df_merged.to_excel('D:/new_report.xlsx', index=False, header=False)
