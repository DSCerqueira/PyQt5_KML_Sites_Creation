import sys, os
import sqlite3
import pandas as pd
import numpy as np
from PyQt5 import QtWebEngineWidgets as pqw
from PyQt5.QtCore import QDir, QUrl
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from googleMaps import Ui_MainWindow
import kml2geojson
import geojsonio as gs
import math as mt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

##########################################################################
con = sqlite3.connect('database/tablesites.db')
cur = con.cursor()
pathl = sys.path
try:
    cur.execute('DROP TABLE sites')
    sqlquery = 'CREATE TABLE sites (STID INTEGER PRIMARY KEY AUTOINCREMENT,AGREGATION,SITE,LAT,LON,PAR01,PAR02, PAR03,PAR04,PAR05)'
    cur.execute(sqlquery)
except:
    sqlquery = 'CREATE TABLE sites (STID INTEGER PRIMARY KEY AUTOINCREMENT,AGREGATION,SITE,LAT,LON,PAR01,PAR02, PAR03,PAR04,PAR05)'
    cur.execute(sqlquery)
try:
    cur.execute('DROP TABLE sectors')
    sqlquery = 'CREATE TABLE sectors (SECID INTEGER PRIMARY KEY AUTOINCREMENT,AGREGATION,STATE,SITE,SECTOR,HEIGHT,AZIMUTH,MEC_TILT,ELE_TILT,BEAMWIDTH_H,BEAMWIDTH_V,LAT,LON,ALTITUDE,PAR01,PAR02,PAR03,PAR04,PAR05 )'
    cur.execute(sqlquery)
except:
    sqlquery = 'CREATE TABLE sectors (SECID INTEGER PRIMARY KEY AUTOINCREMENT,AGREGATION,STATE,SITE,SECTOR,HEIGHT,AZIMUTH,MEC_TILT,ELE_TILT,BEAMWIDTH_H,BEAMWIDTH_V,LAT,LON,ALTITUDE,PAR01,PAR02,PAR03,PAR04,PAR05)'
    cur.execute(sqlquery)


