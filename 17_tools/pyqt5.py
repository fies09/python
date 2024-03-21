#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/8/29 23:39
# @Author     : fany
# @Project    : PyCharm
# @File       : pyqt5.py
# @description: pyqt5
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem
from PyQt5.QtCore import Qt

class TreeExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.tree = QTreeWidget(self)
        self.tree.setHeaderLabel('Items')

        item = QTreeWidgetItem(self.tree, ['Item 1'])
        child_item1 = QTreeWidgetItem(item, ['Child 1'])
        child_item2 = QTreeWidgetItem(item, ['Child 2'])
        child_item3 = QTreeWidgetItem(item, ['Child 3'])

        item.setFlags(item.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
        for i in range(item.columnCount()):
            item.setCheckState(i, Qt.Unchecked)

        self.tree.expandAll()

        self.tree.itemClicked.connect(self.handleItemClicked)

        self.setCentralWidget(self.tree)
        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('Tree with Checkboxes')
        self.show()

    def handleItemClicked(self, item, column):
        state = item.checkState(column)
        if state == Qt.Checked:
            self.checkChildren(item, column)
            self.checkParent(item, column)
        elif state == Qt.Unchecked:
            self.uncheckChildren(item, column)
            self.checkParent(item, column)

    def checkChildren(self, item, column):
        for i in range(item.childCount()):
            child = item.child(i)
            child.setCheckState(column, Qt.Checked)
            self.checkChildren(child, column)

    def uncheckChildren(self, item, column):
        for i in range(item.childCount()):
            child = item.child(i)
            child.setCheckState(column, Qt.Unchecked)
            self.uncheckChildren(child, column)

    def checkParent(self, item, column):
        parent = item.parent()
        if parent:
            checked_count = 0
            unchecked_count = 0
            for i in range(parent.childCount()):
                child = parent.child(i)
                if child.checkState(column) == Qt.Checked:
                    checked_count += 1
                elif child.checkState(column) == Qt.Unchecked:
                    unchecked_count += 1

            if checked_count == parent.childCount():
                parent.setCheckState(column, Qt.Checked)
            elif unchecked_count == parent.childCount():
                parent.setCheckState(column, Qt.Unchecked)
            else:
                parent.setCheckState(column, Qt.PartiallyChecked)
            self.checkParent(parent, column)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TreeExample()
    sys.exit(app.exec_())
