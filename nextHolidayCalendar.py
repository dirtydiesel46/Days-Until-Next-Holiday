# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nextHolidayCalendar.ui'
#
# Created: Sun Jul 26 14:31:10 2020
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(733, 410)
        self.nextHolidayGroupBox = QtGui.QGroupBox(Dialog)
        self.nextHolidayGroupBox.setGeometry(QtCore.QRect(9, 9, 701, 391))
        self.nextHolidayGroupBox.setObjectName(_fromUtf8("nextHolidayGroupBox"))
        self.layoutWidget = QtGui.QWidget(self.nextHolidayGroupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 681, 261))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.calendarsLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.calendarsLayout.setMargin(0)
        self.calendarsLayout.setObjectName(_fromUtf8("calendarsLayout"))
        self.todayCalendarLayout = QtGui.QVBoxLayout()
        self.todayCalendarLayout.setObjectName(_fromUtf8("todayCalendarLayout"))
        self.todayCalendarLabel = QtGui.QLabel(self.layoutWidget)
        self.todayCalendarLabel.setObjectName(_fromUtf8("todayCalendarLabel"))
        self.todayCalendarLayout.addWidget(self.todayCalendarLabel)
        self.todayCalendar = QtGui.QCalendarWidget(self.layoutWidget)
        self.todayCalendar.setObjectName(_fromUtf8("todayCalendar"))
        self.todayCalendarLayout.addWidget(self.todayCalendar)
        self.currentDateSplitter = QtGui.QSplitter(self.layoutWidget)
        self.currentDateSplitter.setOrientation(QtCore.Qt.Horizontal)
        self.currentDateSplitter.setObjectName(_fromUtf8("currentDateSplitter"))
        self.currentDate = QtGui.QLabel(self.currentDateSplitter)
        self.currentDate.setObjectName(_fromUtf8("currentDate"))
        self.currentDateEdit = QtGui.QDateEdit(self.currentDateSplitter)
        self.currentDateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 7, 27), QtCore.QTime(0, 0, 0)))
        self.currentDateEdit.setCurrentSection(QtGui.QDateTimeEdit.DaySection)
        self.currentDateEdit.setDate(QtCore.QDate(2020, 7, 27))
        self.currentDateEdit.setObjectName(_fromUtf8("currentDateEdit"))
        self.todayCalendarLayout.addWidget(self.currentDateSplitter)
        self.calendarsLayout.addLayout(self.todayCalendarLayout)
        self.nextHolidayLayout = QtGui.QVBoxLayout()
        self.nextHolidayLayout.setObjectName(_fromUtf8("nextHolidayLayout"))
        self.nextHolidayCalendarLabel = QtGui.QLabel(self.layoutWidget)
        self.nextHolidayCalendarLabel.setObjectName(_fromUtf8("nextHolidayCalendarLabel"))
        self.nextHolidayLayout.addWidget(self.nextHolidayCalendarLabel)
        self.nextHolidayCalendar = QtGui.QCalendarWidget(self.layoutWidget)
        self.nextHolidayCalendar.setSelectedDate(QtCore.QDate(2020, 8, 9))
        self.nextHolidayCalendar.setObjectName(_fromUtf8("nextHolidayCalendar"))
        self.nextHolidayLayout.addWidget(self.nextHolidayCalendar)
        self.nextHolidaySplitter = QtGui.QSplitter(self.layoutWidget)
        self.nextHolidaySplitter.setOrientation(QtCore.Qt.Horizontal)
        self.nextHolidaySplitter.setObjectName(_fromUtf8("nextHolidaySplitter"))
        self.nextHolidayLabel = QtGui.QLabel(self.nextHolidaySplitter)
        self.nextHolidayLabel.setObjectName(_fromUtf8("nextHolidayLabel"))
        self.nextHolidayDateEdit = QtGui.QDateEdit(self.nextHolidaySplitter)
        self.nextHolidayDateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 8, 9), QtCore.QTime(0, 0, 0)))
        self.nextHolidayDateEdit.setObjectName(_fromUtf8("nextHolidayDateEdit"))
        self.nextHolidayLayout.addWidget(self.nextHolidaySplitter)
        self.calendarsLayout.addLayout(self.nextHolidayLayout)
        self.studentInfoLayout = QtGui.QGroupBox(self.nextHolidayGroupBox)
        self.studentInfoLayout.setGeometry(QtCore.QRect(350, 290, 341, 91))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.studentInfoLayout.sizePolicy().hasHeightForWidth())
        self.studentInfoLayout.setSizePolicy(sizePolicy)
        self.studentInfoLayout.setObjectName(_fromUtf8("studentInfoLayout"))
        self.layoutWidget1 = QtGui.QWidget(self.studentInfoLayout)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 30, 291, 56))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.studentLayout = QtGui.QHBoxLayout(self.layoutWidget1)
        self.studentLayout.setMargin(0)
        self.studentLayout.setObjectName(_fromUtf8("studentLayout"))
        self.studentLabelsLayout = QtGui.QVBoxLayout()
        self.studentLabelsLayout.setObjectName(_fromUtf8("studentLabelsLayout"))
        self.studNameDescLabel = QtGui.QLabel(self.layoutWidget1)
        self.studNameDescLabel.setEnabled(True)
        self.studNameDescLabel.setObjectName(_fromUtf8("studNameDescLabel"))
        self.studentLabelsLayout.addWidget(self.studNameDescLabel)
        self.studNumDesclabel = QtGui.QLabel(self.layoutWidget1)
        self.studNumDesclabel.setObjectName(_fromUtf8("studNumDesclabel"))
        self.studentLabelsLayout.addWidget(self.studNumDesclabel)
        self.studentLayout.addLayout(self.studentLabelsLayout)
        self.studentDetailsLayout = QtGui.QVBoxLayout()
        self.studentDetailsLayout.setObjectName(_fromUtf8("studentDetailsLayout"))
        self.studNameLable = QtGui.QLineEdit(self.layoutWidget1)
        self.studNameLable.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.studNameLable.sizePolicy().hasHeightForWidth())
        self.studNameLable.setSizePolicy(sizePolicy)
        self.studNameLable.setObjectName(_fromUtf8("studNameLable"))
        self.studentDetailsLayout.addWidget(self.studNameLable)
        self.studNumLable = QtGui.QLineEdit(self.layoutWidget1)
        self.studNumLable.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.studNumLable.sizePolicy().hasHeightForWidth())
        self.studNumLable.setSizePolicy(sizePolicy)
        self.studNumLable.setObjectName(_fromUtf8("studNumLable"))
        self.studentDetailsLayout.addWidget(self.studNumLable)
        self.studentLayout.addLayout(self.studentDetailsLayout)
        self.daysUntilNextSplitter = QtGui.QSplitter(self.nextHolidayGroupBox)
        self.daysUntilNextSplitter.setGeometry(QtCore.QRect(30, 330, 307, 20))
        self.daysUntilNextSplitter.setOrientation(QtCore.Qt.Horizontal)
        self.daysUntilNextSplitter.setObjectName(_fromUtf8("daysUntilNextSplitter"))
        self.daysUntilNextLabel = QtGui.QLabel(self.daysUntilNextSplitter)
        self.daysUntilNextLabel.setObjectName(_fromUtf8("daysUntilNextLabel"))
        self.daysUntilNextLineEdit = QtGui.QLineEdit(self.daysUntilNextSplitter)
        self.daysUntilNextLineEdit.setEnabled(False)
        self.daysUntilNextLineEdit.setObjectName(_fromUtf8("daysUntilNextLineEdit"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.currentDateEdit, QtCore.SIGNAL(_fromUtf8("dateChanged(QDate)")), self.todayCalendar.setSelectedDate)
        QtCore.QObject.connect(self.nextHolidayDateEdit, QtCore.SIGNAL(_fromUtf8("dateChanged(QDate)")), self.nextHolidayCalendar.setSelectedDate)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.nextHolidayGroupBox.setTitle(_translate("Dialog", "Next Holiday Calculator", None))
        self.todayCalendarLabel.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Today Calendar</span></p></body></html>", None))
        self.currentDate.setText(_translate("Dialog", "Current Date:", None))
        self.currentDateEdit.setDisplayFormat(_translate("Dialog", "dd/MM/yyyy", None))
        self.nextHolidayCalendarLabel.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Next Holiday Calendar</span></p></body></html>", None))
        self.nextHolidayLabel.setText(_translate("Dialog", "Next Holiday:", None))
        self.nextHolidayDateEdit.setDisplayFormat(_translate("Dialog", "dd/MM/yyyy", None))
        self.studentInfoLayout.setTitle(_translate("Dialog", "Student Information", None))
        self.studNameDescLabel.setText(_translate("Dialog", "Student Name:", None))
        self.studNumDesclabel.setText(_translate("Dialog", "Student Number:", None))
        self.studNameLable.setText(_translate("Dialog", "Daniel du Preez", None))
        self.studNumLable.setText(_translate("Dialog", "64245179", None))
        self.daysUntilNextLabel.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Days until next Holiday:</span></p></body></html>", None))

