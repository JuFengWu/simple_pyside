# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.setIDButton = QPushButton(Dialog)
        self.setIDButton.setObjectName(u"setIDButton")
        self.setIDButton.setGeometry(QRect(150, 210, 89, 25))
        self.showIDLabel = QLabel(Dialog)
        self.showIDLabel.setObjectName(u"showIDLabel")
        self.showIDLabel.setGeometry(QRect(110, 90, 81, 17))
        self.IDlabel = QLabel(Dialog)
        self.IDlabel.setObjectName(u"IDlabel")
        self.IDlabel.setGeometry(QRect(210, 90, 31, 17))
        self.IDlineEdit = QLineEdit(Dialog)
        self.IDlineEdit.setObjectName(u"IDlineEdit")
        self.IDlineEdit.setGeometry(QRect(180, 150, 113, 25))
        self.changeIDLabel = QLabel(Dialog)
        self.changeIDLabel.setObjectName(u"changeIDLabel")
        self.changeIDLabel.setGeometry(QRect(80, 150, 81, 17))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.setIDButton.setText(QCoreApplication.translate("Dialog", u"Set ID", None))
        self.showIDLabel.setText(QCoreApplication.translate("Dialog", u"Current ID :", None))
        self.IDlabel.setText(QCoreApplication.translate("Dialog", u"90", None))
        self.changeIDLabel.setText(QCoreApplication.translate("Dialog", u"Change ID :", None))
    # retranslateUi

