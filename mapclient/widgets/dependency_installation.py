'''
MAP Client, a program to generate detailed musculoskeletal models for OpenSim.
    Copyright (C) 2012  University of Auckland
    
This file is part of MAP Client. (http://launchpad.net/mapclient)

    MAP Client is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    MAP Client is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with MAP Client.  If not, see <http://www.gnu.org/licenses/>..
'''

import sys, os, time, subprocess, random
from PySide import QtGui
from PySide.QtCore import QThread, QObject, Signal

from mapclient.widgets.pluginprogress import PluginProgress
from mapclient.widgets.ui_pluginprogress import Ui_DownloadProgress
from mapclient.core.utils import convertExceptionToMessage

class MySignal(QObject):
        sig = Signal(str)

class Thread(QThread):
    
    def __init__(self, env_dir, parent=None):
        QThread.__init__(self, parent)
        self.signal = MySignal()
        self.env_dir = env_dir

    def run(self):
        try:
            subprocess.check_call(['virtualenv', '--clear', '--system-site-packages', self.env_dir])
            sys.path.append(os.path.join(self.env_dir, 'Lib', 'site-packages'))
        except Exception as e:
            message = convertExceptionToMessage(e)
            self.signal.sig.emit(message)
                
class VESetup(PluginProgress):
    
    def __init__(self, env_dir, parent=None):
        '''
        Constructor
        '''
        QtGui.QDialog.__init__(self, parent)
        self._ui = Ui_DownloadProgress()
        self._ui.setupUi(self)
        self.setWindowTitle('Virtual Environment')
        self._ui.cancelDownload.setText('Ok')
        self._ui.progressBar.setValue(0)
        self._ui.progressBar.setMaximum(100)
        self.thread = Thread(env_dir)
        self._makeConnections()
        
    def run(self):
        self.thread.start()
        self.animateProgress()
        self.validationStep()
        
    def animateProgress(self):
        self.started()
        damping = 1
        while self.thread.isRunning() and (self._ui.progressBar.value() < self._ui.progressBar.maximum()):
            time.sleep((random.randrange(0, 250)/1000)*damping)
            self._ui.progressBar.setValue(self._ui.progressBar.value() + 1.5)
            damping += 0.05
        self.finished()

    def validationStep(self):
        while self._ui.progressBar.value() < self._ui.progressBar.maximum():
            time.sleep(0.01)
            self._ui.progressBar.setValue(self._ui.progressBar.value() + 1)
        self.complete()
        
    def _makeConnections(self):
        self.thread.terminated.connect(self.closeDialog)
        self.thread.signal.sig.connect(self.error)
        self._ui.cancelDownload.clicked.connect(self.closeDialog)
        
    def error(self, data):
        self.close()
        QtGui.QMessageBox.warning(self, 'Setup Failed', 'A problem occurred while setting up the virtual environment: \n\n' + data, QtGui.QMessageBox.Ok)
            
    def started(self):
        self._ui.label.setText('Setting up Virtual Environment. Please wait...')
        self._ui.cancelDownload.setEnabled(False)
        
    def finished(self):
        self._ui.label.setText('Validating successful Virtual Environment setup...')
        
    def complete(self):
        self._ui.label.setText('Virtual Environment setup successful.')
        self._ui.cancelDownload.setEnabled(True)
    
    def closeDialog(self):
        self.close()