#############################################################################
class gwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(gwindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #############################################################################
        self.view = pqw.QWebEngineView()
        layout = self.ui.mapsout
        layout.addWidget(self.view)
        # self.view.load(QUrl('http://geojson.io/#map=2/20.1/0.0'))
        self.view.load(QUrl('http://geojson.io/#map=2/20.1/0.0'))
        self.view.show()
        #####################chart area#############################################
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        layout = self.ui.chartout
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        ############################################################################
        cur.execute('select * from sites')
        self.coltable = cur.description
        self.ui.basetable.setColumnCount(len(self.coltable))
        self.ncol = []
        for i in self.coltable:
            self.ncol.append(i[0])
        self.ui.basetable.setHorizontalHeaderLabels(list(self.ncol))
        #####################CLICK BUTTONS##########################################################
        self.ui.texpbt.clicked.connect(self.exporttemp)
        self.ui.importbt.clicked.connect(self.importtablesites)
        self.ui.importsectorbt.clicked.connect(self.importtablesectors)

        self.ui.runquery.clicked.connect(self.runqueryfunc)
        self.ui.colorbt.clicked.connect(self.colorpick)
        self.ui.setparbt.clicked.connect(self.setpar)
        self.ui.clearbt.clicked.connect(self.cleartb)
        self.ui.alltbbt.clicked.connect(self.allsites)
        self.ui.alltbsecbt.clicked.connect(self.allsectors)
        self.ui.refreshbt.clicked.connect(self.refreshmap)
        self.ui.rungmap.clicked.connect(self.loadkml)
        self.ui.kmlbtsec.clicked.connect(self.kmlsectors)
        if self.ui.kmlbtsec.clicked:
            self.valsite = 'bola'
        self.ui.kmlbt.clicked.connect(self.kmlsectors)
        if self.ui.kmlbt.clicked:
            self.valsite = 'clickedsite'
        self.ui.setgr.clicked.connect(self.group)
        self.ui.chartbt.clicked.connect(self.chart)

    #####################functions########################
    def exporttemp(self):
        self.data = pd.DataFrame(columns=(
        'AGREGATION', 'STATE', 'SITE', 'SECTOR', 'HEIGHT', 'AZIMUTH', 'MEC_TILT', 'ELE_TILT', 'BEAMWIDTH_H',
        'BEAMWIDTH_V', 'LAT', 'LON', 'ALTITUDE', 'PAR01', 'PAR02', 'PAR03', 'PAR04', 'PAR05'))
        self.pathfile = pathl[0] + '/database/temporary/gtemplate_sector.csv'
        self.data.to_csv(self.pathfile, index=False)
        openfile = '"' + self.pathfile + '"'
        os.system(openfile)
        self.data = pd.DataFrame(
            columns=('AGREGATION', 'SITE', 'LAT', 'LON', 'PAR01', 'PAR02', 'PAR03', 'PAR04', 'PAR05'))
        self.pathfile = pathl[0] + '/database/temporary/gtemplate_site.csv'
        self.data.to_csv(self.pathfile, index=False)
        openfile = '"' + self.pathfile + '"'
        os.system(openfile)

    def importtablesites(self):

        try:
            try:
                cur.execute('DROP TABLE sites')
            except:
                pass
            fname = QFileDialog()
            fname.setFileMode(QFileDialog.AnyFile)
            fname.setNameFilter('CSV files (*.csv)')
            if fname.exec_():
                self.fname = fname.selectedFiles()
                self.dataframe = pd.read_csv(self.fname[0])
                self.dataframe = pd.DataFrame(self.dataframe)
            dima = np.shape(self.dataframe)
            self.ui.basetable.setRowCount(dima[0])
            self.ui.basetable.setColumnCount(dima[1])
            self.ui.basetable.setHorizontalHeaderLabels(self.dataframe.columns)

            #######creating database table sites####
            strqueryend = '(STID INTEGER PRIMARY KEY AUTOINCREMENT,'
            strquery = '('
            for i in list(self.dataframe.columns):
                strqueryend = strqueryend + i + ','
                strquery = strquery + i + ','
            strqueryend = strqueryend + 'SELECTOR,COLOR)'
            strquery = strquery + 'SELECTOR,COLOR)'
            sqlqueryend = 'CREATE TABLE sites ' + strqueryend
            cur.execute(sqlqueryend)
            row = 0
            sqlcoluna = ''
            for i in range(dima[0]):
                col = 0
                sqlrow = '('
                for n in list(self.dataframe.loc[i]):
                    cellinfo = QtWidgets.QTableWidgetItem(str(n))
                    self.ui.basetable.setItem(row, col, cellinfo)
                    sqlrow = sqlrow + '"' + str(n) + '",'
                    col = col + 1
                sqlrow = sqlrow + '"","")'

                if i < int(dima[0] - 1):
                    sqlcoluna = sqlcoluna + sqlrow + ','

                if i == int(dima[0] - 1):
                    sqlcoluna = sqlcoluna + sqlrow + ';'

                row += 1
            #####insertin data into the table sites######
            sqlquery = 'INSERT INTO sites ' + strquery + ' VALUES' + sqlcoluna
            cur.execute(sqlquery)
            con.commit()
            try:
                cur.execute('DROP TABLE sitestemp')
                sqlquery = 'CREATE TABLE sitestemp AS SELECT * FROM sites;'
                cur.execute(sqlquery)
            except:
                sqlquery = 'CREATE TABLE sitestemp AS SELECT * FROM sites;'
                cur.execute(sqlquery)
        except:
            pass

    def importtablesectors(self):

        try:
            cur.execute('DROP TABLE sectors')
            fname = QFileDialog()
            fname.setFileMode(QFileDialog.AnyFile)
            fname.setNameFilter('CSV files (*.csv)')
            if fname.exec_():
                self.fname = fname.selectedFiles()
                self.dataframe = pd.read_csv(self.fname[0])
                self.dataframe = pd.DataFrame(self.dataframe)
            dima = np.shape(self.dataframe)
            self.ui.basetable.setRowCount(dima[0])
            self.ui.basetable.setColumnCount(dima[1])
            self.ui.basetable.setHorizontalHeaderLabels(self.dataframe.columns)

            #######creating database table sites####
            strqueryend = '(SECID INTEGER PRIMARY KEY AUTOINCREMENT,'
            strquery = '('
            for i in list(self.dataframe.columns):
                strqueryend = strqueryend + i + ','
                strquery = strquery + i + ','
            strqueryend = strqueryend + 'SELECTOR,COLOR)'
            strquery = strquery + 'SELECTOR,COLOR)'
            sqlqueryend = 'CREATE TABLE sectors ' + strqueryend
            cur.execute(sqlqueryend)
            row = 0
            sqlcoluna = ''
            for i in range(dima[0]):
                col = 0
                sqlrow = '('
                for n in list(self.dataframe.loc[i]):
                    cellinfo = QtWidgets.QTableWidgetItem(str(n))
                    self.ui.basetable.setItem(row, col, cellinfo)
                    sqlrow = sqlrow + '"' + str(n) + '",'
                    col = col + 1
                sqlrow = sqlrow + '"","")'

                if i < int(dima[0] - 1):
                    sqlcoluna = sqlcoluna + sqlrow + ','

                if i == int(dima[0] - 1):
                    sqlcoluna = sqlcoluna + sqlrow + ';'

                row += 1
            #####insertin data into the table sites######
            sqlquery = 'INSERT INTO sectors ' + strquery + ' VALUES' + sqlcoluna
            cur.execute(sqlquery)
            con.commit()
            try:
                cur.execute('DROP TABLE sectorstemp')
                sqlquery = 'CREATE TABLE sectorstemp AS SELECT * FROM sectors;'
                cur.execute(sqlquery)
            except:
                sqlquery = 'CREATE TABLE sectorstemp AS SELECT * FROM sectors;'
                cur.execute(sqlquery)
        except:
            pass

    def runqueryfunc(self):
        try:
            sqlquery = self.ui.rquerytext.toPlainText()
            cur.execute(sqlquery)
            self.tbdtb = cur.fetchall()
            self.ui.tbout.setRowCount(len(self.tbdtb))
            self.ui.tbout.setColumnCount(len(self.tbdtb[0]))
            row = 0
            for i in self.tbdtb:
                col = 0
                for n in i:
                    cellinfo = QtWidgets.QTableWidgetItem(str(n))
                    self.ui.tbout.setItem(row, col, cellinfo)
                    col = col + 1
                row += 1
            coltable = cur.description
            ncol = []
            for i in coltable:
                ncol.append(i[0])
            self.ui.tbout.setHorizontalHeaderLabels(list(ncol))

        except:
            pass

    def allsites(self):
        try:
            sqlquery = 'SELECT * FROM sitestemp'
            cur.execute(sqlquery)
            self.tbdtb = cur.fetchall()
            self.ui.tbout.setRowCount(len(self.tbdtb))
            self.ui.tbout.setColumnCount(len(self.tbdtb[0]))
            row = 0
            for i in self.tbdtb:
                col = 0
                for n in i:
                    cellinfo = QtWidgets.QTableWidgetItem(str(n))
                    self.ui.tbout.setItem(row, col, cellinfo)
                    col = col + 1
                row += 1
            coltable = cur.description
            ncol = []
            for i in coltable:
                ncol.append(i[0])
            self.ui.tbout.setHorizontalHeaderLabels(list(ncol))

        except:
            pass

    def allsectors(self):
        try:
            sqlquery = 'SELECT * FROM sectorstemp'
            cur.execute(sqlquery)
            self.tbdtb = cur.fetchall()
            self.ui.tbout.setRowCount(len(self.tbdtb))
            self.ui.tbout.setColumnCount(len(self.tbdtb[0]))
            row = 0
            for i in self.tbdtb:
                col = 0
                for n in i:
                    cellinfo = QtWidgets.QTableWidgetItem(str(n))
                    self.ui.tbout.setItem(row, col, cellinfo)
                    col = col + 1
                row += 1
            coltable = cur.description
            ncol = []
            for i in coltable:
                ncol.append(i[0])
            self.ui.tbout.setHorizontalHeaderLabels(list(ncol))

        except:
            pass

    def colorpick(self):
        try:
            items = ('sites', 'sectors')
            self.seltable = QInputDialog.getItem(self, 'Select Table', 'Select Table to set color', items, 0, False)
            self.table = self.seltable[0] + 'temp'
            query = 'UPDATE ' + self.table + ' SET COLOR='
            color = QtWidgets.QColorDialog.getColor()
            framecolor = pd.DataFrame(self.tbdtb)
            setcolor = '('
            for i in list(framecolor[0]):
                setcolor = setcolor + str(i) + ','
            setcolor = setcolor + '"")'
            if self.seltable[0] == 'sites':
                sqlquery = query + '"' + color.name() + '"' + ' WHERE STID IN ' + setcolor
            elif self.seltable[0] == 'sectors':
                sqlquery = query + '"' + color.name() + '"' + ' WHERE SECID IN ' + setcolor
            cur.execute(sqlquery)
            con.commit()
        except:
            pass

    def setpar(self):
        try:
            items = ('sites', 'sectors')
            self.seltable = QInputDialog.getItem(self, 'Select Table', 'Select Table to set color', items, 0, False)
            self.table = self.seltable[0] + 'temp'
            query = 'UPDATE ' + self.table + ' SET SELECTOR= "selected"'
            framepr = pd.DataFrame(self.tbdtb)
            setcpar = '('
            for i in list(framepr[0]):
                setcpar = setcpar + str(i) + ','
            setcpar = setcpar + '"")'
            if self.seltable[0] == 'sites':
                sqlquery = query + ' WHERE STID IN ' + setcpar + ';'
            elif self.seltable[0] == 'sectors':
                sqlquery = query + ' WHERE SECID IN ' + setcpar + ';'
            cur.execute(sqlquery)
            con.commit()
        except:
            pass

    def cleartb(self):
        try:
            cur.execute('DROP TABLE sitestemp')
            sqlquery = 'CREATE TABLE sitestemp AS SELECT * FROM sites;'
            cur.execute(sqlquery)
            cur.execute('DROP TABLE sectorstemp')
            sqlquery = 'CREATE TABLE sectorstemp AS SELECT * FROM sectors;'
            cur.execute(sqlquery)
            self.ui.tbout.clear()
        except:
            pass

    def refreshmap(self):
        self.view.load(QUrl('http://geojson.io/#map=2/20.1/0.0'))
        self.view.show()

    def loadkml(self):
        #try:
            self.mesg = QMessageBox.information(self, 'Select KML file', 'Select KML file to open in Geojson MAPs.')
            fname = QFileDialog()
            fname.setFileMode(QFileDialog.AnyFile)
            fname.setNameFilter('KML files (*.kml)')
            print('casa')
            if fname.exec_():
                self.fnamepath = fname.selectedFiles()
            self.pathfile = pathl[0] + '/database/temporary/json_files'
            print(self.pathfile)
            print(self.fnamepath[0])
            kml2geojson.main.convert(self.fnamepath[0], self.pathfile)
            mapname = self.fnamepath[0]
            mapname = mapname.split('/')
            mapname = mapname[-1].split('.')
            mapname = mapname[0] + '.geojson'
            self.mappath = self.pathfile + '/' + mapname
            self.mappath = self.mappath.replace(os.sep, '/')
            self.maptemplate = open(self.mappath).read()
            self.view.close()
            gs.display(self.maptemplate, force_gist=True)
            self.view.load(QUrl(gs.display(self.maptemplate)))
            self.view.show()
        #except:
            pass

    def kmlsectors(self):
        limiter = 0
        try:
            sqlquery = 'SELECT * FROM sitestemp'
            cur.execute(sqlquery)
            self.tablesites = pd.DataFrame(cur.fetchall())
            self.tablesites.sort_values(by=[1, 2], inplace=True)
            aux = list(cur.description)
            fields = []
            for i in aux:
                fields.append(i[0])

            try:
                sqlquery = 'SELECT * FROM sectorstemp'
                cur.execute(sqlquery)
                self.tablesectors = pd.DataFrame(cur.fetchall())
                self.tablesectors.sort_values(by=[1, 3, 4], inplace=True)
                self.agregation = list(self.tablesites[1].unique())
                aux = list(cur.description)
                fieldsect = []
                for i in aux:
                    fieldsect.append(i[0])
            except:
                self.agregation = list(self.tablesites[1].unique())
                pass

            ############creating agregation style#############

            self.kmltext = open('database/temporary/KML_Google_Sites.txt', 'w')
            self.kmltext.writelines(['<?xml version="1.0" encoding="UTF-8"?>\n',
                                     '<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" \n',
                                     'xmlns:atom="http://www.w3.org/2005/Atom" >\n'])
            self.kmltext.close()
            self.kmltext = open('database/temporary/KML_Google_Sites.txt', 'a')
            self.kmltext.writelines(['<Document>\n',
                                     '\t<name>KML_File_Sectors</name>\n'])
            listcolor = ['FF0000FF', 'FFB469FF', 'FFB469FF', 'FF9314FF', 'FF9314FF', 'FF00FF00', 'FF00FF00', 'FF00FF7F',
                         'FF00FF7F', 'FF9AFA00', 'FF9AFA00', 'FF2FFFAD', 'FF2FFFAD', 'FF32CD32', 'FF32CD32', 'FF32CD9A',
                         'FF32CD9A', 'FF228B22', 'FF228B22', 'FFFF7084', 'FFFF7084', 'FFCD0000', 'FFCD0000', 'FFE16941',
                         'FFE16941', 'FFFF0000', 'FFFF0000', 'FF00FFFF', 'FF00FFFF', 'FF00D7FF', 'FF00D7FF', 'FF82DDEE',
                         'FF82DDEE', 'FF20A5DA', 'FF20A5DA', 'FF0B86B8', 'FF0B86B8', 'FF8B7B6C', 'FF8B7B6C', 'FFFFF500',
                         'FFFFF500', 'FF3333CD', 'FF3333CD', 'FF23238B', 'FF23238B', 'FF698CFF', 'FF698CFF', 'FF8B008B',
                         'FF8B008B', 'FF00008B', 'FF00008B', 'FF90EE90', 'FF90EE90', 'FF1D66CD', 'FF1D66CD', 'FF86838B',
                         'FF86838B', 'FFD2D5EE', 'FFD2D5EE', 'FFB5B7CD', 'FFB5B7CD', 'FFED9564', 'FFED9564', 'FFE1E4FF',
                         'FFE1E4FF', 'FFFFFFFF', 'FFFFFFFF', 'FF000000', 'FF000000', 'FF4F4F2F', 'FF4F4F2F', 'FF696969',
                         'FF696969', 'FF394FCD', 'FF394FCD', 'FF26368B', 'FF26368B', 'FF0045FF', 'FF0045FF']
            ncolor = -1

            for i in self.agregation:
                ncolor = ncolor + 1
                self.kmltext.writelines(['\t<Style id="' + i + '">\n',
                                         '\t\t<IconStyle>\n',
                                         '\t\t\t<color>' + listcolor[ncolor] + '</color>\n',
                                         '\t\t\t<scale>0.5</scale>\n',
                                         '\t\t\t<Icon>\n',
                                         '\t\t\t\t<href>http://maps.google.com/mapfiles/kml/shapes/shaded_dot.png</href>\n',
                                         '\t\t\t</Icon>\n',
                                         '\t\t</IconStyle>\n',
                                         '\t</Style>\n'])
            ########################creating folder agregation-sites#############################

            for n in range(len(self.agregation)):
                self.kmltext.writelines(['\t<Folder>\n', '\t\t<name>' + self.agregation[n] + '</name>\n'])

                for i in range(self.tablesites.shape[0]):

                    if self.tablesites[1][i] == self.agregation[n]:

                        auxcolor = self.tablesites[self.tablesites.shape[1] - 1][i]
                        if auxcolor != '':
                            color = 'FF' + auxcolor[5] + auxcolor[6] + auxcolor[3] + auxcolor[4] + auxcolor[1] + \
                                    auxcolor[2]
                        elif auxcolor == '':
                            color = 'ffffffff'
                        selected = self.tablesites[self.tablesites.shape[1] - 2][i]
                        site = self.tablesites[2][i]
                        lat = float(self.tablesites[3][i])
                        long = float(self.tablesites[4][i])
                        altitude = 0
                        terminator = 0
                        contador = 0
                        aux2 = 0

                        if self.valsite != 'clickedsite':
                            for isc in range(self.tablesectors.shape[0]):
                                terminator = terminator + 1
                                if self.tablesectors[3][isc] == site:
                                    count = 'start'
                                    contador = terminator
                                    aux = float(self.tablesectors[5][isc] * 1) + float(self.tablesectors[13][isc] * 1)
                                    if aux2 > aux:
                                        aux = aux2
                                    if aux * 1 > altitude:
                                        altitude = aux
                                elif count == 'start' and terminator > contador and contador > 0:
                                    aux2 = float(self.tablesectors[5][isc] * 1) + float(self.tablesectors[13][isc] * 1)
                                    break
                                else:
                                    pass
                        else:
                            pass

                        self.kmltext.writelines(['\t\t<Style id="corsite">\n', '\t\t\t<IconStyle>\n',
                                                 '\t\t\t\t<color>' + color + '</color>\n',
                                                 '\t\t\t\t<scale>0.5</scale>\n',
                                                 '\t\t\t\t<Icon>\n',
                                                 '\t\t\t\t\t<href>http://maps.google.com/mapfiles/kml/shapes/shaded_dot.png</href>\n',
                                                 '\t\t\t\t</Icon>\n', '\t\t\t</IconStyle>\n', '\t\t</Style>\n'])
                        self.kmltext.writelines(
                            ['\t\t<Folder>\n', '\t\t\t<name>' + site + '</name>\n', '\t\t\t<Placemark>\n',
                             '\t\t\t\t<name>' + site + '</name>\n'])

                        ###############starting site description##################
                        self.kmltext.writelines(
                            ['\t\t\t\t\t<description><![CDATA[<table border="1" padding="0"></tr><td>'])

                        for l in range(5, self.tablesites.shape[1] - 2):
                            paramsites = self.tablesites[l][i]
                            self.kmltext.writelines('<tr><td>' + fields[l] + '=' + paramsites + '</tr><td>')
                        self.kmltext.writelines([']]></description>\n', '\t\t\t\t<styleUrl>#corsite</styleUrl>\n'])
                        self.kmltext.writelines(['\t\t\t\t<Point>\n', '\t\t\t\t\t<extrude>1</extrude>\n',
                                                 '\t\t\t\t\t<altitudeMode>absolute</altitudeMode>\n',
                                                 '\t\t\t\t\t<coordinates>' + str(long) + ',' + str(lat) + ',' + str(
                                                     altitude) + '</coordinates>\n', '\t\t\t\t</Point>\n',
                                                 '\t\t\t</Placemark>\n'])

                        ###################starting sector creation##################################

                        if self.valsite != 'clickedsite':
                            counter = 0
                            terminator = 0
                            for isc in range(limiter, self.tablesectors.shape[0]):

                                if site == self.tablesectors[3][isc]:
                                    counter = terminator
                                    limiter = limiter + 1
                                    auxcolorsec = self.tablesectors[self.tablesectors.shape[1] - 1][isc]
                                    if auxcolorsec != '':
                                        colorsec = "80" + auxcolorsec[5] + auxcolorsec[6] + auxcolorsec[3] + \
                                                   auxcolorsec[4] + auxcolorsec[1] + auxcolorsec[2]
                                    elif auxcolorsec == '':
                                        colorsec = '28FFFFFF'
                                    selectedsec = self.tablesectors[self.tablesectors.shape[1] - 2][isc]
                                    sector = self.tablesectors[4][isc]
                                    height = float(self.tablesectors[5][isc] * 1) + float(
                                        self.tablesectors[13][isc] * 1)
                                    azimuth = float(self.tablesectors[6][isc] * 1)
                                    tilt = float(self.tablesectors[7][isc] * 1) + float(self.tablesectors[8][isc] * 1)
                                    bandvert = float(self.tablesectors[10][isc] * 1)
                                    bandhor = float(self.tablesectors[9][isc] * 1)
                                    altitude = float(self.tablesectors[13][isc] * 1)

                                    self.kmltext.writelines(['\t\t\t<Placemark>\n'])
                                    self.kmltext.writelines(
                                        ['\t\t\t\t<description><![CDATA[<table border="1" padding="0"></tr><td>',
                                         '<tr><td>SETOR = ' + sector + '</tr><td>'])

                                    for lns in range(14, self.tablesectors.shape[1] - 2):
                                        paramsector = self.tablesectors[lns][isc]
                                        self.kmltext.writelines(
                                            ['<tr><td>' + fieldsect[lns] + '=' + paramsector + '</tr><td>'])
                                    self.kmltext.writelines([']]></description>\n'])

                                    self.kmltext.writelines(['\t\t\t<Style id="corset">\n', '\t\t\t\t<PolyStyle>\n',
                                                             '\t\t\t\t\t<color>' + colorsec + '</color>\n',
                                                             '\t\t\t\t</PolyStyle>\n',
                                                             '\t\t\t</Style>\n'])
                                    latp1 = lat + (250 * (180 / mt.pi) * mt.cos(
                                        (azimuth - bandhor / 2) * mt.pi / 180)) / 6371000
                                    lonp1 = long + (250 * (180 / mt.pi) * mt.sin(
                                        (azimuth - bandhor / 2) * mt.pi / 180)) / 6371000

                                    latp2 = lat + (250 * (180 / mt.pi) * mt.cos(
                                        (azimuth + bandhor / 2) * mt.pi / 180)) / 6371000
                                    lonp2 = long + (250 * (180 / mt.pi) * mt.sin(
                                        (azimuth + bandhor / 2) * mt.pi / 180)) / 6371000
                                    heigthf = height - 250 * mt.tan(tilt * mt.pi / 180)

                                    self.kmltext.writelines(
                                        ['\t\t\t\t<Polygon>\n', '\t\t\t\t\t<altitudeMode>absolute</altitudeMode>\n',
                                         '\t\t\t\t\t<outerBoundaryIs>\n', '\t\t\t\t\t\t<LinearRing>\n'
                                                                          '\t\t\t\t\t\t\t<coordinates>\n',
                                         '\t\t\t\t\t\t\t\t' + str(long) + ',' + str(lat) + ',' + str(height) + ' ' +
                                         str(lonp1) + ',' + str(latp1) + ',' + str(heigthf) + ' ' + str(
                                             lonp2) + ',' + str(latp2) + ',' + str(heigthf) + ' '
                                         + str(long) + ',' + str(lat) + ',' + str(height) + '\n',
                                         '\t\t\t\t\t\t\t</coordinates>\n',
                                         '\t\t\t\t\t\t</LinearRing>\n', '\t\t\t\t\t</outerBoundaryIs>\n',
                                         '\t\t\t\t\t<heading>90</heading><tilt>10</tilt>\n',
                                         '\t\t\t\t</Polygon>\n', '\t\t\t\t<StyleUrl>#corset</StyleUrl>\n',
                                         '\t\t\t</Placemark>\n'])

                                else:
                                    pass
                                if counter > 0:
                                    xy = terminator - counter
                                    if xy == 1:
                                        break
                                terminator = terminator + 1

                        self.kmltext.writelines(['\t\t</Folder>\n'])
                    else:
                        pass
                self.kmltext.writelines(['\t</Folder>\n'])
            self.kmltext.writelines(['</Document>\n', '</kml>\n'])
            self.kmltext.close()
            self.valsite = 'bola'
            try:
                self.pathfile = 'del ' + pathl[0] + '/database/temporary/KML_Google_Sites.kml'
                self.pathfile = self.pathfile.replace('/', os.sep)
                os.system(self.pathfile)
            except:
                pass
            self.pathfile = 'rename ' + pathl[0] + '/database/temporary/KML_Google_Sites.txt KML_Google_Sites.kml'
            self.pathfile = self.pathfile.replace('/', os.sep)
            os.system(self.pathfile)
        except:
            self.valsite = 'bola'
            pass

    def group(self):
        try:
            self.ui.selectgroup.clear()
            items = ('sites', 'sectors')
            self.seltable = QInputDialog.getItem(self, 'Select Table', 'Select Table to set color', items, 0, False)
            self.table = self.seltable[0] + 'temp'
            sqlquery = 'SELECT * FROM ' + self.table + ' WHERE SELECTOR="selected"'
            cur.execute(sqlquery)
            self.tablechart = pd.DataFrame(cur.fetchall())

            aux = list(cur.description)
            for i in aux:
                self.ui.selectgroup.addItem(i[0])
        except:
            pass

    def chart(self):
        try:
            self.figure.clear()
            self.ax = self.figure.subplots()
            self.position = self.ui.selectgroup.currentIndex()
            self.titleinput = QInputDialog.getText(self, 'Select Title', 'Set Table title')
            self.title = self.titleinput[0]
            self.ax.set_title(self.title)

            self.varx = list(self.tablechart[self.position].unique())
            self.vary = list(self.tablechart[self.position].value_counts())
            self.ax.set_xlabel(self.ui.selectgroup.currentText())
            x = np.arange(len(self.varx))
            rects = self.ax.bar(x, self.vary, 0.35)
            self.ax.set_xticks(x)
            self.ax.set_xticklabels(self.varx)

            for rect in rects:
                height = rect.get_height()
                self.ax.annotate('{}'.format(height),
                                 xy=(rect.get_x() + rect.get_width() / 2, height),
                                 xytext=(0, 3),  # 3 points vertical offset
                                 textcoords="offset points",
                                 ha='center', va='bottom')

            self.figure.tight_layout()
            self.canvas.draw()

        except:
            pass


def main():
    app = QtWidgets.QApplication([])
    mwindow = gwindow()
    mwindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
