# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BigReport.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmBigReport(object):
    def setupUi(self, frmBigReport):
        frmBigReport.setObjectName("frmBigReport")
        frmBigReport.resize(1000, 625)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(frmBigReport.sizePolicy().hasHeightForWidth())
        frmBigReport.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon_tripreport.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmBigReport.setWindowIcon(icon)
        self.scrollArea = QtWidgets.QScrollArea(frmBigReport)
        self.scrollArea.setGeometry(QtCore.QRect(9, 9, 720, 427))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 720, 427))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblLocation = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblLocation.sizePolicy().hasHeightForWidth())
        self.lblLocation.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblLocation.setFont(font)
        self.lblLocation.setObjectName("lblLocation")
        self.verticalLayout_2.addWidget(self.lblLocation)
        self.lblDateRange = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDateRange.sizePolicy().hasHeightForWidth())
        self.lblDateRange.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lblDateRange.setFont(font)
        self.lblDateRange.setObjectName("lblDateRange")
        self.verticalLayout_2.addWidget(self.lblDateRange)
        self.lblDetails = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDetails.sizePolicy().hasHeightForWidth())
        self.lblDetails.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lblDetails.setFont(font)
        self.lblDetails.setObjectName("lblDetails")
        self.verticalLayout_2.addWidget(self.lblDetails)
        self.lblLocationsVisited = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblLocationsVisited.sizePolicy().hasHeightForWidth())
        self.lblLocationsVisited.setSizePolicy(sizePolicy)
        self.lblLocationsVisited.setObjectName("lblLocationsVisited")
        self.verticalLayout_2.addWidget(self.lblLocationsVisited)
        self.lblTopSpeciesSeen = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTopSpeciesSeen.sizePolicy().hasHeightForWidth())
        self.lblTopSpeciesSeen.setSizePolicy(sizePolicy)
        self.lblTopSpeciesSeen.setObjectName("lblTopSpeciesSeen")
        self.verticalLayout_2.addWidget(self.lblTopSpeciesSeen)
        self.tabAnalysis = QtWidgets.QTabWidget(self.scrollAreaWidgetContents)
        self.tabAnalysis.setObjectName("tabAnalysis")
        self.tabSpecies = QtWidgets.QWidget()
        self.tabSpecies.setObjectName("tabSpecies")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tabSpecies)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tblSpecies = QtWidgets.QTableWidget(self.tabSpecies)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblSpecies.sizePolicy().hasHeightForWidth())
        self.tblSpecies.setSizePolicy(sizePolicy)
        self.tblSpecies.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tblSpecies.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tblSpecies.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tblSpecies.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblSpecies.setObjectName("tblSpecies")
        self.tblSpecies.setColumnCount(0)
        self.tblSpecies.setRowCount(0)
        self.tblSpecies.horizontalHeader().setVisible(False)
        self.tblSpecies.horizontalHeader().setHighlightSections(False)
        self.tblSpecies.verticalHeader().setVisible(False)
        self.tblSpecies.verticalHeader().setHighlightSections(False)
        self.horizontalLayout.addWidget(self.tblSpecies)
        self.tabAnalysis.addTab(self.tabSpecies, "")
        self.tabDates = QtWidgets.QWidget()
        self.tabDates.setObjectName("tabDates")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tabDates)
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.tabDates)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setLineWidth(0)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_8.setContentsMargins(5, 5, -1, 5)
        self.verticalLayout_8.setSpacing(4)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.lblDatesSeen = QtWidgets.QLabel(self.frame_4)
        self.lblDatesSeen.setObjectName("lblDatesSeen")
        self.verticalLayout_8.addWidget(self.lblDatesSeen)
        self.lstDates = QtWidgets.QListWidget(self.frame_4)
        self.lstDates.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.lstDates.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.lstDates.setProperty("showDropIndicator", False)
        self.lstDates.setObjectName("lstDates")
        self.verticalLayout_8.addWidget(self.lstDates)
        self.horizontalLayout_3.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.tabDates)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_5.setLineWidth(0)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setContentsMargins(-1, 5, 5, 5)
        self.verticalLayout_7.setSpacing(4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.lblSpeciesSeen = QtWidgets.QLabel(self.frame_5)
        self.lblSpeciesSeen.setObjectName("lblSpeciesSeen")
        self.verticalLayout_7.addWidget(self.lblSpeciesSeen)
        self.lstSpecies = QtWidgets.QListWidget(self.frame_5)
        self.lstSpecies.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.lstSpecies.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.lstSpecies.setProperty("showDropIndicator", False)
        self.lstSpecies.setObjectName("lstSpecies")
        self.verticalLayout_7.addWidget(self.lstSpecies)
        self.horizontalLayout_3.addWidget(self.frame_5)
        self.tabAnalysis.addTab(self.tabDates, "")
        self.tabLocations = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabLocations.sizePolicy().hasHeightForWidth())
        self.tabLocations.setSizePolicy(sizePolicy)
        self.tabLocations.setObjectName("tabLocations")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tabLocations)
        self.horizontalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_4.setSpacing(4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_6 = QtWidgets.QFrame(self.tabLocations)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_6.setLineWidth(0)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_9.setSpacing(4)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.lblLocations = QtWidgets.QLabel(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblLocations.sizePolicy().hasHeightForWidth())
        self.lblLocations.setSizePolicy(sizePolicy)
        self.lblLocations.setObjectName("lblLocations")
        self.verticalLayout_9.addWidget(self.lblLocations)
        self.lstLocations = QtWidgets.QListWidget(self.frame_6)
        self.lstLocations.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.lstLocations.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.lstLocations.setProperty("showDropIndicator", False)
        self.lstLocations.setObjectName("lstLocations")
        self.verticalLayout_9.addWidget(self.lstLocations)
        self.horizontalLayout_4.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.tabLocations)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_7.setLineWidth(0)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_10.setSpacing(4)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.lblLocationSpecies = QtWidgets.QLabel(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblLocationSpecies.sizePolicy().hasHeightForWidth())
        self.lblLocationSpecies.setSizePolicy(sizePolicy)
        self.lblLocationSpecies.setObjectName("lblLocationSpecies")
        self.verticalLayout_10.addWidget(self.lblLocationSpecies)
        self.lstLocationSpecies = QtWidgets.QListWidget(self.frame_7)
        self.lstLocationSpecies.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.lstLocationSpecies.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.lstLocationSpecies.setProperty("showDropIndicator", False)
        self.lstLocationSpecies.setObjectName("lstLocationSpecies")
        self.verticalLayout_10.addWidget(self.lstLocationSpecies)
        self.horizontalLayout_4.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.tabLocations)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_8.setLineWidth(0)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_11.setSpacing(4)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.lblLocationUniqueSpecies = QtWidgets.QLabel(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblLocationUniqueSpecies.sizePolicy().hasHeightForWidth())
        self.lblLocationUniqueSpecies.setSizePolicy(sizePolicy)
        self.lblLocationUniqueSpecies.setObjectName("lblLocationUniqueSpecies")
        self.verticalLayout_11.addWidget(self.lblLocationUniqueSpecies)
        self.lstLocationUniqueSpecies = QtWidgets.QListWidget(self.frame_8)
        self.lstLocationUniqueSpecies.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.lstLocationUniqueSpecies.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.lstLocationUniqueSpecies.setProperty("showDropIndicator", False)
        self.lstLocationUniqueSpecies.setObjectName("lstLocationUniqueSpecies")
        self.verticalLayout_11.addWidget(self.lstLocationUniqueSpecies)
        self.horizontalLayout_4.addWidget(self.frame_8)
        self.tabAnalysis.addTab(self.tabLocations, "")
        self.tabMap = QtWidgets.QWidget()
        self.tabMap.setObjectName("tabMap")
        self.tabAnalysis.addTab(self.tabMap, "")
        self.tabNewDates = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabNewDates.sizePolicy().hasHeightForWidth())
        self.tabNewDates.setSizePolicy(sizePolicy)
        self.tabNewDates.setObjectName("tabNewDates")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tabNewDates)
        self.horizontalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_5.setSpacing(4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_9 = QtWidgets.QFrame(self.tabNewDates)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_9.setLineWidth(0)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_12.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_12.setSpacing(4)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.lblNewLifeSpecies = QtWidgets.QLabel(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblNewLifeSpecies.sizePolicy().hasHeightForWidth())
        self.lblNewLifeSpecies.setSizePolicy(sizePolicy)
        self.lblNewLifeSpecies.setObjectName("lblNewLifeSpecies")
        self.verticalLayout_12.addWidget(self.lblNewLifeSpecies)
        self.lstNewLifeSpecies = QtWidgets.QListWidget(self.frame_9)
        self.lstNewLifeSpecies.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.lstNewLifeSpecies.setObjectName("lstNewLifeSpecies")
        self.verticalLayout_12.addWidget(self.lstNewLifeSpecies)
        self.horizontalLayout_5.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(self.tabNewDates)
        self.frame_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_10.setLineWidth(0)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_13.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_13.setSpacing(4)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.lblNewYearSpecies = QtWidgets.QLabel(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblNewYearSpecies.sizePolicy().hasHeightForWidth())
        self.lblNewYearSpecies.setSizePolicy(sizePolicy)
        self.lblNewYearSpecies.setObjectName("lblNewYearSpecies")
        self.verticalLayout_13.addWidget(self.lblNewYearSpecies)
        self.tblNewYearSpecies = QtWidgets.QTableWidget(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblNewYearSpecies.sizePolicy().hasHeightForWidth())
        self.tblNewYearSpecies.setSizePolicy(sizePolicy)
        self.tblNewYearSpecies.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tblNewYearSpecies.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tblNewYearSpecies.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tblNewYearSpecies.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblNewYearSpecies.setObjectName("tblNewYearSpecies")
        self.tblNewYearSpecies.setColumnCount(0)
        self.tblNewYearSpecies.setRowCount(0)
        self.tblNewYearSpecies.horizontalHeader().setVisible(False)
        self.tblNewYearSpecies.horizontalHeader().setHighlightSections(False)
        self.tblNewYearSpecies.verticalHeader().setVisible(False)
        self.tblNewYearSpecies.verticalHeader().setHighlightSections(False)
        self.verticalLayout_13.addWidget(self.tblNewYearSpecies)
        self.horizontalLayout_5.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.tabNewDates)
        self.frame_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_11.setLineWidth(0)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_14.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_14.setSpacing(4)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.lblNewMonthSpecies = QtWidgets.QLabel(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblNewMonthSpecies.sizePolicy().hasHeightForWidth())
        self.lblNewMonthSpecies.setSizePolicy(sizePolicy)
        self.lblNewMonthSpecies.setObjectName("lblNewMonthSpecies")
        self.verticalLayout_14.addWidget(self.lblNewMonthSpecies)
        self.tblNewMonthSpecies = QtWidgets.QTableWidget(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblNewMonthSpecies.sizePolicy().hasHeightForWidth())
        self.tblNewMonthSpecies.setSizePolicy(sizePolicy)
        self.tblNewMonthSpecies.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tblNewMonthSpecies.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tblNewMonthSpecies.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tblNewMonthSpecies.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblNewMonthSpecies.setObjectName("tblNewMonthSpecies")
        self.tblNewMonthSpecies.setColumnCount(0)
        self.tblNewMonthSpecies.setRowCount(0)
        self.tblNewMonthSpecies.horizontalHeader().setVisible(False)
        self.tblNewMonthSpecies.horizontalHeader().setHighlightSections(False)
        self.tblNewMonthSpecies.verticalHeader().setVisible(False)
        self.tblNewMonthSpecies.verticalHeader().setHighlightSections(False)
        self.verticalLayout_14.addWidget(self.tblNewMonthSpecies)
        self.horizontalLayout_5.addWidget(self.frame_11)
        self.tabAnalysis.addTab(self.tabNewDates, "")
        self.tabNewRegions = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabNewRegions.sizePolicy().hasHeightForWidth())
        self.tabNewRegions.setSizePolicy(sizePolicy)
        self.tabNewRegions.setObjectName("tabNewRegions")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tabNewRegions)
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.tabNewRegions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setContentsMargins(5, 5, 9, 5)
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lblNewCountrySpecies = QtWidgets.QLabel(self.frame_2)
        self.lblNewCountrySpecies.setObjectName("lblNewCountrySpecies")
        self.verticalLayout_4.addWidget(self.lblNewCountrySpecies)
        self.tblNewCountrySpecies = QtWidgets.QTableWidget(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblNewCountrySpecies.sizePolicy().hasHeightForWidth())
        self.tblNewCountrySpecies.setSizePolicy(sizePolicy)
        self.tblNewCountrySpecies.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tblNewCountrySpecies.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tblNewCountrySpecies.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tblNewCountrySpecies.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblNewCountrySpecies.setObjectName("tblNewCountrySpecies")
        self.tblNewCountrySpecies.setColumnCount(0)
        self.tblNewCountrySpecies.setRowCount(0)
        self.tblNewCountrySpecies.horizontalHeader().setVisible(False)
        self.tblNewCountrySpecies.horizontalHeader().setHighlightSections(False)
        self.tblNewCountrySpecies.verticalHeader().setVisible(False)
        self.tblNewCountrySpecies.verticalHeader().setHighlightSections(False)
        self.verticalLayout_4.addWidget(self.tblNewCountrySpecies)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.tabNewRegions)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setLineWidth(0)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_6.setSpacing(4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lblNewStateSpecies = QtWidgets.QLabel(self.frame_3)
        self.lblNewStateSpecies.setObjectName("lblNewStateSpecies")
        self.verticalLayout_6.addWidget(self.lblNewStateSpecies)
        self.tblNewStateSpecies = QtWidgets.QTableWidget(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblNewStateSpecies.sizePolicy().hasHeightForWidth())
        self.tblNewStateSpecies.setSizePolicy(sizePolicy)
        self.tblNewStateSpecies.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tblNewStateSpecies.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tblNewStateSpecies.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tblNewStateSpecies.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblNewStateSpecies.setObjectName("tblNewStateSpecies")
        self.tblNewStateSpecies.setColumnCount(0)
        self.tblNewStateSpecies.setRowCount(0)
        self.tblNewStateSpecies.horizontalHeader().setVisible(False)
        self.tblNewStateSpecies.horizontalHeader().setHighlightSections(False)
        self.tblNewStateSpecies.verticalHeader().setVisible(False)
        self.tblNewStateSpecies.verticalHeader().setHighlightSections(False)
        self.verticalLayout_6.addWidget(self.tblNewStateSpecies)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.frame = QtWidgets.QFrame(self.tabNewRegions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setContentsMargins(9, 5, 5, 5)
        self.verticalLayout_5.setSpacing(4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lblNewCountySpecies = QtWidgets.QLabel(self.frame)
        self.lblNewCountySpecies.setObjectName("lblNewCountySpecies")
        self.verticalLayout_5.addWidget(self.lblNewCountySpecies)
        self.tblNewCountySpecies = QtWidgets.QTableWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblNewCountySpecies.sizePolicy().hasHeightForWidth())
        self.tblNewCountySpecies.setSizePolicy(sizePolicy)
        self.tblNewCountySpecies.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tblNewCountySpecies.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tblNewCountySpecies.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tblNewCountySpecies.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblNewCountySpecies.setObjectName("tblNewCountySpecies")
        self.tblNewCountySpecies.setColumnCount(0)
        self.tblNewCountySpecies.setRowCount(0)
        self.tblNewCountySpecies.horizontalHeader().setVisible(False)
        self.tblNewCountySpecies.horizontalHeader().setHighlightSections(False)
        self.tblNewCountySpecies.verticalHeader().setVisible(False)
        self.tblNewCountySpecies.verticalHeader().setHighlightSections(False)
        self.verticalLayout_5.addWidget(self.tblNewCountySpecies)
        self.horizontalLayout_2.addWidget(self.frame)
        self.tabAnalysis.addTab(self.tabNewRegions, "")
        self.tabNewLocations = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabNewLocations.sizePolicy().hasHeightForWidth())
        self.tabNewLocations.setSizePolicy(sizePolicy)
        self.tabNewLocations.setObjectName("tabNewLocations")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tabNewLocations)
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lblNewLocationSpecies = QtWidgets.QLabel(self.tabNewLocations)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblNewLocationSpecies.sizePolicy().hasHeightForWidth())
        self.lblNewLocationSpecies.setSizePolicy(sizePolicy)
        self.lblNewLocationSpecies.setObjectName("lblNewLocationSpecies")
        self.verticalLayout_3.addWidget(self.lblNewLocationSpecies)
        self.tblNewLocationSpecies = QtWidgets.QTableWidget(self.tabNewLocations)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblNewLocationSpecies.sizePolicy().hasHeightForWidth())
        self.tblNewLocationSpecies.setSizePolicy(sizePolicy)
        self.tblNewLocationSpecies.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tblNewLocationSpecies.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tblNewLocationSpecies.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tblNewLocationSpecies.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblNewLocationSpecies.setObjectName("tblNewLocationSpecies")
        self.tblNewLocationSpecies.setColumnCount(0)
        self.tblNewLocationSpecies.setRowCount(0)
        self.tblNewLocationSpecies.horizontalHeader().setVisible(False)
        self.tblNewLocationSpecies.horizontalHeader().setHighlightSections(False)
        self.tblNewLocationSpecies.verticalHeader().setVisible(False)
        self.tblNewLocationSpecies.verticalHeader().setHighlightSections(False)
        self.verticalLayout_3.addWidget(self.tblNewLocationSpecies)
        self.tabAnalysis.addTab(self.tabNewLocations, "")
        self.verticalLayout_2.addWidget(self.tabAnalysis)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.actionSetDateFilter = QtWidgets.QAction(frmBigReport)
        self.actionSetDateFilter.setObjectName("actionSetDateFilter")
        self.actionSetLocationFilter = QtWidgets.QAction(frmBigReport)
        self.actionSetLocationFilter.setObjectName("actionSetLocationFilter")
        self.actionSetFirstDateFilter = QtWidgets.QAction(frmBigReport)
        self.actionSetFirstDateFilter.setObjectName("actionSetFirstDateFilter")
        self.actionSetLastDateFilter = QtWidgets.QAction(frmBigReport)
        self.actionSetLastDateFilter.setObjectName("actionSetLastDateFilter")
        self.actionSetSpeciesFilter = QtWidgets.QAction(frmBigReport)
        self.actionSetSpeciesFilter.setObjectName("actionSetSpeciesFilter")
        self.actionSetCountryFilter = QtWidgets.QAction(frmBigReport)
        self.actionSetCountryFilter.setObjectName("actionSetCountryFilter")
        self.actionSetStateFilter = QtWidgets.QAction(frmBigReport)
        self.actionSetStateFilter.setObjectName("actionSetStateFilter")
        self.actionSetCountyFilter = QtWidgets.QAction(frmBigReport)
        self.actionSetCountyFilter.setObjectName("actionSetCountyFilter")
        self.actionSetDateFilterToYear = QtWidgets.QAction(frmBigReport)
        self.actionSetDateFilterToYear.setObjectName("actionSetDateFilterToYear")
        self.actionSetDateFilterToMonth = QtWidgets.QAction(frmBigReport)
        self.actionSetDateFilterToMonth.setObjectName("actionSetDateFilterToMonth")

        self.retranslateUi(frmBigReport)
        self.tabAnalysis.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(frmBigReport)

    def retranslateUi(self, frmBigReport):
        _translate = QtCore.QCoreApplication.translate
        frmBigReport.setWindowTitle(_translate("frmBigReport", "Location Report"))
        self.lblLocation.setText(_translate("frmBigReport", "Location"))
        self.lblDateRange.setText(_translate("frmBigReport", "Date Range"))
        self.lblDetails.setText(_translate("frmBigReport", "Details Label"))
        self.lblLocationsVisited.setText(_translate("frmBigReport", "Locations Visited:"))
        self.lblTopSpeciesSeen.setText(_translate("frmBigReport", "Species Seen:"))
        self.tblSpecies.setSortingEnabled(True)
        self.tabAnalysis.setTabText(self.tabAnalysis.indexOf(self.tabSpecies), _translate("frmBigReport", "Species"))
        self.lblDatesSeen.setText(_translate("frmBigReport", "Dates"))
        self.lstDates.setSortingEnabled(False)
        self.lblSpeciesSeen.setText(_translate("frmBigReport", "Species Seen on Selected Date"))
        self.lstSpecies.setSortingEnabled(False)
        self.tabAnalysis.setTabText(self.tabAnalysis.indexOf(self.tabDates), _translate("frmBigReport", "Dates"))
        self.lblLocations.setText(_translate("frmBigReport", "Locations"))
        self.lstLocations.setSortingEnabled(False)
        self.lblLocationSpecies.setText(_translate("frmBigReport", "Species seen at Selected Location"))
        self.lstLocationSpecies.setSortingEnabled(False)
        self.lblLocationUniqueSpecies.setText(_translate("frmBigReport", "Species seen ONLY at Selected Location"))
        self.lstLocationUniqueSpecies.setSortingEnabled(False)
        self.tabAnalysis.setTabText(self.tabAnalysis.indexOf(self.tabLocations), _translate("frmBigReport", "Locations"))
        self.tabAnalysis.setTabText(self.tabAnalysis.indexOf(self.tabMap), _translate("frmBigReport", "Map"))
        self.lblNewLifeSpecies.setText(_translate("frmBigReport", "New Life Species"))
        self.lblNewYearSpecies.setText(_translate("frmBigReport", "New Year Species"))
        self.tblNewYearSpecies.setSortingEnabled(True)
        self.lblNewMonthSpecies.setText(_translate("frmBigReport", "New Species for Month Range"))
        self.tblNewMonthSpecies.setSortingEnabled(True)
        self.tabAnalysis.setTabText(self.tabAnalysis.indexOf(self.tabNewDates), _translate("frmBigReport", "New for Dates"))
        self.lblNewCountrySpecies.setText(_translate("frmBigReport", "New Country Species"))
        self.tblNewCountrySpecies.setSortingEnabled(True)
        self.lblNewStateSpecies.setText(_translate("frmBigReport", "New State Species"))
        self.tblNewStateSpecies.setSortingEnabled(True)
        self.lblNewCountySpecies.setText(_translate("frmBigReport", "New County Species"))
        self.tblNewCountySpecies.setSortingEnabled(True)
        self.tabAnalysis.setTabText(self.tabAnalysis.indexOf(self.tabNewRegions), _translate("frmBigReport", "New for Regions"))
        self.lblNewLocationSpecies.setText(_translate("frmBigReport", "New Location Species"))
        self.tblNewLocationSpecies.setSortingEnabled(True)
        self.tabAnalysis.setTabText(self.tabAnalysis.indexOf(self.tabNewLocations), _translate("frmBigReport", "New for Locations"))
        self.actionSetDateFilter.setText(_translate("frmBigReport", "Set Filter to Date"))
        self.actionSetLocationFilter.setText(_translate("frmBigReport", "Set Filter to Location"))
        self.actionSetFirstDateFilter.setText(_translate("frmBigReport", "Set Filter to \"First\" Date"))
        self.actionSetLastDateFilter.setText(_translate("frmBigReport", "Set Filter to \"Last\" Date"))
        self.actionSetSpeciesFilter.setText(_translate("frmBigReport", "Set Filter to Species"))
        self.actionSetCountryFilter.setText(_translate("frmBigReport", "Set Filter to Country"))
        self.actionSetStateFilter.setText(_translate("frmBigReport", "Set Filter to State"))
        self.actionSetCountyFilter.setText(_translate("frmBigReport", "Set Filter to County"))
        self.actionSetDateFilterToYear.setText(_translate("frmBigReport", "Set Filter To Year"))
        self.actionSetDateFilterToMonth.setText(_translate("frmBigReport", "Set Filter to Month"))

import icons_rc
