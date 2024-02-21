from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLayout, QLineEdit, QMainWindow, QProgressBar,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget, QLabel, QPushButton)

class InterfaceOverview:
    UI=None
    wordclass=None

    @classmethod
    def set_ui(cls, ui_instance):
        cls.UI = ui_instance

    @classmethod
    def set_wordinstance(cls, word_instance):
        cls.wordclass = word_instance

    @classmethod
    def overviewInterface(cls):
        cls.UI.MainWidget.setCurrentWidget(cls.UI.Overview)
        cls.UI.WordOverviewlabel.setText(f"{cls.wordclass.name}")
        cls.UI.CategoryOverviewLabel.setText(f"{cls.wordclass.category}")


    def loadvideo():
        downloadlink = cls.wordclass.download_link



    def playvideo():
        print(video)