# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nextHolidayCalendar.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
        Dialog.resize(757, 434)
        self.nextHolidayGroupBox = QtGui.QGroupBox(Dialog)
        self.nextHolidayGroupBox.setGeometry(QtCore.QRect(9, 9, 701, 391))
        self.nextHolidayGroupBox.setObjectName(_fromUtf8("nextHolidayGroupBox"))
        self.studentInfoLayout = QtGui.QGroupBox(self.nextHolidayGroupBox)
        self.studentInfoLayout.setGeometry(QtCore.QRect(350, 290, 341, 91))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.studentInfoLayout.sizePolicy().hasHeightForWidth())
        self.studentInfoLayout.setSizePolicy(sizePolicy)
        self.studentInfoLayout.setObjectName(_fromUtf8("studentInfoLayout"))
        self.layoutWidget = QtGui.QWidget(self.studentInfoLayout)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 30, 291, 56))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.studentLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.studentLayout.setObjectName(_fromUtf8("studentLayout"))
        self.studentLabelsLayout = QtGui.QVBoxLayout()
        self.studentLabelsLayout.setObjectName(_fromUtf8("studentLabelsLayout"))
        self.studNameDescLabel = QtGui.QLabel(self.layoutWidget)
        self.studNameDescLabel.setEnabled(True)
        self.studNameDescLabel.setObjectName(_fromUtf8("studNameDescLabel"))
        self.studentLabelsLayout.addWidget(self.studNameDescLabel)
        self.studNumDesclabel = QtGui.QLabel(self.layoutWidget)
        self.studNumDesclabel.setObjectName(_fromUtf8("studNumDesclabel"))
        self.studentLabelsLayout.addWidget(self.studNumDesclabel)
        self.studentLayout.addLayout(self.studentLabelsLayout)
        self.studentDetailsLayout = QtGui.QVBoxLayout()
        self.studentDetailsLayout.setObjectName(_fromUtf8("studentDetailsLayout"))
        self.studNameLable = QtGui.QLineEdit(self.layoutWidget)
        self.studNameLable.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.studNameLable.sizePolicy().hasHeightForWidth())
        self.studNameLable.setSizePolicy(sizePolicy)
        self.studNameLable.setObjectName(_fromUtf8("studNameLable"))
        self.studentDetailsLayout.addWidget(self.studNameLable)
        self.studNumLable = QtGui.QLineEdit(self.layoutWidget)
        self.studNumLable.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.studNumLable.sizePolicy().hasHeightForWidth())
        self.studNumLable.setSizePolicy(sizePolicy)
        self.studNumLable.setObjectName(_fromUtf8("studNumLable"))
        self.studentDetailsLayout.addWidget(self.studNumLable)
        self.studentLayout.addLayout(self.studentDetailsLayout)
        self.layoutWidget1 = QtGui.QWidget(self.nextHolidayGroupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(12, 22, 681, 261))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.calendarLayout = QtGui.QHBoxLayout(self.layoutWidget1)
        self.calendarLayout.setObjectName(_fromUtf8("calendarLayout"))
        self.todayLayout = QtGui.QVBoxLayout()
        self.todayLayout.setObjectName(_fromUtf8("todayLayout"))
        self.todayCalendarLabel = QtGui.QLabel(self.layoutWidget1)
        self.todayCalendarLabel.setObjectName(_fromUtf8("todayCalendarLabel"))
        self.todayLayout.addWidget(self.todayCalendarLabel)
        self.todayCalendar = QtGui.QCalendarWidget(self.layoutWidget1)
        self.todayCalendar.setMinimumDate(QtCore.QDate(2020, 7, 26))
        self.todayCalendar.setObjectName(_fromUtf8("todayCalendar"))
        self.todayLayout.addWidget(self.todayCalendar)
        self.currentDateLayout = QtGui.QHBoxLayout()
        self.currentDateLayout.setObjectName(_fromUtf8("currentDateLayout"))
        self.currentDate = QtGui.QLabel(self.layoutWidget1)
        self.currentDate.setObjectName(_fromUtf8("currentDate"))
        self.currentDateLayout.addWidget(self.currentDate)
        self.currentDateEdit = QtGui.QDateEdit(self.layoutWidget1)
        self.currentDateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 7, 27), QtCore.QTime(0, 0, 0)))
        self.currentDateEdit.setCurrentSection(QtGui.QDateTimeEdit.DaySection)
        self.currentDateEdit.setDate(QtCore.QDate(2020, 7, 27))
        self.currentDateEdit.setObjectName(_fromUtf8("currentDateEdit"))
        self.currentDateLayout.addWidget(self.currentDateEdit)
        self.todayLayout.addLayout(self.currentDateLayout)
        self.calendarLayout.addLayout(self.todayLayout)
        self.nextHolidayLayout = QtGui.QVBoxLayout()
        self.nextHolidayLayout.setObjectName(_fromUtf8("nextHolidayLayout"))
        self.nextHolidayCalendarLabel = QtGui.QLabel(self.layoutWidget1)
        self.nextHolidayCalendarLabel.setObjectName(_fromUtf8("nextHolidayCalendarLabel"))
        self.nextHolidayLayout.addWidget(self.nextHolidayCalendarLabel)
        self.nextHolidayCalendar = QtGui.QCalendarWidget(self.layoutWidget1)
        self.nextHolidayCalendar.setSelectedDate(QtCore.QDate(2020, 8, 9))
        self.nextHolidayCalendar.setMinimumDate(QtCore.QDate(2020, 8, 9))
        self.nextHolidayCalendar.setObjectName(_fromUtf8("nextHolidayCalendar"))
        self.nextHolidayLayout.addWidget(self.nextHolidayCalendar)
        self.nextHolidayDateLayout = QtGui.QHBoxLayout()
        self.nextHolidayDateLayout.setObjectName(_fromUtf8("nextHolidayDateLayout"))
        self.nextHolidayDateLabel = QtGui.QLabel(self.layoutWidget1)
        self.nextHolidayDateLabel.setObjectName(_fromUtf8("nextHolidayDateLabel"))
        self.nextHolidayDateLayout.addWidget(self.nextHolidayDateLabel)
        self.nextHolidayDateEdit = QtGui.QDateEdit(self.layoutWidget1)
        self.nextHolidayDateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 8, 9), QtCore.QTime(0, 0, 0)))
        self.nextHolidayDateEdit.setObjectName(_fromUtf8("nextHolidayDateEdit"))
        self.nextHolidayDateLayout.addWidget(self.nextHolidayDateEdit)
        self.nextHolidayLayout.addLayout(self.nextHolidayDateLayout)
        self.calendarLayout.addLayout(self.nextHolidayLayout)
        self.layoutWidget2 = QtGui.QWidget(self.nextHolidayGroupBox)
        self.layoutWidget2.setGeometry(QtCore.QRect(30, 330, 277, 23))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.daysUntilNextLayout = QtGui.QHBoxLayout(self.layoutWidget2)
        self.daysUntilNextLayout.setObjectName(_fromUtf8("daysUntilNextLayout"))
        self.daysUntilNextLabel = QtGui.QLabel(self.layoutWidget2)
        self.daysUntilNextLabel.setObjectName(_fromUtf8("daysUntilNextLabel"))
        self.daysUntilNextLayout.addWidget(self.daysUntilNextLabel)
        self.daysUntilNextLineEdit = QtGui.QLineEdit(self.layoutWidget2)
        self.daysUntilNextLineEdit.setEnabled(False)
        self.daysUntilNextLineEdit.setObjectName(_fromUtf8("daysUntilNextLineEdit"))
        self.daysUntilNextLayout.addWidget(self.daysUntilNextLineEdit)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.currentDateEdit, QtCore.SIGNAL(_fromUtf8("dateChanged(QDate)")), self.todayCalendar.setSelectedDate)
        QtCore.QObject.connect(self.nextHolidayDateEdit, QtCore.SIGNAL(_fromUtf8("dateChanged(QDate)")), self.nextHolidayCalendar.setSelectedDate)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Next Holiday Calculator", None))
        self.nextHolidayGroupBox.setTitle(_translate("Dialog", "Next Holiday Calculator", None))
        self.studentInfoLayout.setTitle(_translate("Dialog", "Student Information", None))
        self.studNameDescLabel.setText(_translate("Dialog", "Student Name:", None))
        self.studNumDesclabel.setText(_translate("Dialog", "Student Number:", None))
        self.studNameLable.setText(_translate("Dialog", "Daniel du Preez", None))
        self.studNumLable.setText(_translate("Dialog", "64245179", None))
        self.todayCalendarLabel.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Today Calendar</span></p></body></html>", None))
        self.currentDate.setText(_translate("Dialog", "Current Date:", None))
        self.currentDateEdit.setDisplayFormat(_translate("Dialog", "dd/MM/yyyy", None))
        self.nextHolidayCalendarLabel.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Next Holiday Calendar</span></p></body></html>", None))
        self.nextHolidayDateLabel.setText(_translate("Dialog", "Next Holiday:", None))
        self.nextHolidayDateEdit.setDisplayFormat(_translate("Dialog", "dd/MM/yyyy", None))
        self.daysUntilNextLabel.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Days until next Holiday:</span></p></body></html>", None))
