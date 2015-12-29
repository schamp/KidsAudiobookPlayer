import pdb
import os
import socket
import sys

from PySide import QtGui, QtCore
from ui_player import Ui_Player

from PersistentMPDClient.PersistentMPDClient import PersistentMPDClient
from AudiobookManager.AudiobookManager import AudiobookManager

class PlayerMainWindow(QtGui.QMainWindow):
    def __init__(self, 
                 local_audiobook_file_path,
                 remote_audiobook_file_path,
                 library_audiobook_path, 
                 socket=None, 
                 host=None, 
                 port=None, 
                 parent=None):
        super(PlayerMainWindow, self).__init__(parent)

        print("Socket:  {}".format(socket))
        print("Host:    {}".format(host))
        print("Port:    {}".format(port))

        self.local_audiobook_file_path  = local_audiobook_file_path
        self.remote_audiobook_file_path = remote_audiobook_file_path
        self.library_audiobook_path     = library_audiobook_path

        if not socket and (not host or not port):
            print("Must provide either socket or host and port to client.")
            sys.exit()

        self.socket = socket
        self.host   = host
        self.port   = port

        if socket:
            self.client = PersistentMPDClient(socket = socket)
        else:
            self.client = PersistentMPDClient(host = host, port = port)

        self.audiobook_manager = AudiobookManager(audiobook_file_path    = self.remote_audiobook_file_path,
                                                  library_audiobook_path = self.library_audiobook_path,
                                                  client                 = self.client)

        self.ui = Ui_Player()
        self.ui.setupUi(self)

        self.ui.stopButton.clicked.connect(self.client.stop)
        self.ui.playPauseButton.clicked.connect(self.playPause)

        self.ui.nextButton.setText("Bedtime")
        self.ui.nextButton.clicked.connect(self.bedtime)

#        self.ui.prevButton.setText("Thomas")
#        self.ui.prevButton.clicked.connect(self.thomas)

#        self.ui.browseRight.setText("Frog and Toad")
#        self.ui.browseRight.clicked.connect(self.frogtoad)

#        self.ui.browseLeft.setText("Mouse Tales")
#        self.ui.browseLeft.clicked.connect(self.mousetales)

        self.audiobooks = self.audiobook_manager.list_audiobooks()

        self.ui.bookList.setViewMode(QtGui.QListView.IconMode)
        self.ui.bookList.setIconSize(QtCore.QSize(100,100))

        self.model = QtGui.QStandardItemModel(self.ui.bookList)

        for book in self.audiobooks:
            item = QtGui.QStandardItem("{}\n{}".format(book['author'], book['title']))
            item.setData(book)
            item.setSizeHint(QtCore.QSize(140, 175))
#            item.setCheckable(True)
#            print("URI: {}".format(book['uri']))
            audiobook_path = book['uri'].replace(self.library_audiobook_path, self.local_audiobook_file_path)
#            print("Audiobook_path: {}".format(audiobook_path))
            # os.path.normpath should convert foward slashes to back slashes for windows
            audiobook_path = os.path.normpath(audiobook_path)
#            print("Looking for album image in path: {}".format(audiobook_path))
            item.setIcon(QtGui.QIcon(os.path.join(audiobook_path, 'cover.jpg')))
            self.model.appendRow(item)

        self.ui.bookList.setModel(self.model)
        self.ui.bookList.clicked.connect(self.bookSelected)

        self.ui.nextPageButton.clicked.connect(self.nextPage)
        self.ui.prevPageButton.clicked.connect(self.prevPage)

        self.ui.booksButton.clicked.connect(self.toggleBookList)
        self.ui.menuButton.clicked.connect(self.toggleMenu)

        # might need to make this 1
        self.current_index = 0

    def bookSelected(self, index):
        item = self.model.itemFromIndex(index)
        book = item.data()
        print("Item selected: {} ({})".format(item, book))
        self.audiobook_manager.play_audiobook(book)

    def bedtime(self):
        self.client.clear()
        self.client.findadd('artist', 'David Phillips')

    def playPause(self):
        if self.client.status()['state'] == 'stop':
            self.client.play()
        else:
            self.client.pause()

    def showBookList(self):
        self.ui.booksButton.setText('Player')
        self.ui.menuButton.setText('Menu')
        self.ui.stackedWidget.setCurrentIndex(0)

    def showPlayer(self):
        self.ui.booksButton.setText('Books')
        self.ui.menuButton.setText('Menu')
        self.ui.stackedWidget.setCurrentIndex(1)

    def showMenu(self):
        self.ui.booksButton.setText('Books')
        self.ui.menuButton.setText('Player')
        self.ui.stackedWidget.setCurrentIndex(2)
    
    def toggleBookList(self):
        if self.ui.stackedWidget.currentIndex() == 0:
            self.showPlayer()
        else:
            self.showBookList()

    def toggleMenu(self):
        if self.ui.stackedWidget.currentIndex() == 2:
            self.showPlayer()
        else:
            self.showMenu()

    def nextPage(self):
        self.current_index += 2
        if self.current_index % 2 == 0:
            self.current_index += 1
        self.current_index = min(self.current_index, len(self.audiobooks))
        self.scrollTo(self.current_index)

    def scrollTo(self, pos):
        pos = min(pos, len(self.audiobooks))
        item = self.model.item(pos)
#        data = item.data() if item else None
#        uri = data['uri'] if data else None
#        print("scrolling to: {} ({})".format(pos, uri))
        pos = max(0, pos)
        index = self.model.indexFromItem(item)
        self.ui.bookList.scrollTo(index, QtGui.QAbstractItemView.PositionAtBottom)

    def prevPage(self):
        self.current_index -= 2
        if self.current_index % 2 == 1:
            self.current_index -= 1
        self.current_index = max(0, self.current_index)
        self.scrollTo(self.current_index)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug",   action="store_true",           help="Don't reset the playlist to the bedtime playlist.")
    parser.add_argument("-s", "--socket",  action="store", default=None,  help="The local socket object to connect to.")
    parser.add_argument("-a", "--address", action="store", default=None,  help="The address of the host to connect to.")
    parser.add_argument("-p", "--port",    action="store", default=6600,  help="The port on the host to connect to.")
    parser.add_argument("-l", "--local",   action="store", default="N:\Audiobooks", help="The path to the audiobooks on the local filesystem.")
    parser.add_argument("-r", "--remote",  action="store", default="/mnt/nas/Audiobooks", help="The path to the audioboks on the remote (target) filesystem")
    parser.add_argument("--library",       action="store", default="NAS/Audiobooks",      help="The path to the audiobooks in the MPD library database on the target.")

    args = parser.parse_args()

    app = QtGui.QApplication(sys.argv)

    mySW = PlayerMainWindow(local_audiobook_file_path  = args.local,
                            remote_audiobook_file_path = args.remote,
                            library_audiobook_path     = args.library,
                            socket                     = args.socket,
                            host                       = args.address,
                            port                       = args.port)
    mySW.show()
    mySW.showBookList()
#    mySW.ui.stackedWidget.setCurrentIndex(1)

#    if not args.debug:
#        mySW.bedtime()

    sys.exit(app.exec_())
