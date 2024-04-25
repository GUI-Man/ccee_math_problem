# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 50, 41, 31))
        self.number_of_index = QComboBox(self.centralwidget)
        self.number_of_index.setObjectName(u"number_of_index")
        self.number_of_index.setGeometry(QRect(120, 60, 68, 22))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 80, 61, 21))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(120, 80, 113, 20))
        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(280, 120, 188, 102))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_condition_number1 = QLabel(self.layoutWidget2)
        self.label_condition_number1.setObjectName(u"label_condition_number1")

        self.verticalLayout_3.addWidget(self.label_condition_number1)

        self.label_condition_number2 = QLabel(self.layoutWidget2)
        self.label_condition_number2.setObjectName(u"label_condition_number2")

        self.verticalLayout_3.addWidget(self.label_condition_number2)

        self.label_condition_number3 = QLabel(self.layoutWidget2)
        self.label_condition_number3.setObjectName(u"label_condition_number3")

        self.verticalLayout_3.addWidget(self.label_condition_number3)

        self.label_condition_number4 = QLabel(self.layoutWidget2)
        self.label_condition_number4.setObjectName(u"label_condition_number4")

        self.verticalLayout_3.addWidget(self.label_condition_number4)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.condition_name_1 = QLineEdit(self.layoutWidget2)
        self.condition_name_1.setObjectName(u"condition_name_1")

        self.verticalLayout_4.addWidget(self.condition_name_1)

        self.condition_name_2 = QLineEdit(self.layoutWidget2)
        self.condition_name_2.setObjectName(u"condition_name_2")

        self.verticalLayout_4.addWidget(self.condition_name_2)

        self.condition_name_3 = QLineEdit(self.layoutWidget2)
        self.condition_name_3.setObjectName(u"condition_name_3")

        self.verticalLayout_4.addWidget(self.condition_name_3)

        self.condition_name_4 = QLineEdit(self.layoutWidget2)
        self.condition_name_4.setObjectName(u"condition_name_4")

        self.verticalLayout_4.addWidget(self.condition_name_4)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.Activicate = QPushButton(self.centralwidget)
        self.Activicate.setObjectName(u"Activicate")
        self.Activicate.setGeometry(QRect(240, 260, 75, 24))
        self.result = QTextEdit(self.centralwidget)
        self.result.setObjectName(u"result")
        self.result.setGeometry(QRect(90, 330, 421, 181))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(60, 120, 202, 104))
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.condition1_label = QLabel(self.widget)
        self.condition1_label.setObjectName(u"condition1_label")
        self.condition1_label.setEnabled(True)
        self.condition1_label.setOpenExternalLinks(False)

        self.verticalLayout.addWidget(self.condition1_label)

        self.condition2_label = QLabel(self.widget)
        self.condition2_label.setObjectName(u"condition2_label")

        self.verticalLayout.addWidget(self.condition2_label)

        self.condition3_label = QLabel(self.widget)
        self.condition3_label.setObjectName(u"condition3_label")

        self.verticalLayout.addWidget(self.condition3_label)

        self.condition4_label = QLabel(self.widget)
        self.condition4_label.setObjectName(u"condition4_label")

        self.verticalLayout.addWidget(self.condition4_label)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.condition_line1 = QLineEdit(self.widget)
        self.condition_line1.setObjectName(u"condition_line1")

        self.verticalLayout_2.addWidget(self.condition_line1)

        self.condition_line2 = QLineEdit(self.widget)
        self.condition_line2.setObjectName(u"condition_line2")

        self.verticalLayout_2.addWidget(self.condition_line2)

        self.condition_line3 = QLineEdit(self.widget)
        self.condition_line3.setObjectName(u"condition_line3")

        self.verticalLayout_2.addWidget(self.condition_line3)

        self.condition_line4 = QLineEdit(self.widget)
        self.condition_line4.setObjectName(u"condition_line4")

        self.verticalLayout_2.addWidget(self.condition_line4)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.zero_1 = QLabel(self.widget)
        self.zero_1.setObjectName(u"zero_1")

        self.verticalLayout_5.addWidget(self.zero_1)

        self.zero_2 = QLabel(self.widget)
        self.zero_2.setObjectName(u"zero_2")

        self.verticalLayout_5.addWidget(self.zero_2)

        self.zero_3 = QLabel(self.widget)
        self.zero_3.setObjectName(u"zero_3")

        self.verticalLayout_5.addWidget(self.zero_3)

        self.zero_4 = QLabel(self.widget)
        self.zero_4.setObjectName(u"zero_4")

        self.verticalLayout_5.addWidget(self.zero_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u53d8\u91cf\u6570", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6c42\u89e3\u5f0f", None))
        self.label_condition_number1.setText(QCoreApplication.translate("MainWindow", u"\u53d8\u91cf\u540d1", None))
        self.label_condition_number2.setText(QCoreApplication.translate("MainWindow", u"\u53d8\u91cf\u540d2", None))
        self.label_condition_number3.setText(QCoreApplication.translate("MainWindow", u"\u53d8\u91cf\u540d3", None))
        self.label_condition_number4.setText(QCoreApplication.translate("MainWindow", u"\u53d8\u91cf\u540d4", None))
        self.Activicate.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210\uff01", None))
        self.condition1_label.setText(QCoreApplication.translate("MainWindow", u"\u6761\u4ef61", None))
        self.condition2_label.setText(QCoreApplication.translate("MainWindow", u"\u6761\u4ef62", None))
        self.condition3_label.setText(QCoreApplication.translate("MainWindow", u"\u6761\u4ef63", None))
        self.condition4_label.setText(QCoreApplication.translate("MainWindow", u"\u6761\u4ef64", None))
        self.zero_1.setText(QCoreApplication.translate("MainWindow", u"=0", None))
        self.zero_2.setText(QCoreApplication.translate("MainWindow", u"=0", None))
        self.zero_3.setText(QCoreApplication.translate("MainWindow", u"=0", None))
        self.zero_4.setText(QCoreApplication.translate("MainWindow", u"=0", None))
    # retranslateUi

