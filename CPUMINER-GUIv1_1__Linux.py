#!/usr/bin/env python3

#   This is the CPU GUI Miner, which is a light software that has a better frontend for easier use of running a miner.
#   Copyright (C) 2019-2020  Nugetzrul3
#   Copyright (C) 2025  Crypto Lover

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

import json
import sys

from PyQt5 import QtCore, QtGui, QtWidgets

path = 'cpuminerrkz/'

class Ui_Form(object):

    def __init__(self):
        super().__init__()

        self.setupUi(Form)

    def setupUi(self, Form):
        config = {}
        with open('minerconfig.json', 'r') as f:
            config = (json.load(f))

        Form.setObjectName("Form")
        Form.resize(800, 800)
        Form.setMinimumSize(QtCore.QSize(800, 800))
        Form.setMaximumSize(QtCore.QSize(800, 800))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("cpu-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Form.setWindowIcon(icon)

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 510, 160))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_3.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 200, 80, 31))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 250, 80, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")

        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(10, 350, 80, 38))
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(10, 350, 100, 39))
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(120, 200, 211, 21))
        self.lineEdit.setText(config['URL'])
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 250, 211, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setText(config['address'])

        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 300, 211, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setText(config['username'])

        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 350, 211, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setText(config['password'])

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(510, 0, 71, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(511, 16777215))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("cpu-logo.png"))
        self.label_2.setObjectName("label_2")

        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(530, 30, 47, 13))
        self.label_5.setOpenExternalLinks(True)
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(530, 50, 47, 16))
        self.label_6.setOpenExternalLinks(True)
        self.label_6.setObjectName("label_6")

        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(530, 65, 130, 51))
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(10, 300, 100, 39))
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 270, 75, 25))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(600, 270, 75, 25))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(700, 270, 75, 25))
        self.pushButton_3.setObjectName("pushbutton_3")

        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(350, 300, 100, 20))
        self.label_11.setWordWrap(True)
        self.label_11.setObjectName("label_11")

        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(430, 300, 30, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setText(config['threads'])

        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(350, 320, 150, 60))
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")

        self.combobox = QtWidgets.QComboBox(Form)
        self.combobox.setGeometry(QtCore.QRect(360, 225, 150, 22))
        self.combobox.addItems(['-—SELECT-—', 'yespower', 'yespoweradvc', 'yespowersugar', 'yespowerltncg','yespowerlitb' ,'yespowerr16' , 'yespowerurx', 'yescrypt', 'yescryptr8', 'yescryptr32', 'yescryptr16', 'argon2d250', 'argon2d500', 'argon2d4096', 'power2b', 'cpupower'])
        self.combobox.setCurrentText(config['algorithm'])
        self.combobox.setObjectName('combobox')

        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(360, 200, 61, 20)

        self.TextEdit1 = QtWidgets.QPlainTextEdit(Form)
        self.TextEdit1.setGeometry(10, 450, 600, 75)
        self.TextEdit1.setObjectName('plainTextEdit1')
        self.TextEdit1.setReadOnly(True)

        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(10, 390, 110, 100))

        self.TextEdit2 = QtWidgets.QPlainTextEdit(Form)
        self.TextEdit2.setGeometry(10, 550, 600, 73)
        self.TextEdit2.setObjectName('plainTextEdit2')
        self.TextEdit2.setReadOnly(True)

        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(10, 490, 110, 100)

        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(530, 100, 250, 100))
        self.label_16.setWordWrap(True)
        self.label_16.setOpenExternalLinks(True)

        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(550, 230, 90, 40))
        self.pushButton_6.setObjectName('pushbutton_6')
        
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(10, 700, 350, 15))
        self.label_17.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)

        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setGeometry(QtCore.QRect(10, 720, 270, 15))
        self.label_18.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)

        self.label_19 = QtWidgets.QLabel(Form)
        self.label_19.setGeometry(QtCore.QRect(10, 735, 280, 15))
        self.label_19.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        
        self.label_20 = QtWidgets.QLabel(Form)
        self.label_20.setGeometry(QtCore.QRect(10, 745, 270, 15))
        self.label_20.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)

        self.process1 = QtCore.QProcess(Form)
        self.process1.readyRead.connect(self.minerOutput1)

        self.process2 = QtCore.QProcess(Form)
        self.process2.readyRead.connect(self.minerOutput2)

        self.pushButton.clicked.connect(self.cmd2)
        self.pushButton.clicked.connect(self.stop_pool)
        self.pushButton_2.clicked.connect(self.cmd)
        self.pushButton_2.clicked.connect(self.stop_solo)
        self.pushButton_3.clicked.connect(self.save_config)
        self.pushButton_6.clicked.connect(self.process1.kill)
        self.pushButton_6.clicked.connect(self.process2.kill)
        self.pushButton_6.clicked.connect(self.stop_and_quit)
        self.pushButton_2.setFont(QtGui.QFont("Nirmala UI", 8))
        self.pushButton_3.setFont(QtGui.QFont("Nirmala UI", 8))
        self.pushButton_6.setFont(QtGui.QFont("Nirmala UI", 8))
        self.pushButton.setFont(QtGui.QFont("Nirmala UI", 8))

        self.combobox.setFont(QtGui.QFont("Nirmala UI", 8))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def start_pool(self):
        self.pushButton.setText('Start Pool')
        self.pushButton.clicked.connect(self.cmd2)
        self.pushButton.clicked.connect(self.stop_pool)

    def stop_pool(self):
        self.pushButton.setText('Stop Pool')
        self.pushButton.clicked.disconnect()
        self.pushButton.clicked.connect(self.process2.kill)
        self.pushButton.clicked.connect(self.start_pool)

    def start_solo(self):
        self.pushButton_2.setText('Start Solo')
        self.pushButton_2.clicked.connect(self.cmd)
        self.pushButton_2.clicked.connect(self.stop_solo)

    def stop_solo(self):
        self.pushButton_2.setText('Stop Solo')
        self.pushButton_2.clicked.disconnect()
        self.pushButton_2.clicked.connect(self.process1.kill)
        self.pushButton_2.clicked.connect(self.start_solo)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "CPU GUI Miner"))
        self.label_3.setText(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Nirmala UI\'; font-size:7.7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Welcome to the CPU GUI miner. </span><span style=\" font-weight:600; font-style:italic; color:#ff0000;\">Warning: This miner is only for coins that use CPU mining algorithms. This will not work with GPU algorithms.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; text-decoration: underline;\">Pool Mining: </span>Enter the pool url, followed by the required port, your coin address, password(optional), cpu threads and the hashing algorithm. Then click \'Start Pool!\'                                                                                                                                <span style=\" font-weight:600; text-decoration: underline;\">Solo Mining:</span><span style=\" font-weight:600;\"> </span>To start, make sure you have set your wallet configuration properly according to the coins configuration. Then enter \'http://127.0.0.1:(coin's rpc port)\' into the URL box, followed by your coins address, rpcuser, rpcpassword, the amount of cpu threads and the required algorithm. Then click \'Start Solo!\'<br /></p></body></html>"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:7.5pt\">Solo/Pool URL:</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:7.5pt\">Coin Address:</span></p></body></html>"))
        self.label_9.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:7.5pt\">rpcuser (only for solo miners):</span></p></body></html>"))
        self.label_10.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:7.5pt\">rpcpassword or Pool password:</span></p></body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><a href=\"https://x.com/CryptoLover705\"><span style=\" text-decoration: underline; color:#0000ff;\">Twitter</span></a></p></body></html>"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p><a href=\"https://github.com/CryptoDevelopmentServices/GUI-CPU-Miner\"><span style=\" text-decoration: underline; color:#0000ff;\">Github</span></a></p></body></html>"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p><span style=\" font-style:italic; font-size:7.5pt\">\'...One-CPU-One-Vote...' - Satoshi Nakamoto </span></p></body></html>"))
        self.pushButton_2.setText(_translate("Form", "Start Solo!"))
        self.pushButton_3.setText(_translate('Form', 'Save config'))
        self.label_11.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:7.5pt\">CPU Cores:</span></p></body></html>"))
        self.label_12.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:7.5pt\">(According to actual cpu thread count)</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Start Pool!"))
        self.pushButton_6.setText(_translate("Form", "Stop Miners \nand Exit"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "Pool password optional"))
        self.label_13.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:7.5pt\">Algoritm:</span></p></body></html>"))
        self.label_14.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:7.5pt\">Solo Miner output:</span></p></body></html>"))
        self.label_15.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:7.5pt\">Pool Miner output:</span></p></body></html>"))
        self.label_16.setText(_translate("Form", "<html><head/><body><p><span style=\" font-style:italic; color:#808080; font-size:7.5pt\">Special thanks to <a href=\"https://github.com/RickillerZ/cpuminer-RKZ\"><span style=\" text-decoration: underline; color:#4D4E4F;\">Rick~z </a>and <a href=\"https://github.com/itwysgsl\"><span style=\" text-decoration: underline; color:#4D4E4F;\">iamstenman</span></a> for contributing to this project</p></body></html>"))
        self.label_17.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:800; font-size:7.5pt\">If you like this miner, please star on github and feel free to donate:</span></p></body></html>"))
        self.label_18.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:7.5pt\">LTC: LazJ61h4mJCHsZkiBvZNXEuEoziZzsAEMJ</span></p></body></html>"))
        self.label_19.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:7.5pt\">POL: 0xc0B254f1e80517Ea4D298a88AB9371dEec62792C</span></p></body></html>"))
        self.label_20.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:7.5pt\">ADVC: AK7WMs3B2u32rmdAGnKAmeJHbbrmEvbb1E</span></p></body></html>"))


    def cmd(self):
        self.TextEdit1.clear()
        self.process1.start(path + './cpuminer -a ' + self.combobox.currentText() +' -o ' + self.lineEdit.text() +' --no-longpoll -u ' + self.lineEdit_3.text() + ' -p ' + self.lineEdit_4.text() + ' --coinbase-addr=' + self.lineEdit_2.text() + ' -t' + self.lineEdit_5.text() + '--api-bind=127.0.0.1:4048')

    def cmd2(self):
        self.TextEdit2.clear()
        self.process2.start(path + './cpuminer -a ' + self.combobox.currentText() + ' -o ' + self.lineEdit.text() + ' --no-longpoll -u ' + self.lineEdit_2.text() + ' -p' + self.lineEdit_4.text() + ' -t' + self.lineEdit_5.text() + ' --api-bind=127.0.0.1:4049')

    def minerOutput1(self):
        read1 = str(self.process1.readAll())
        output1 = read1.replace('b"', '').replace("b'[", '[').replace('\\', '').replace('x1b[', '').replace('x1b[0m"', '').replace("rn'", '').replace("rn", '').replace('0m', '   ').replace('36m', '     ').replace('31m', '    ').replace('01;37m', '    ').replace('32m', '    ').replace(' "', '').replace("'power2b'", 'power2b').replace('n"', '').replace('n[', '[').replace("n'", ' ').replace(' net', '  net').replace(' n ', '').replace('.n', ' ').replace("b'n", ' ').replace('nnnnn', ' ').replace('Forkn', 'Fork').replace('sn', 's').replace('zS', 'z S').replace('Zn', 'Z ').replace('nS', ' S').replace('nnC', ' C')
        self.TextEdit1.appendHtml(output1)

    def minerOutput2(self):
        read2 = str(self.process2.readAll())
        output2 = read2.replace('b"', '').replace("b'[", '[').replace('\\', '').replace('x1b[', '').replace('x1b[0m"', '').replace("rn'", '').replace("rn", '').replace('0m', '    ').replace('36m', '    ').replace('31m', '    ').replace('01;37m', '    ').replace('32m', '    ').replace(' "', '').replace("'power2b'", 'power2b').replace('n"', '').replace('n[', '[').replace("n'", ' ').replace(' net', '  net').replace(' n ', '').replace('.n', ' ').replace("b'n", ' ').replace('nnnnn', ' ').replace('Forkn', 'Fork').replace('sn', 's').replace('zS', 'z S').replace('Zn', 'Z ').replace('nS', ' S').replace('nnC', ' C')
        self.TextEdit2.appendHtml(output2)

    def stop_and_quit(self):
        sys.exit()

    def save_config(self):

        config = {
            'address': str(self.lineEdit_2.text()),
            'URL': str(self.lineEdit.text()),
            'username': str(self.lineEdit_3.text()),
            'password': str(self.lineEdit_4.text()),
            'threads': str(self.lineEdit_5.text()),
            'algorithm': str(self.combobox.currentText())
        }

        with open('minerconfig.json', 'w') as f:
            f.write(json.dumps(config))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
    
