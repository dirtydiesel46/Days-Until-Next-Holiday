import sys
from daysUntilNextHoliday import *


class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.todayCalendar.setMinimumDate(QtCore.QDate.currentDate())
        QtCore.QObject.connect(self.ui.todayCalendar, QtCore.SIGNAL('selectionChanged()')
                               , self.dispTodayDate)
        QtCore.QObject.connect(self.ui.nextHolidayCalendar, QtCore.SIGNAL('selectionChanged()')
                               , self.dispNextHolidayDate)
        self.daysUntil()

    def dispTodayDate(self):
        self.ui.currentDateEdit.setDate(self.ui.todayCalendar.selectedDate())
        self.daysUntil()

    def dispNextHolidayDate(self):
        self.ui.nextHolidayDateEdit.setDate(self.ui.nextHolidayCalendar.selectedDate())
        self.daysUntil()

    def daysUntil(self):
        todayDate = self.ui.todayCalendar.selectedDate()
        nextDate = self.ui.nextHolidayCalendar.selectedDate()
        differenceDays = str(todayDate.daysTo(nextDate))
        self.ui.daysUntilNextLineEdit.setText(differenceDays)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
