# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'player.ui'
#
# Created: Wed Dec 30 05:54:00 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Player(object):
    def setupUi(self, Player):
        Player.setObjectName("Player")
        Player.resize(320, 240)
        self.centralWidget = QtGui.QWidget(Player)
        self.centralWidget.setObjectName("centralWidget")
        self.stackedWidget = QtGui.QStackedWidget(self.centralWidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 320, 200))
        self.stackedWidget.setObjectName("stackedWidget")
        self.bookPage = QtGui.QWidget()
        self.bookPage.setObjectName("bookPage")
        self.bookList = QtGui.QListView(self.bookPage)
        self.bookList.setGeometry(QtCore.QRect(40, 0, 240, 200))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bookList.sizePolicy().hasHeightForWidth())
        self.bookList.setSizePolicy(sizePolicy)
        self.bookList.setMinimumSize(QtCore.QSize(240, 200))
        self.bookList.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.bookList.setAutoScroll(False)
        self.bookList.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.bookList.setProperty("showDropIndicator", False)
        self.bookList.setIconSize(QtCore.QSize(100, 100))
        self.bookList.setMovement(QtGui.QListView.Static)
        self.bookList.setFlow(QtGui.QListView.LeftToRight)
        self.bookList.setProperty("isWrapping", False)
        self.bookList.setGridSize(QtCore.QSize(120, 175))
        self.bookList.setViewMode(QtGui.QListView.IconMode)
        self.bookList.setUniformItemSizes(True)
        self.bookList.setWordWrap(True)
        self.bookList.setObjectName("bookList")
        self.prevPageButton = QtGui.QPushButton(self.bookPage)
        self.prevPageButton.setEnabled(True)
        self.prevPageButton.setGeometry(QtCore.QRect(0, 0, 40, 200))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prevPageButton.sizePolicy().hasHeightForWidth())
        self.prevPageButton.setSizePolicy(sizePolicy)
        self.prevPageButton.setMinimumSize(QtCore.QSize(0, 0))
        self.prevPageButton.setMaximumSize(QtCore.QSize(500, 500))
        self.prevPageButton.setObjectName("prevPageButton")
        self.nextPageButton = QtGui.QPushButton(self.bookPage)
        self.nextPageButton.setGeometry(QtCore.QRect(280, 0, 40, 200))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextPageButton.sizePolicy().hasHeightForWidth())
        self.nextPageButton.setSizePolicy(sizePolicy)
        self.nextPageButton.setMinimumSize(QtCore.QSize(0, 0))
        self.nextPageButton.setMaximumSize(QtCore.QSize(200, 200))
        self.nextPageButton.setObjectName("nextPageButton")
        self.stackedWidget.addWidget(self.bookPage)
        self.playerPage = QtGui.QWidget()
        self.playerPage.setObjectName("playerPage")
        self.albumTextLabel = QtGui.QLabel(self.playerPage)
        self.albumTextLabel.setGeometry(QtCore.QRect(70, 180, 180, 20))
        self.albumTextLabel.setObjectName("albumTextLabel")
        self.browseLeft = QtGui.QPushButton(self.playerPage)
        self.browseLeft.setEnabled(True)
        self.browseLeft.setGeometry(QtCore.QRect(0, 0, 70, 200))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browseLeft.sizePolicy().hasHeightForWidth())
        self.browseLeft.setSizePolicy(sizePolicy)
        self.browseLeft.setMinimumSize(QtCore.QSize(0, 0))
        self.browseLeft.setMaximumSize(QtCore.QSize(500, 500))
        self.browseLeft.setObjectName("browseLeft")
        self.albumImageLabel = QtGui.QLabel(self.playerPage)
        self.albumImageLabel.setGeometry(QtCore.QRect(70, 0, 180, 180))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.albumImageLabel.sizePolicy().hasHeightForWidth())
        self.albumImageLabel.setSizePolicy(sizePolicy)
        self.albumImageLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.albumImageLabel.setMaximumSize(QtCore.QSize(200, 200))
        self.albumImageLabel.setBaseSize(QtCore.QSize(200, 200))
        self.albumImageLabel.setScaledContents(True)
        self.albumImageLabel.setObjectName("albumImageLabel")
        self.browseRight = QtGui.QPushButton(self.playerPage)
        self.browseRight.setGeometry(QtCore.QRect(250, 0, 70, 200))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browseRight.sizePolicy().hasHeightForWidth())
        self.browseRight.setSizePolicy(sizePolicy)
        self.browseRight.setMinimumSize(QtCore.QSize(0, 0))
        self.browseRight.setMaximumSize(QtCore.QSize(200, 200))
        self.browseRight.setObjectName("browseRight")
        self.stackedWidget.addWidget(self.playerPage)
        self.menuPage = QtGui.QWidget()
        self.menuPage.setObjectName("menuPage")
        self.selectBooksButton = QtGui.QPushButton(self.menuPage)
        self.selectBooksButton.setGeometry(QtCore.QRect(10, 10, 90, 70))
        self.selectBooksButton.setMinimumSize(QtCore.QSize(90, 70))
        self.selectBooksButton.setMaximumSize(QtCore.QSize(90, 70))
        self.selectBooksButton.setObjectName("selectBooksButton")
        self.stackedWidget.addWidget(self.menuPage)
        self.bookSelectPage = QtGui.QWidget()
        self.bookSelectPage.setObjectName("bookSelectPage")
        self.bookSelectList = QtGui.QListView(self.bookSelectPage)
        self.bookSelectList.setGeometry(QtCore.QRect(40, 0, 240, 200))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bookSelectList.sizePolicy().hasHeightForWidth())
        self.bookSelectList.setSizePolicy(sizePolicy)
        self.bookSelectList.setMinimumSize(QtCore.QSize(240, 200))
        self.bookSelectList.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.bookSelectList.setAutoScroll(False)
        self.bookSelectList.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.bookSelectList.setProperty("showDropIndicator", False)
        self.bookSelectList.setIconSize(QtCore.QSize(100, 100))
        self.bookSelectList.setMovement(QtGui.QListView.Static)
        self.bookSelectList.setFlow(QtGui.QListView.LeftToRight)
        self.bookSelectList.setProperty("isWrapping", False)
        self.bookSelectList.setGridSize(QtCore.QSize(120, 175))
        self.bookSelectList.setViewMode(QtGui.QListView.IconMode)
        self.bookSelectList.setUniformItemSizes(True)
        self.bookSelectList.setWordWrap(True)
        self.bookSelectList.setObjectName("bookSelectList")
        self.prevSelectPageButton = QtGui.QPushButton(self.bookSelectPage)
        self.prevSelectPageButton.setEnabled(True)
        self.prevSelectPageButton.setGeometry(QtCore.QRect(0, 0, 40, 200))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prevSelectPageButton.sizePolicy().hasHeightForWidth())
        self.prevSelectPageButton.setSizePolicy(sizePolicy)
        self.prevSelectPageButton.setMinimumSize(QtCore.QSize(0, 0))
        self.prevSelectPageButton.setMaximumSize(QtCore.QSize(500, 500))
        self.prevSelectPageButton.setObjectName("prevSelectPageButton")
        self.nextSelectPageButton = QtGui.QPushButton(self.bookSelectPage)
        self.nextSelectPageButton.setGeometry(QtCore.QRect(280, 0, 40, 200))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextSelectPageButton.sizePolicy().hasHeightForWidth())
        self.nextSelectPageButton.setSizePolicy(sizePolicy)
        self.nextSelectPageButton.setMinimumSize(QtCore.QSize(0, 0))
        self.nextSelectPageButton.setMaximumSize(QtCore.QSize(200, 200))
        self.nextSelectPageButton.setObjectName("nextSelectPageButton")
        self.stackedWidget.addWidget(self.bookSelectPage)
        self.controlWidget = QtGui.QWidget(self.centralWidget)
        self.controlWidget.setGeometry(QtCore.QRect(0, 200, 320, 40))
        self.controlWidget.setObjectName("controlWidget")
        self.nextButton = QtGui.QPushButton(self.controlWidget)
        self.nextButton.setGeometry(QtCore.QRect(210, 3, 45, 35))
        self.nextButton.setMinimumSize(QtCore.QSize(45, 35))
        self.nextButton.setMaximumSize(QtCore.QSize(45, 35))
        self.nextButton.setObjectName("nextButton")
        self.stopButton = QtGui.QPushButton(self.controlWidget)
        self.stopButton.setGeometry(QtCore.QRect(110, 3, 45, 35))
        self.stopButton.setMinimumSize(QtCore.QSize(45, 35))
        self.stopButton.setMaximumSize(QtCore.QSize(45, 35))
        self.stopButton.setObjectName("stopButton")
        self.menuButton = QtGui.QPushButton(self.controlWidget)
        self.menuButton.setGeometry(QtCore.QRect(270, 3, 45, 35))
        self.menuButton.setMaximumSize(QtCore.QSize(45, 35))
        self.menuButton.setObjectName("menuButton")
        self.booksButton = QtGui.QPushButton(self.controlWidget)
        self.booksButton.setGeometry(QtCore.QRect(5, 3, 45, 35))
        self.booksButton.setMinimumSize(QtCore.QSize(45, 35))
        self.booksButton.setMaximumSize(QtCore.QSize(45, 35))
        self.booksButton.setObjectName("booksButton")
        self.playPauseButton = QtGui.QPushButton(self.controlWidget)
        self.playPauseButton.setGeometry(QtCore.QRect(160, 3, 45, 35))
        self.playPauseButton.setMinimumSize(QtCore.QSize(45, 35))
        self.playPauseButton.setMaximumSize(QtCore.QSize(45, 35))
        self.playPauseButton.setObjectName("playPauseButton")
        self.prevButton = QtGui.QPushButton(self.controlWidget)
        self.prevButton.setGeometry(QtCore.QRect(60, 3, 45, 35))
        self.prevButton.setMinimumSize(QtCore.QSize(45, 35))
        self.prevButton.setMaximumSize(QtCore.QSize(45, 35))
        self.prevButton.setObjectName("prevButton")
        Player.setCentralWidget(self.centralWidget)

        self.retranslateUi(Player)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Player)

    def retranslateUi(self, Player):
        Player.setWindowTitle(QtGui.QApplication.translate("Player", "Player", None, QtGui.QApplication.UnicodeUTF8))
        self.prevPageButton.setText(QtGui.QApplication.translate("Player", "Prev\n"
"Page", None, QtGui.QApplication.UnicodeUTF8))
        self.nextPageButton.setText(QtGui.QApplication.translate("Player", "Next\n"
"Page", None, QtGui.QApplication.UnicodeUTF8))
        self.albumTextLabel.setText(QtGui.QApplication.translate("Player", "Current Song Info", None, QtGui.QApplication.UnicodeUTF8))
        self.browseLeft.setText(QtGui.QApplication.translate("Player", "Prev\n"
"Album", None, QtGui.QApplication.UnicodeUTF8))
        self.albumImageLabel.setText(QtGui.QApplication.translate("Player", "Current Album Info", None, QtGui.QApplication.UnicodeUTF8))
        self.browseRight.setText(QtGui.QApplication.translate("Player", "Next\n"
"Album", None, QtGui.QApplication.UnicodeUTF8))
        self.selectBooksButton.setText(QtGui.QApplication.translate("Player", "Select Books", None, QtGui.QApplication.UnicodeUTF8))
        self.prevSelectPageButton.setText(QtGui.QApplication.translate("Player", "Prev\n"
"Page", None, QtGui.QApplication.UnicodeUTF8))
        self.nextSelectPageButton.setText(QtGui.QApplication.translate("Player", "Next\n"
"Page", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setText(QtGui.QApplication.translate("Player", "Next\n"
"Song", None, QtGui.QApplication.UnicodeUTF8))
        self.stopButton.setText(QtGui.QApplication.translate("Player", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.menuButton.setText(QtGui.QApplication.translate("Player", "Menu", None, QtGui.QApplication.UnicodeUTF8))
        self.booksButton.setText(QtGui.QApplication.translate("Player", "Books", None, QtGui.QApplication.UnicodeUTF8))
        self.playPauseButton.setText(QtGui.QApplication.translate("Player", "Play/\n"
"Pause", None, QtGui.QApplication.UnicodeUTF8))
        self.prevButton.setText(QtGui.QApplication.translate("Player", "Prev\n"
"Song", None, QtGui.QApplication.UnicodeUTF8))

