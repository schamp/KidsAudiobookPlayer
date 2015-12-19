
import os
import socket
import sys

from PySide import QtGui, QtCore
from ui_player import Ui_Player

import mpd

class PlayerMainWindow(QtGui.QMainWindow):
    def __init__(self, library, socket=None, host=None, port=None, parent=None):
        super(PlayerMainWindow, self).__init__(parent)

        print("Library: {}".format(library))
        print("Socket:  {}".format(socket))
        print("Host:    {}".format(host))
        print("Port:    {}".format(port))

        self.library = library

        if not socket and (not host or not port):
            print("Must provide either socket or host and port to client.")
            sys.exit()

        self.socket = socket
        self.host   = host
        self.port   = port

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)

        self.client = mpd.MPDClient()
        self.client.timeout = 10
        self.client.idletimeout = None

        self.connect()

        self.ui = Ui_Player()
        self.ui.setupUi(self)

        self.ui.stopButton.clicked.connect(self.client.stop)
        self.ui.playPauseButton.clicked.connect(self.playPause)

        self.ui.nextButton.setText("Bedtime")
        self.ui.nextButton.clicked.connect(self.bedtime)

        self.ui.prevButton.setText("Thomas")
        self.ui.prevButton.clicked.connect(self.thomas)

        self.ui.browseRight.setText("Frog and Toad")
        self.ui.browseRight.clicked.connect(self.frogtoad)

        self.ui.browseLeft.setText("Mouse Tales")
        self.ui.browseLeft.clicked.connect(self.mousetales)

        self.users = sorted(name for name in os.listdir(self.library) if os.path.isdir(os.path.join(self.library, name)))
        print("Found users: {}".format(", ".join(self.users)))

        for user in self.users:
            userWidget = QtGui.QListWidgetItem(user)
            self.ui.userList.addItem(userWidget)

        self.ui.userButton.clicked.connect(self.showUserList)
        self.ui.menuButton.clicked.connect(self.showMenu)

    def bedtime(self):
        self.client.clear()
        self.client.findadd('artist', 'David Phillips')

    def thomas(self):
        self.client.clear()
        self.client.findadd('artist', 'Reverend W. Awdry')

    def frogtoad(self):
        self.client.clear()
        self.client.findadd('album', 'Frog and Toad')

    def mousetales(self):
        self.client.clear()
        self.client.findadd('album', 'Mouse Tales')

    def update(self):
        try:
            self.client.ping()
        except (mpd.ConnectionError, OSError) as e:
            print("Lost connection.")
            self.connect()


    def connect(self):
        try:
            try:
                # disconnect if we need to, but if it fails, don't care
                self.client.disconnect()
            except mpd.ConnectionError as e:
                pass
            if self.socket:
                print("Connecting to {}".format(self.socket))
                self.client.connect(s.socket, None)
            else:
                print("Connecting to {}:{}".format(self.host, self.port))
                self.client.connect(self.host, self.port)
        except socket.error as e:
            print("Connection refused.")

    def playPause(self):
        if self.client.status()['state'] == 'stop':
            self.client.play()
        else:
            self.client.pause()

    def showUserList(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def showMenu(self):
        self.ui.stackedWidget.setCurrentIndex(1)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug",   action="store_true",           help="Don't reset the playlist to the bedtime playlist.")
    parser.add_argument("-s", "--socket",  action="store", default=None,  help="The local socket object to connect to.")
    parser.add_argument("-a", "--address", action="store", default=None,  help="The address of the host to connect to.")
    parser.add_argument("-p", "--port",    action="store", default=6600,  help="The port on the host to connect to.")
    parser.add_argument("-l", "--library", action="store", required=True, help="The path to the music library, as seen my MPD.")
    args = parser.parse_args()

    app = QtGui.QApplication(sys.argv)

    mySW = PlayerMainWindow(library = args.library,
                            socket  = args.socket,
                            host    = args.address,
                            port    = args.port)
    mySW.show()
    mySW.showMenu()
#    mySW.ui.stackedWidget.setCurrentIndex(1)

#    if not args.debug:
#        mySW.bedtime()

    sys.exit(app.exec_())
