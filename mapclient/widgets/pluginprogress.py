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
import os, zipfile, requests
from PySide import QtGui, QtCore

from mapclient.widgets.ui_pluginprogress import Ui_DownloadProgress

class PluginProgress(QtGui.QDialog):
    '''
    Displays download and extraction progress of plugins from GitHub repository.
    '''
    
    def __init__(self, plugins, directory, parent=None):
        '''
        Constructor
        '''
        QtGui.QDialog.__init__(self, parent)
        self._ui = Ui_DownloadProgress()
        self._ui.setupUi(self)
        self._makeConnections()
        
        self._directory = directory
        self._plugins = plugins
        self._fileNames = {}
        self._totalBytes = 0
        self._download_strings = ['Downloading %d of %d plugins...', 'Extracting %d of %d plugins...']
        self._ui.progressBar.setMaximum(len(plugins)*50)
        
    def _makeConnections(self):
        self._ui.cancelDownload.clicked.connect(self.downloadCancelled)
        
    def downloadCancelled(self):
        for file in self._fileNames:
            if os.path.exists(file):           
                os.remove(file)
        self.close()

    def run(self):
        downloaded = 0
        url_no = 1
        for plugin in self._plugins.keys():
            self._ui.label.setText(self._download_strings[0] %(url_no, len(self._plugins)))
            self._fileNames[plugin] = plugin.lower().split(' ')
            file = ''
            for part in self._fileNames[plugin]:
                file = file + part
            self._fileNames[plugin] = file
            
            rq = requests.get(self._plugins[plugin]['location'])
            if not rq.ok:
                ret = QtGui.QMessageBox.critical(self, 'Error', '\n There was a problem downloading the following plugin:  ' + plugin + '\n\n Please check your internet connection.\t', QMessageBox.Ok)            
                
            self._totalBytes += int(rq.headers['content-length'])
            with open(os.path.join(self._directory, self._fileNames[plugin] + '.zip'), "wb") as zFile:
                for chunk in rq.iter_content(1):
                    zFile.write(chunk)
                    downloaded += len(chunk)
                    progress = downloaded / self._totalBytes
                    self._ui.progressBar.setValue(int(progress * url_no*40))
            url_no += 1
        
        file_no = 1
        for plugin in self._plugins:
            self._ui.label.setText(self._download_strings[1] %(file_no, len(self._plugins)))
            zfobj = zipfile.ZipFile(os.path.join(self._directory, self._fileNames[plugin] + '.zip'), 'r')
            zfobj.extractall(self._directory)
            self._ui.progressBar.setValue(self._ui.progressBar.value() + 5)
            zfobj.close()
            os.remove(os.path.join(self._directory, self._fileNames[plugin] + '.zip'))
            self._ui.progressBar.setValue(self._ui.progressBar.value() + 5)
            file_no += 1
        self.close()
