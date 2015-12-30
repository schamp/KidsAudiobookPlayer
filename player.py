import json
import pdb
import os
import socket
import sys

from PySide import QtGui, QtCore
from ui_player import Ui_Player

from PersistentMPDClient.PersistentMPDClient import PersistentMPDClient
from AudiobookManager.AudiobookManager import AudiobookManager

keep_debugging = True

class CheckedFilterProxyModel(QtGui.QSortFilterProxyModel):
    """Only pass through items that have been "checked" in the
    source model"""
    def filterAcceptsRow(self, source_row, source_parent):
        try:
#            print("Filtering on row: {}".format(source_row))
            index = self.sourceModel().index(source_row, 0, source_parent)
#            print("Index: {}".format(index))
            item = self.sourceModel().itemFromIndex(index)
#            print("Item: {}".format(item))
            checked = item.checkState()
#            print("Checked: {}".format(checked))
            return checked == QtCore.Qt.Checked
        except Exception as e:
            pass
        return True

    def data(self, index, role):
        """Force no checkbox to be shown, otherwise, behave as source model."""
        if not index.isValid():
            return None
        elif role == QtCore.Qt.CheckStateRole:
            return None
        else:
            return super().data(index, role)

class PlayerMainWindow(QtGui.QMainWindow):
    def __init__(self, 
                 config_file,
                 local_audiobook_file_path,
                 remote_audiobook_file_path,
                 library_audiobook_path, 
                 socket=None, 
                 host=None, 
                 port=None, 
                 debug=False,
                 parent=None):
        super(PlayerMainWindow, self).__init__(parent)

        print("Config_File: {}".format(config_file))
        print("Local path: {}".format(local_audiobook_file_path))
        print("Remote Path: {}".format(remote_audiobook_file_path))
        print("Library path: {}".format(library_audiobook_path))

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
        self.debug  = debug

        if socket:
            self.client = PersistentMPDClient(socket = socket)
        else:
            self.client = PersistentMPDClient(host = host, port = port)

        self.audiobook_manager = AudiobookManager(audiobook_file_path    = self.local_audiobook_file_path,
                                                  library_audiobook_path = self.library_audiobook_path,
                                                  client                 = self.client,
                                                  debug                  = self.debug)

        self.config_file = config_file
        self.config = {}
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as fin:
                try:
                    self.config = json.load(fin)
                except ValueError as e:
                    print("Error reading config file.")

        if not self.config or 'selected_books' not in self.config:
            print("Warning, config file not found, using empty config")
            self.config = {
                'selected_books': {}, # dict of "author: title" to bool, True if selected
            }

        # FIXME: identify currently playing book

        self.ui = Ui_Player()
        self.ui.setupUi(self)

        self.bookListModel = QtGui.QStandardItemModel(self)
        self.bookListModel.itemChanged.connect(self.itemChanged)


        self.bookListProxyModel = CheckedFilterProxyModel(self)
        self.bookListProxyModel.setSourceModel(self.bookListModel)
        self.bookListProxyModel.setDynamicSortFilter(True)

        self.ui.bookList.setModel(self.bookListProxyModel)
        self.ui.bookSelectList.setModel(self.bookListModel)

        self.reloadBookList()
    
        self.ui.stopButton.clicked.connect(self.client.stop)
        self.ui.playPauseButton.clicked.connect(self.playPause)

        self.ui.nextButton.setText("Bedtime")
        self.ui.nextButton.clicked.connect(self.bedtime)

        self.ui.bookList.clicked.connect(self.playBook)

        self.ui.nextPageButton.clicked.connect(self.nextBookListPage)
        self.ui.prevPageButton.clicked.connect(self.prevBookListPage)

        self.ui.booksButton.clicked.connect(self.toggleBookList)
        self.ui.menuButton.clicked.connect(self.toggleMenu)

        self.ui.selectBooksButton.clicked.connect(self.showBookSelectList)
        self.ui.nextSelectPageButton.clicked.connect(self.nextBookSelectListPage)
        self.ui.prevSelectPageButton.clicked.connect(self.prevBookSelectListPage)

        self.current_book_list_index        = 0
        self.current_book_select_list_index = 0

    def playBook(self, index):
        item = self.bookListProxyModel.itemFromIndex(index)
        book = item.data()
        print("Item selected: {} ({})".format(item, book))
        pixmap = QtGui.QPixmap(self.audiobook_manager.get_album_image(book))
        self.ui.albumImageLabel.setPixmap(pixmap)
        self.ui.albumTextLabel.setText("{} - {}".format(book['author'], book['title']))
        self.audiobook_manager.play_audiobook(book)

    def bedtime(self):
        self.client.clear()
        self.client.findadd('artist', 'David Phillips')

    def playPause(self):
        if self.client.status()['state'] == 'stop':
            self.client.play()
        else:
            self.client.pause()

    def reloadBookList(self):
        self.bookListModel.clear()

        audiobooks = self.audiobook_manager.list_audiobooks()

        for i, book in enumerate(audiobooks, start=1):
            # select all books by default
            if book['uri'] not in self.config['selected_books']:
                self.config['selected_books'][book['uri']] = True

            item = QtGui.QStandardItem("{}\n{}".format(book['author'], book['title']))
            item.setData(book)
            item.setSizeHint(QtCore.QSize(140, 175))
            item.setCheckable(True)
            
            if not self.config.get('selected_books') \
                or self.config.get('selected_books').get(book['uri'], False):
                item.setCheckState(QtCore.Qt.Checked)
            album_image = self.audiobook_manager.get_album_image(book)
            item.setIcon(QtGui.QIcon(album_image))
            self.bookListModel.appendRow(item)
        self.writeConfig()
    
    def writeConfig(self):
        print("Writing config file...")
        with open(self.config_file, 'w') as fout:
            json.dump(self.config, fout)

    def itemChanged(self, item):
        # triggered when an item is newly checked.
        # update the config
        data = item.data()
        self.config['selected_books'][data['uri']] = item.checkState() == QtCore.Qt.Checked
        # write the updated config out to disk (because we'll reload it the next time we go to update the book list
        self.writeConfig()

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

    def showBookSelectList(self):
        # load the book list and the config
        self.reloadBookList()
        self.ui.stackedWidget.setCurrentIndex(3)
        
    def nextBookListPage(self):
        self.current_book_list_index += 2
        if self.current_book_list_index % 2 == 0:
            self.current_book_list_index += 1
        self.current_book_list_index = min(self.current_book_list_index, self.bookListModel.rowCount())
        self.scrollBookListTo(self.current_book_list_index)

    def scrollBookListTo(self, pos):
        pos = min(pos, self.bookListModel.rowCount())
        item = self.bookListModel.item(pos)
        pos = max(0, pos)
        index = self.bookListModel.indexFromItem(item)
        self.ui.bookList.scrollTo(index, QtGui.QAbstractItemView.PositionAtBottom)

    def prevBookListPage(self):
        self.current_book_list_index -= 2
        if self.current_book_list_index % 2 == 1:
            self.current_book_list_index -= 1
        self.current_book_list_index = max(0, self.current_book_list_index)
        self.scrollBookListTo(self.current_book_list_index)

    def nextBookSelectListPage(self):
        self.current_book_select_list_index += 2
        if self.current_book_select_list_index % 2 == 0:
            self.current_book_select_list_index += 1
        self.current_book_select_list_index = min(self.current_book_select_list_index, self.bookListModel.rowCount())
        self.scrollBookListTo(self.current_book_select_list_index)

    def scrollBookSelectListTo(self, pos):
        pos = min(pos, self.bookListModel.rowCount())
        item = self.bookListModel.item(pos)
        pos = max(0, pos)
        index = self.bookListModel.indexFromItem(item)
        self.ui.bookList.scrollTo(index, QtGui.QAbstractItemView.PositionAtBottom)

    def prevBookSelectListPage(self):
        self.current_book_select_list_index -= 2
        if self.current_book_select_list_index % 2 == 1:
            self.current_book_select_list_index -= 1
        self.current_book_select_list_index = max(0, self.current_book_select_list_index)
        self.scrollBookListTo(self.current_book_select_list_index)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config",  action="store", default="player.json", help="The path to the player config file.")
    parser.add_argument("-d", "--debug",   action="store_true",           help="Don't reset the playlist to the bedtime playlist.")
    parser.add_argument("-s", "--socket",  action="store", default=None,  help="The local socket object to connect to.")
    parser.add_argument("-a", "--address", action="store", default=None,  help="The address of the host to connect to.")
    parser.add_argument("-p", "--port",    action="store", default=6600,  help="The port on the host to connect to.")
    parser.add_argument("-l", "--local",   action="store", default="N:\Audiobooks", help="The path to the audiobooks on the local filesystem.")
    parser.add_argument("-r", "--remote",  action="store", default="/mnt/nas/Audiobooks", help="The path to the audioboks on the remote (target) filesystem")
    parser.add_argument("--library",       action="store", default="NAS/Audiobooks",      help="The path to the audiobooks in the MPD library database on the target.")

    args = parser.parse_args()

    app = QtGui.QApplication(sys.argv)

    mySW = PlayerMainWindow(config_file                = args.config,
                            local_audiobook_file_path  = args.local,
                            remote_audiobook_file_path = args.remote,
                            library_audiobook_path     = args.library,
                            socket                     = args.socket,
                            host                       = args.address,
                            port                       = args.port,
                            debug                      = args.debug)
    mySW.show()
    mySW.showPlayer()

#    if not args.debug:
#        mySW.bedtime()

    sys.exit(app.exec_())
