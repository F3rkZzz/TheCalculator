# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TheCalculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TheCalculator(object):
    def setupUi(self, TheCalculator):
        TheCalculator.setObjectName("TheCalculator")
        TheCalculator.setWindowModality(QtCore.Qt.ApplicationModal)
        TheCalculator.resize(340, 495)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TheCalculator.sizePolicy().hasHeightForWidth())
        TheCalculator.setSizePolicy(sizePolicy)
        TheCalculator.setMinimumSize(QtCore.QSize(340, 495))
        TheCalculator.setBaseSize(QtCore.QSize(340, 495))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        TheCalculator.setFont(font)
        TheCalculator.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        TheCalculator.setMouseTracking(False)
        TheCalculator.setTabletTracking(False)
        TheCalculator.setFocusPolicy(QtCore.Qt.NoFocus)
        TheCalculator.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/TCLogo1.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TheCalculator.setWindowIcon(icon)
        TheCalculator.setStyleSheet("background-color: rgb(223, 223, 223);\n"
"")
        TheCalculator.setTabShape(QtWidgets.QTabWidget.Rounded)
        TheCalculator.setDockNestingEnabled(True)
        self.centralwidget = QtWidgets.QWidget(TheCalculator)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.pushB_DEL = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.pushB_DEL.sizePolicy().hasHeightForWidth())
        self.pushB_DEL.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushB_DEL.setFont(font)
        self.pushB_DEL.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushB_DEL.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushB_DEL.setStyleSheet("QPushButton{\n"
"font: 25pt \"SimSun-ExtB\";\n"
"background-color: #f1d753;\n"
"color:#FFFFFF;\n"
"border-style:outset;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#f2dd8e;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:#e6ba66;\n"
"}")
        self.pushB_DEL.setObjectName("pushB_DEL")
        self.gridLayout.addWidget(self.pushB_DEL, 1, 3, 1, 1)
        self.pushB_Cbracket = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.pushB_Cbracket.sizePolicy().hasHeightForWidth())
        self.pushB_Cbracket.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.pushB_Cbracket.setFont(font)
        self.pushB_Cbracket.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushB_Cbracket.setStyleSheet("QPushButton{\n"
"font: 25pt \"SimSun-ExtB\";\n"
"background-color: rgb(239, 239, 239);\n"
"border-style:outset;\n"
"border-radius:8px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#f4f4f4;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:#c3c3c3;\n"
"}")
        self.pushB_Cbracket.setObjectName("pushB_Cbracket")
        self.gridLayout.addWidget(self.pushB_Cbracket, 1, 1, 1, 1)
        self.pushB_clear = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.pushB_clear.sizePolicy().hasHeightForWidth())
        self.pushB_clear.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(241, 215, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(241, 215, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(241, 215, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(241, 215, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(241, 215, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(241, 215, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(241, 215, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(241, 215, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(241, 215, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushB_clear.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.pushB_clear.setFont(font)
        self.pushB_clear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushB_clear.setStyleSheet("QPushButton{\n"
"font: 25pt \"SimSun-ExtB\";\n"
"background-color: #f1d753;\n"
"color:#FFFFFF;\n"
"border-style:outset;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#f2dd8e;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:#e6ba66;\n"
"}")
        self.pushB_clear.setObjectName("pushB_clear")
        self.gridLayout.addWidget(self.pushB_clear, 1, 2, 1, 1)
        self.pushB_multi = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.pushB_multi.sizePolicy().hasHeightForWidth())
        self.pushB_multi.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.pushB_multi.setFont(font)
        self.pushB_multi.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushB_multi.setStyleSheet("QPushButton{\n"
"font: 25pt \"SimSun-ExtB\";\n"
"background-color: rgb(239, 239, 239);\n"
"border-style:outset;\n"
"border-radius:8px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#f4f4f4;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:#c3c3c3;\n"
"}")
        self.pushB_multi.setObjectName("pushB_multi")
        self.gridLayout.addWidget(self.pushB_multi, 3, 3, 1, 1)
        self.pushB_minus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.pushB_minus.sizePolicy().hasHeightForWidth())
        self.pushB_minus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.pushB_minus.setFont(font)
        self.pushB_minus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushB_minus.setStyleSheet("QPushButton{\n"
"font: 25pt \"SimSun-ExtB\";\n"
"background-color: rgb(239, 239, 239);\n"
"border-style:outset;\n"
"border-radius:8px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#f4f4f4;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:#c3c3c3;\n"
"}")
        self.pushB_minus.setShortcut("")
        self.pushB_minus.setObjectName("pushB_minus")
        self.gridLayout.addWidget(self.pushB_minus, 4, 3, 1, 1)
        self.pushB_plus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.pushB_plus.sizePolicy().hasHeightForWidth())
        self.pushB_plus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushB_plus.setFont(font)
        self.pushB_plus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushB_plus.setStyleSheet("QPushButton{\n"
"font: 25pt \"SimSun-ExtB\";\n"
"background-color: rgb(239, 239, 239);\n"
"border-style:outset;\n"
"border-radius:8px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#f4f4f4;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:#c3c3c3;\n"
"}")
        self.pushB_plus.setObjectName("pushB_plus")
        self.gridLayout.addWidget(self.pushB_plus, 5, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setMouseTracking(True)
        self.label.setStyleSheet("font: 25pt \"SimSun-ExtB\";\n"
"background-color:#fbfbfb;\n"
"border-radius:8px;")
        self.label.setText("")
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)
        self.pushB_div = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.pushB_div.sizePolicy().hasHeightForWidth())
        self.pushB_div.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.pushB_div.setFont(font)
        self.pushB_div.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushB_div.setStyleSheet("QPushButton{\n"
"font: 25pt \"SimSun-ExtB\";\n"
"background-color: rgb(239, 239, 239);\n"
"border-style:outset;\n"
"border-radius:8px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#f4f4f4;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:#c3c3c3;\n"
"}")
        self.pushB_div.setObjectName("pushB_div")
        self.gridLayout.addWidget(self.pushB_div, 2, 3, 1, 1)
        self.pushB_Obracket = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.pushB_Obracket.sizePolicy().hasHeightForWidth())
        self.pushB_Obracket.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.pushB_Obracket.setFont(font)
        self.pushB_Obracket.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushB_Obracket.setTabletTracking(False)
        self.pushB_Obracket.setAcceptDrops(False)
        self.pushB_Obracket.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushB_Obracket.setAutoFillBackground(False)
        self.pushB_Obracket.setStyleSheet("QPushButton{\n"
"font: 25pt \"SimSun-ExtB\";\n"
"background-color: rgb(239, 239, 239);\n"
"border-style:outset;\n"
"border-radius:8px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#f4f4f4;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:#c3c3c3;\n"
"}")
        self.pushB_Obracket.setObjectName("pushB_Obracket")
        self.gridLayout.addWidget(self.pushB_Obracket, 1, 0, 1, 1)
        self.pushB_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.pushB_9.sizePolicy().hasHeightForWidth())
        self.pushB_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.pushB_9.setFont(font)
        self.pushB_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushB_9.setStyleSheet("QPushButton{\n"
"font: 25pt \"SimSun-ExtB\";\n"
"background-color:#fbfbfb;\n"
"border-style:outset;\n"
"border-radius:8px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#FFFFFF;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:#c3c3c3;\n"
"}")
        self.pushB_9.setObjectName("pushB_9")
        self.gridLayout.addWidget(self.pushB_9, 2, 2, 1, 1)
        self.pushB_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.pushB_8.sizePolicy().hasHeightForWidth())
        self.pushB_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.pushB_8.setFont(font)
        self.pushB_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushB_8.setStyleSheet("QPushButton{\n"
"font: 25pt \"SimSun-ExtB\";\n"
"background-color:#fbfbfb;\n"
"border-style:outset;\n"
"border-radius:8px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#FFFFFF;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:#c3c3c3;\n"
"}")
        self.pushB_8.setObjectName("pushB_8")
        self.gridLayout.addWidget(self.pushB_8, 2, 1, 1, 1)
        self.pushB_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.pushB_7.sizePolicy().hasHeightForWidth())
        self.pushB_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.pushB_7.setFont(font)
        self.pushB_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushB_7.setStyleSheet("QPushButton{\n"
"font: 25pt \"SimSun-ExtB\";\n"
"background-color:#fbfbfb;\n"
"border-style:outset;\n"
"border-radius:8px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#FFFFFF;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:#c3c3c3;\n"
"}")
        self.pushB_7.setObjectName("pushB_7")
        self.gridLayout.addWidget(self.pushB_7, 2, 0, 1, 1)
        self.pushB_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.pushB_5.sizePolicy().hasHeightForWidth())
        self.pushB_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.pushB_5.setFont(font)
        self.pushB_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushB_5.setStyleSheet("QPushButton{\n"
"font: 25pt \"SimSun-ExtB\";\n"
"background-color:#fbfbfb;\n"
"border-style:outset;\n"
"border-radius:8px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#FFFFFF;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:#c3c3c3;\n"
"}")
        self.pushB_5.setObjectName("pushB_5")
        self.gridLayout.addWidget(self.pushB_5, 3, 1, 1, 1)
        self.pushB_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.pushB_6.sizePolicy().hasHeightForWidth())
        self.pushB_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.pushB_6.setFont(font)
        self.pushB_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushB_6.setStyleSheet("QPushButton{\n"
"font: 25pt \"SimSun-ExtB\";\n"
"background-color:#fbfbfb;\n"
"border-style:outset;\n"
"border-radius:8px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#FFFFFF;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:#c3c3c3;\n"
"}")
        self.pushB_6.setObjectName("pushB_6")
        self.gridLayout.addWidget(self.pushB_6, 3, 2, 1, 1)
        self.pushB_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.pushB_3.sizePolicy().hasHeightForWidth())
        self.pushB_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.pushB_3.setFont(font)
        self.pushB_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushB_3.setStyleSheet("QPushButton{\n"
"font: 25pt \"SimSun-ExtB\";\n"
"background-color:#fbfbfb;\n"
"border-style:outset;\n"
"border-radius:8px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#FFFFFF;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:#c3c3c3;\n"
"}")
        self.pushB_3.setObjectName("pushB_3")
        self.gridLayout.addWidget(self.pushB_3, 4, 2, 1, 1)
        self.pushB_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.pushB_2.sizePolicy().hasHeightForWidth())
        self.pushB_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.pushB_2.setFont(font)
        self.pushB_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushB_2.setStyleSheet("QPushButton{\n"
"font: 25pt \"SimSun-ExtB\";\n"
"background-color:#fbfbfb;\n"
"border-style:outset;\n"
"border-radius:8px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#FFFFFF;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:#c3c3c3;\n"
"}")
        self.pushB_2.setObjectName("pushB_2")
        self.gridLayout.addWidget(self.pushB_2, 4, 1, 1, 1)
        self.pushB_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.pushB_4.sizePolicy().hasHeightForWidth())
        self.pushB_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.pushB_4.setFont(font)
        self.pushB_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushB_4.setStyleSheet("QPushButton{\n"
"font: 25pt \"SimSun-ExtB\";\n"
"background-color:#fbfbfb;\n"
"border-style:outset;\n"
"border-radius:8px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#FFFFFF;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:#c3c3c3;\n"
"}")
        self.pushB_4.setObjectName("pushB_4")
        self.gridLayout.addWidget(self.pushB_4, 3, 0, 1, 1)
        self.pushB_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.pushB_1.sizePolicy().hasHeightForWidth())
        self.pushB_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.pushB_1.setFont(font)
        self.pushB_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushB_1.setStyleSheet("QPushButton{\n"
"font: 25pt \"SimSun-ExtB\";\n"
"background-color:#fbfbfb;\n"
"border-style:outset;\n"
"border-radius:8px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#FFFFFF;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:#c3c3c3;\n"
"}")
        self.pushB_1.setObjectName("pushB_1")
        self.gridLayout.addWidget(self.pushB_1, 4, 0, 1, 1)
        self.pushB_zero = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.pushB_zero.sizePolicy().hasHeightForWidth())
        self.pushB_zero.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.pushB_zero.setFont(font)
        self.pushB_zero.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushB_zero.setStyleSheet("QPushButton{\n"
"font: 25pt \"SimSun-ExtB\";\n"
"background-color:#fbfbfb;\n"
"border-style:outset;\n"
"border-radius:8px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#FFFFFF;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:#c3c3c3;\n"
"}")
        self.pushB_zero.setObjectName("pushB_zero")
        self.gridLayout.addWidget(self.pushB_zero, 5, 1, 1, 1)
        self.pushB_point = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.pushB_point.sizePolicy().hasHeightForWidth())
        self.pushB_point.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.pushB_point.setFont(font)
        self.pushB_point.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushB_point.setStyleSheet("QPushButton{\n"
"font: 25pt \"SimSun-ExtB\";\n"
"background-color: rgb(239, 239, 239);\n"
"border-style:outset;\n"
"border-radius:8px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#f4f4f4;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:#c3c3c3;\n"
"}")
        self.pushB_point.setObjectName("pushB_point")
        self.gridLayout.addWidget(self.pushB_point, 5, 2, 1, 1)
        self.pushB_deg = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.pushB_deg.sizePolicy().hasHeightForWidth())
        self.pushB_deg.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.pushB_deg.setFont(font)
        self.pushB_deg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushB_deg.setStyleSheet("QPushButton{\n"
"font: 25pt \"SimSun-ExtB\";\n"
"background-color: rgb(239, 239, 239);\n"
"border-style:outset;\n"
"border-radius:8px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#f4f4f4;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:#c3c3c3;\n"
"}")
        self.pushB_deg.setObjectName("pushB_deg")
        self.gridLayout.addWidget(self.pushB_deg, 5, 0, 1, 1)
        self.pushB_equals = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.pushB_equals.sizePolicy().hasHeightForWidth())
        self.pushB_equals.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushB_equals.setFont(font)
        self.pushB_equals.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushB_equals.setStyleSheet("QPushButton{\n"
"font: 25pt \"SimSun-ExtB\";\n"
"background-color: #f1d753;\n"
"color:#FFFFFF;\n"
"border-style:outset;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#f2dd8e;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:#e6ba66;\n"
"}")
        self.pushB_equals.setObjectName("pushB_equals")
        self.gridLayout.addWidget(self.pushB_equals, 6, 0, 1, 4)
        self.verticalLayout.addLayout(self.gridLayout)
        TheCalculator.setCentralWidget(self.centralwidget)

        self.retranslateUi(TheCalculator)
        QtCore.QMetaObject.connectSlotsByName(TheCalculator)

        self.pushB_1.clicked.connect(self.method_1)
        self.pushB_2.clicked.connect(self.method_2)
        self.pushB_3.clicked.connect(self.method_3)
        self.pushB_4.clicked.connect(self.method_4)
        self.pushB_5.clicked.connect(self.method_5)
        self.pushB_6.clicked.connect(self.method_6)
        self.pushB_7.clicked.connect(self.method_7)
        self.pushB_8.clicked.connect(self.method_8)
        self.pushB_9.clicked.connect(self.method_9)
        self.pushB_zero.clicked.connect(self.method_zero)
        self.pushB_deg.clicked.connect(self.method_deg)
        self.pushB_point.clicked.connect(self.method_point)
        self.pushB_equals.clicked.connect(self.method_equals)
        self.pushB_plus.clicked.connect(self.method_plus)
        self.pushB_minus.clicked.connect(self.method_minus)
        self.pushB_multi.clicked.connect(self.method_multi)
        self.pushB_div.clicked.connect(self.method_div)
        self.pushB_deg.clicked.connect(self.method_deg)
        self.pushB_Obracket.clicked.connect(self.method_Obracket)
        self.pushB_Cbracket.clicked.connect(self.method_Cbracket)
        self.pushB_clear.clicked.connect(self.method_clear)
        self.pushB_DEL.clicked.connect(self.method_DEL)
        
    def method_1(self):
        text=self.label.text()
        self.label.setText(text+"1")

    def method_2(self):
        text=self.label.text()
        self.label.setText(text+"2")

    def method_3(self):
        text=self.label.text()
        self.label.setText(text+"3")
    def method_4(self):
        text=self.label.text()
        self.label.setText(text+"4")
    def method_5(self):
        text=self.label.text()
        self.label.setText(text+"5")
    def method_6(self):
        text=self.label.text()
        self.label.setText(text+"6")
    def method_7(self):
        text=self.label.text()
        self.label.setText(text+"7")
    def method_8(self):
        text=self.label.text()
        self.label.setText(text+"8")
    def method_9(self):
        text=self.label.text()
        self.label.setText(text+"9")
    def method_zero(self):
        text=self.label.text()
        self.label.setText(text+"0")   
    def method_point(self):
        text=self.label.text()
        self.label.setText(text+".")
    def method_equals(self):
        text=self.label.text()
        try:
            ans=eval(text)
            self.label.setText(str("%.1f" % ans))
        except:
            if text=="":
                self.label.setText(str())
            else:
                self.label.setText("Invalid input")
                
    def method_plus(self):
        text=self.label.text()
        self.label.setText(text+"+")
    def method_minus(self):
        text=self.label.text()
        self.label.setText(text+"-")
    def method_multi(self):
        text=self.label.text()
        self.label.setText(text+"*")
    def method_div(self):
        text=self.label.text()
        self.label.setText(text+"/")
    def method_deg(self):
        text=self.label.text()
        self.label.setText(text+"*")
    def method_Obracket(self):
        text=self.label.text()
        self.label.setText(text+"(")
    def method_Cbracket(self):
        text=self.label.text()
        self.label.setText(text+")")
    def method_clear(self):
        self.label.setText("")
    def method_DEL(self):
        text=self.label.text()
        self.label.setText(text[:len(text)-1])

    def retranslateUi(self, TheCalculator):
        _translate = QtCore.QCoreApplication.translate
        TheCalculator.setWindowTitle(_translate("TheCalculator", "The Calculator"))
        self.pushB_DEL.setText(_translate("TheCalculator", "???"))
        self.pushB_Cbracket.setText(_translate("TheCalculator", ")"))
        self.pushB_clear.setText(_translate("TheCalculator", "AC"))
        self.pushB_multi.setText(_translate("TheCalculator", "??"))
        self.pushB_multi.setShortcut(_translate("TheCalculator", "X"))
        self.pushB_minus.setText(_translate("TheCalculator", "-"))
        self.pushB_plus.setText(_translate("TheCalculator", "+"))
        self.pushB_plus.setShortcut(_translate("TheCalculator", "+"))
        self.pushB_div.setText(_translate("TheCalculator", "??"))
        self.pushB_Obracket.setText(_translate("TheCalculator", "("))
        self.pushB_9.setText(_translate("TheCalculator", "9"))
        self.pushB_8.setText(_translate("TheCalculator", "8"))
        self.pushB_7.setText(_translate("TheCalculator", "7"))
        self.pushB_5.setText(_translate("TheCalculator", "5"))
        self.pushB_6.setText(_translate("TheCalculator", "6"))
        self.pushB_3.setText(_translate("TheCalculator", "3"))
        self.pushB_2.setText(_translate("TheCalculator", "2"))
        self.pushB_4.setText(_translate("TheCalculator", "4"))
        self.pushB_1.setText(_translate("TheCalculator", "1"))
        self.pushB_zero.setText(_translate("TheCalculator", "0"))
        self.pushB_point.setText(_translate("TheCalculator", "???"))
        self.pushB_point.setShortcut(_translate("TheCalculator", "."))
        self.pushB_deg.setText(_translate("TheCalculator", "x???"))
        self.pushB_equals.setText(_translate("TheCalculator", "="))
        self.pushB_equals.setShortcut(_translate("TheCalculator", "="))

    def retranslateUi(self, TheCalculator):
        _translate = QtCore.QCoreApplication.translate
        TheCalculator.setWindowTitle(_translate("TheCalculator", "The Calculator"))
        self.pushB_DEL.setText(_translate("TheCalculator", "???"))
        self.pushB_Cbracket.setText(_translate("TheCalculator", ")"))
        self.pushB_clear.setText(_translate("TheCalculator", "AC"))
        self.pushB_multi.setText(_translate("TheCalculator", "??"))
        self.pushB_multi.setShortcut(_translate("TheCalculator", "X"))
        self.pushB_minus.setText(_translate("TheCalculator", "-"))
        self.pushB_plus.setText(_translate("TheCalculator", "+"))
        self.pushB_plus.setShortcut(_translate("TheCalculator", "+"))
        self.pushB_div.setText(_translate("TheCalculator", "??"))
        self.pushB_Obracket.setText(_translate("TheCalculator", "("))
        self.pushB_9.setText(_translate("TheCalculator", "9"))
        self.pushB_8.setText(_translate("TheCalculator", "8"))
        self.pushB_7.setText(_translate("TheCalculator", "7"))
        self.pushB_5.setText(_translate("TheCalculator", "5"))
        self.pushB_6.setText(_translate("TheCalculator", "6"))
        self.pushB_3.setText(_translate("TheCalculator", "3"))
        self.pushB_2.setText(_translate("TheCalculator", "2"))
        self.pushB_4.setText(_translate("TheCalculator", "4"))
        self.pushB_1.setText(_translate("TheCalculator", "1"))
        self.pushB_zero.setText(_translate("TheCalculator", "0"))
        self.pushB_point.setText(_translate("TheCalculator", "???"))
        self.pushB_point.setShortcut(_translate("TheCalculator", "."))
        self.pushB_deg.setText(_translate("TheCalculator", "x???"))
        self.pushB_equals.setText(_translate("TheCalculator", "="))
        self.pushB_equals.setShortcut(_translate("TheCalculator", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TheCalculator = QtWidgets.QMainWindow()
    ui = Ui_TheCalculator()
    ui.setupUi(TheCalculator)
    TheCalculator.show()
    sys.exit(app.exec_())
