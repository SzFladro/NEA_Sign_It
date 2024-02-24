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

from Interface import OverviewInterface 
OverviewUI = OverviewInterface.InterfaceOverview

class InterfaceCatalogue:
    _existingFrames = [] 
    UI=None

    @classmethod
    def set_ui(cls, ui_instance):
        cls.UI = ui_instance
        OverviewUI.set_ui(ui_instance)

    @classmethod
    def createWidgets(cls,word_instance, row_number, column_number):
        frame = QFrame(cls.UI.CatalogueWidget)
        frame.setObjectName(u"frame")
        frame.setMinimumSize(100, 100)
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        cls.UI.gridLayout.addWidget(frame, row_number, column_number, 1, 1, Qt.AlignHCenter | Qt.AlignVCenter)

        vertical_layout = QVBoxLayout(frame)

        word_frame = QFrame(frame)
        word_frame.setObjectName(u"WordFrame")
        word_frame.setFrameShape(QFrame.StyledPanel)
        word_frame.setFrameShadow(QFrame.Raised)
        vertical_layout_2 = QVBoxLayout(word_frame)

        word_label = QLabel(word_frame)
        word_label.setObjectName(u"WordLabel")
        word_label.setText(word_instance.name)
        vertical_layout_2.addWidget(word_label)
        vertical_layout.addWidget(word_frame, 0, Qt.AlignTop)

        image_frame = QFrame(frame)
        image_frame.setObjectName(u"ImageFrame")
        size_policy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(image_frame.sizePolicy().hasHeightForWidth())
        image_frame.setSizePolicy(size_policy)
        image_frame.setFrameShape(QFrame.StyledPanel)
        image_frame.setFrameShadow(QFrame.Raised)
        vertical_layout.addWidget(image_frame)

        button_frame = QFrame(frame)
        button_frame.setObjectName(u"ButtonFrame")
        button_frame.setFrameShape(QFrame.StyledPanel)
        button_frame.setFrameShadow(QFrame.Raised)
        vertical_layout_3 = QVBoxLayout(button_frame)

        go_to_button = QPushButton(button_frame)
        go_to_button.setObjectName(u"GoToButton")
        go_to_button.setText("GoToOverview")
        go_to_button.clicked.connect(lambda: cls.goto_overview(word_instance))
        vertical_layout_3.addWidget(go_to_button, 0, Qt.AlignRight)

        vertical_layout.addWidget(button_frame, 0, Qt.AlignBottom)

        cls._existingFrames.append(frame)

    @classmethod
    def frame_creator(cls, window,results):
        window_size = window.size()
        window_width = window_size.width()
        window_height = window_size.height()
        x_max = window_width // 300
        y_max = window_height // 200
        x = 0
        y = 0
        cls.clear_frames()

        for instance in results:
            cls.createWidgets(instance, y, x)
            if x == x_max:
                y += 1
                x = 0
            else:
                x += 1

    @classmethod
    def clear_frames(cls):
        for frame in cls._existingFrames:
            frame.setParent(None)
            frame.deleteLater()
        cls._existingFrames =[]

    @classmethod
    def goto_overview(cls, word):
        OverviewUI.set_wordinstance(word)
        OverviewUI.overviewInterface()




